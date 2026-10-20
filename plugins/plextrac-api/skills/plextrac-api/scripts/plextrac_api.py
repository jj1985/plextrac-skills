#!/usr/bin/env python3
"""PlexTrac API client and CLI (standard library only).

Environment: PLEXTRAC_URL (https://tenant.plextrac.com), PLEXTRAC_USERNAME, PLEXTRAC_PASSWORD,
optional PLEXTRAC_MFA_CODE (6-digit, one-shot), PLEXTRAC_TOKEN (skip login), PLEXTRAC_CA_BUNDLE.

Examples
  python plextrac_api.py whoami
  python plextrac_api.py clients                              # paginated client list
  python plextrac_api.py reports --client 1254                # reports of a client
  python plextrac_api.py findings 1254 500006 --limit 100     # all findings in a report (auto-paged)
  python plextrac_api.py finding 1254 500006 1795388512       # one finding (full object)
  python plextrac_api.py create-finding 1254 500006 finding.json
  python plextrac_api.py update-finding 1254 500006 1795388512 patch.json   # GET + merge + PUT
  python plextrac_api.py export 1254 500006 --format doc --out report.docx [--template-id <exportTemplateId>]
  python plextrac_api.py import-scan 1254 500006 nessus ./scan.nessus --tags web --wait
  python plextrac_api.py raw POST /api/v2/reports --body '{"pagination":{"offset":0,"limit":25}}'
"""
from __future__ import annotations

import argparse
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any, Iterator


class PlexTracError(RuntimeError):
    def __init__(self, message: str, status: int | None = None, payload: Any = None):
        super().__init__(message)
        self.status = status
        self.payload = payload


class PlexTrac:
    """Thin client. Handles login (password/MFA), 15-minute token refresh, JSON and file requests."""

    TOKEN_TTL = 15 * 60
    REFRESH_MARGIN = 3 * 60

    def __init__(self, base_url: str, username: str | None = None, password: str | None = None,
                 token: str | None = None, mfa_code: str | None = None, verify_tls: bool = True,
                 ca_bundle: str | None = None, timeout: int = 120):
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.mfa_code = mfa_code
        self.token = token
        self.tenant_id: int | None = None
        self.token_time = time.time() if token else 0.0
        self.timeout = timeout
        # TLS is verified by default; pass ca_bundle for self-signed on-prem certificates.
        self._ctx = ssl.create_default_context(cafile=ca_bundle) if ca_bundle else ssl.create_default_context()
        if not verify_tls:
            print('WARNING: TLS verification disabled; lab use only.', file=sys.stderr)
            self._ctx.check_hostname = False
            self._ctx.verify_mode = ssl.CERT_NONE

    # ------------------------------------------------------------------ transport
    def _request(self, method: str, path: str, body: Any = None, *, query: dict | None = None,
                 auth: bool = True, raw_body: bytes | None = None, content_type: str | None = None,
                 headers: dict | None = None, absolute: bool = False) -> tuple[int, bytes, dict]:
        url = path if absolute else self.base_url + path
        if query:
            url += ('&' if '?' in url else '?') + urllib.parse.urlencode({k: v for k, v in query.items() if v is not None})
        hdrs = {'Accept': 'application/json'}
        if auth:
            self.ensure_token()
            hdrs['Authorization'] = 'Bearer ' + self.token
        data = None
        if raw_body is not None:
            data = raw_body
            hdrs['Content-Type'] = content_type or 'application/octet-stream'
        elif body is not None:
            data = json.dumps(body).encode('utf-8')
            hdrs['Content-Type'] = 'application/json'
        if headers:
            hdrs.update(headers)
        req = urllib.request.Request(url, data=data, method=method, headers=hdrs)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as resp:
                return resp.status, resp.read(), dict(resp.headers)
        except urllib.error.HTTPError as e:
            payload = e.read()
            try:
                parsed = json.loads(payload)
            except ValueError:
                parsed = payload.decode('utf-8', 'replace')
            raise PlexTracError(f'HTTP {e.code} {method} {path}: {str(parsed)[:500]}', e.code, parsed) from None

    def request(self, method: str, path: str, body: Any = None, **kw) -> Any:
        status, payload, _ = self._request(method, path, body, **kw)
        if not payload:
            return None
        try:
            return json.loads(payload)
        except ValueError:
            return payload.decode('utf-8', 'replace')

    def download(self, path: str, query: dict | None = None) -> bytes:
        _, payload, _ = self._request('GET', path, query=query)
        return payload

    # ------------------------------------------------------------------ auth
    def login(self) -> str:
        if not (self.username and self.password):
            raise PlexTracError('Set PLEXTRAC_USERNAME and PLEXTRAC_PASSWORD (or PLEXTRAC_TOKEN)')
        res = self.request('POST', '/api/v1/authenticate', {'username': self.username, 'password': self.password}, auth=False)
        if isinstance(res, dict) and res.get('code') and not res.get('token'):
            if not self.mfa_code:
                raise PlexTracError('Account requires MFA: set PLEXTRAC_MFA_CODE (6-digit) or use a Service Account', payload=res)
            res = self.request('POST', '/api/v1/authenticate/mfa', {'code': res['code'], 'token': self.mfa_code}, auth=False)
            self.mfa_code = None
        if not isinstance(res, dict) or not res.get('token'):
            raise PlexTracError('Authentication did not return a token', payload=res)
        self.token = res['token']
        self.tenant_id = res.get('tenant_id')
        self.token_time = time.time()
        return self.token

    def refresh(self) -> str:
        res = self.request('PUT', '/api/v1/token/refresh')
        if isinstance(res, dict) and res.get('token'):
            self.token = res['token']
            self.tenant_id = res.get('tenant_id', self.tenant_id)
            self.token_time = time.time()
            return self.token
        return self.login()

    def ensure_token(self) -> None:
        if not self.token:
            self.login()
        elif time.time() - self.token_time > self.TOKEN_TTL - self.REFRESH_MARGIN:
            try:
                # refresh needs a still-valid token; temporarily mark fresh to avoid recursion
                self.token_time = time.time()
                self.refresh()
            except PlexTracError:
                self.login()

    def whoami(self) -> dict:
        return self.request('GET', '/api/v2/whoami')

    # ------------------------------------------------------------------ pagination
    def paginate(self, path: str, limit: int = 25, sort: list | None = None, filters: list | None = None,
                 data_key: str = 'data', max_records: int | None = None) -> Iterator[dict]:
        """Iterate a v2 POST list endpoint ({pagination, sort, filters})."""
        offset = 0
        seen = 0
        while True:
            body = {'pagination': {'offset': offset, 'limit': limit}}
            if sort:
                body['sort'] = sort
            if filters:
                body['filters'] = filters
            res = self.request('POST', path, body)
            rows = res.get(data_key) or res.get('findings') or res.get('assets') or [] if isinstance(res, dict) else res
            for r in rows:
                yield r
                seen += 1
                if max_records and seen >= max_records:
                    return
            total = ((res.get('meta') or {}).get('pagination') or {}).get('total') if isinstance(res, dict) else None
            offset += limit
            if not rows or len(rows) < limit or (total is not None and offset >= total):
                return

    # ------------------------------------------------------------------ helpers
    def clients(self, **kw) -> Iterator[dict]:
        return self.paginate('/api/v2/clients', **kw)

    def reports(self, client_id: int | None = None, **kw) -> Iterator[dict]:
        if client_id is not None:
            filters = (kw.pop('filters', None) or []) + [{'by': 'clients', 'value': [int(client_id)]}]
            return self.paginate('/api/v2/reports', filters=filters, **kw)
        return self.paginate('/api/v2/reports', **kw)

    def findings(self, client_id: int, report_id: int, limit: int = 100, **kw) -> Iterator[dict]:
        if limit not in (1, 10, 50, 100):
            limit = 100
        return self.paginate(f'/api/v2/clients/{client_id}/reports/{report_id}/findings', limit=limit, **kw)

    def finding(self, client_id: int, report_id: int, finding_id: int) -> dict:
        return self.request('GET', f'/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}')

    def create_finding(self, client_id: int, report_id: int, finding: dict) -> dict:
        for k in ('title', 'severity', 'status', 'description'):
            if k not in finding:
                raise PlexTracError(f'finding is missing required field {k!r}')
        return self.request('POST', f'/api/v1/client/{client_id}/report/{report_id}/flaw/create', finding)

    def update_finding(self, client_id: int, report_id: int, finding_id: int, patch: dict) -> dict:
        current = self.finding(client_id, report_id, finding_id)
        current.pop('doc_version', None)
        current.update(patch)
        return self.request('PUT', f'/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}', current)

    def client_assets(self, client_id: int, **kw) -> Iterator[dict]:
        return self.paginate(f'/api/v2/clients/{client_id}/assets', **kw)

    def create_asset(self, client_id: int, asset: dict) -> dict:
        asset.setdefault('doc_type', 'client_asset')
        asset.setdefault('findings', {})
        return self.request('PUT', f'/api/v1/client/{client_id}/asset/0', asset)

    def export_report(self, client_id: int, report_id: int, fmt: str = 'doc', include_evidence: bool = False,
                      template_id: str | None = None) -> bytes:
        if fmt not in ('doc', 'pdf', 'ptrac'):
            raise PlexTracError('format must be doc, pdf or ptrac')
        q = {'includeEvidence': str(include_evidence).lower()} if fmt in ('doc', 'pdf') else None
        if template_id and q is not None:
            q['templateID'] = template_id
        return self.download(f'/api/v1/client/{client_id}/report/{report_id}/export/{fmt}', q)

    def upload_image(self, path: str) -> str:
        """POST /api/v1/uploads (multipart). Returns the fileUrl to embed as <img src="/api/v1/{fileUrl}">."""
        res = self.multipart('/api/v1/uploads', {'file': path})
        return res['fileUrl'] if isinstance(res, dict) else res

    def multipart(self, path: str, files: dict, fields: dict | None = None, method: str = 'POST') -> Any:
        boundary = '----plextrac' + uuid.uuid4().hex
        parts = []
        for k, v in (fields or {}).items():
            parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
        for k, fpath in files.items():
            with open(fpath, 'rb') as fh:
                content = fh.read()
            parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"; filename="{os.path.basename(fpath)}"\r\nContent-Type: application/octet-stream\r\n\r\n'.encode() + content + b'\r\n')
        parts.append(f'--{boundary}--\r\n'.encode())
        return self.request(method, path, raw_body=b''.join(parts), content_type=f'multipart/form-data; boundary={boundary}')

    # ------------------------------------------------------------------ scanner import (streaming upload)
    def import_scan(self, client_id: int, report_id: int, source: str, file_path: str,
                    finding_tags: list | None = None, asset_tags: list | None = None,
                    use_parser_actions: bool = True, wait: bool = False, poll_seconds: int = 10, timeout: int = 1800) -> dict:
        name = os.path.basename(file_path)
        pre = self.request('POST', '/api/v2/presigned-url', {'name': name})
        if not isinstance(pre, dict) or not pre.get('url'):
            raise PlexTracError('presigned-url did not return a url', payload=pre)
        with open(file_path, 'rb') as fh:
            data = fh.read()
        self._request('PUT', pre['url'], raw_body=data, content_type='application/octet-stream', auth=False, absolute=True)
        body = {'key': pre['key'], 'fileName': name, 'useParserActions': 'true' if use_parser_actions else 'false',
                'tags': json.dumps({'assets': asset_tags or [], 'findings': finding_tags or []})}
        res = self.request('POST', f'/api/v2/client/{client_id}/report/{report_id}/preuploaded-import/{source}', body)
        if not wait:
            return res
        op = res.get('operationId') if isinstance(res, dict) else None
        deadline = time.time() + timeout
        last = None
        while time.time() < deadline:
            jobs = self.request('GET', '/api/v2/my-imports') or []
            for j in jobs:
                if j.get('key') == op:
                    last = j
                    if j.get('status') in ('IMPORT COMPLETE', 'ERROR'):
                        return {'queued': res, 'job': j}
            time.sleep(poll_seconds)
        return {'queued': res, 'job': last, 'timedOut': True}


# ---------------------------------------------------------------------- CLI
def _client(a) -> PlexTrac:
    return PlexTrac(
        base_url=a.url or os.environ.get('PLEXTRAC_URL', ''),
        username=a.username or os.environ.get('PLEXTRAC_USERNAME'),
        password=a.password or os.environ.get('PLEXTRAC_PASSWORD'),
        token=os.environ.get('PLEXTRAC_TOKEN'),
        mfa_code=a.mfa_code or os.environ.get('PLEXTRAC_MFA_CODE'),
        verify_tls=not a.insecure,
        ca_bundle=a.ca_bundle or os.environ.get('PLEXTRAC_CA_BUNDLE'),
    )


def _dump(obj: Any) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str))


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--url'); p.add_argument('--username'); p.add_argument('--password'); p.add_argument('--mfa-code')
    p.add_argument('--ca-bundle', help='PEM CA file for self-signed certificates'); p.add_argument('--insecure', action='store_true', help='disable TLS verification (lab only)')
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('whoami')
    s = sub.add_parser('clients'); s.add_argument('--limit', type=int, default=25); s.add_argument('--name')
    s = sub.add_parser('reports'); s.add_argument('--client', type=int); s.add_argument('--limit', type=int, default=25); s.add_argument('--status')
    s = sub.add_parser('findings'); s.add_argument('client_id', type=int); s.add_argument('report_id', type=int); s.add_argument('--limit', type=int, default=100); s.add_argument('--out')
    s = sub.add_parser('finding'); s.add_argument('client_id', type=int); s.add_argument('report_id', type=int); s.add_argument('finding_id', type=int)
    s = sub.add_parser('create-finding'); s.add_argument('client_id', type=int); s.add_argument('report_id', type=int); s.add_argument('json_file')
    s = sub.add_parser('update-finding'); s.add_argument('client_id', type=int); s.add_argument('report_id', type=int); s.add_argument('finding_id', type=int); s.add_argument('patch_json_file')
    s = sub.add_parser('assets'); s.add_argument('client_id', type=int); s.add_argument('--limit', type=int, default=25)
    s = sub.add_parser('export'); s.add_argument('client_id', type=int); s.add_argument('report_id', type=int); s.add_argument('--format', default='doc', choices=['doc', 'pdf', 'ptrac']); s.add_argument('--out'); s.add_argument('--include-evidence', action='store_true'); s.add_argument('--template-id')
    s = sub.add_parser('import-scan'); s.add_argument('client_id', type=int); s.add_argument('report_id', type=int); s.add_argument('source'); s.add_argument('file'); s.add_argument('--tags', nargs='*', default=[]); s.add_argument('--asset-tags', nargs='*', default=[]); s.add_argument('--no-parser-actions', action='store_true'); s.add_argument('--wait', action='store_true')
    sub.add_parser('imports')
    s = sub.add_parser('upload-image'); s.add_argument('file')
    s = sub.add_parser('raw'); s.add_argument('method'); s.add_argument('path'); s.add_argument('--body'); s.add_argument('--out')
    a = p.parse_args(argv)
    c = _client(a)
    try:
        if a.cmd == 'whoami':
            _dump(c.whoami())
        elif a.cmd == 'clients':
            f = [{'by': 'name', 'value': a.name}] if a.name else None
            _dump(list(c.clients(limit=a.limit, filters=f)))
        elif a.cmd == 'reports':
            f = [{'by': 'status', 'value': a.status}] if a.status else None
            _dump(list(c.reports(a.client, limit=a.limit, filters=f)))
        elif a.cmd == 'findings':
            rows = list(c.findings(a.client_id, a.report_id, limit=a.limit))
            if a.out:
                with open(a.out, 'w', encoding='utf-8') as fh:
                    json.dump(rows, fh, indent=1, ensure_ascii=False)
                print(f'{len(rows)} findings -> {a.out}')
            else:
                _dump(rows)
        elif a.cmd == 'finding':
            _dump(c.finding(a.client_id, a.report_id, a.finding_id))
        elif a.cmd == 'create-finding':
            _dump(c.create_finding(a.client_id, a.report_id, json.load(open(a.json_file, encoding='utf-8'))))
        elif a.cmd == 'update-finding':
            _dump(c.update_finding(a.client_id, a.report_id, a.finding_id, json.load(open(a.patch_json_file, encoding='utf-8'))))
        elif a.cmd == 'assets':
            _dump(list(c.client_assets(a.client_id, limit=a.limit)))
        elif a.cmd == 'export':
            data = c.export_report(a.client_id, a.report_id, a.format, a.include_evidence, a.template_id)
            out = a.out or f'report_{a.report_id}.{ {"doc": "docx", "pdf": "pdf", "ptrac": "ptrac"}[a.format] }'
            with open(out, 'wb') as fh:
                fh.write(data)
            print(f'{len(data)} bytes -> {out}')
        elif a.cmd == 'import-scan':
            _dump(c.import_scan(a.client_id, a.report_id, a.source, a.file, a.tags, a.asset_tags, not a.no_parser_actions, a.wait))
        elif a.cmd == 'imports':
            _dump(c.request('GET', '/api/v2/my-imports'))
        elif a.cmd == 'upload-image':
            print(c.upload_image(a.file))
        elif a.cmd == 'raw':
            body = json.loads(a.body) if a.body else None
            if a.out:
                data = c.download(a.path) if a.method.upper() == 'GET' else None
                if data is None:
                    _dump(c.request(a.method.upper(), a.path, body))
                else:
                    open(a.out, 'wb').write(data); print(f'{len(data)} bytes -> {a.out}')
            else:
                _dump(c.request(a.method.upper(), a.path, body))
        return 0
    except PlexTracError as e:
        print(f'ERROR: {e}', file=sys.stderr)
        if e.payload is not None:
            print(json.dumps(e.payload, indent=2, default=str)[:3000], file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
