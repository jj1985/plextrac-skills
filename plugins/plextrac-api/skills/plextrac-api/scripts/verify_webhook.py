#!/usr/bin/env python3
"""Verify a PlexTrac webhook signature (header X-Authorization-HMAC-256).

PlexTrac computes hex(HMAC-SHA256(secret, JSON.stringify(payload))). Verify against the raw request
body bytes when you have them (most faithful); otherwise re-serialise with compact separators.

Library:
    from verify_webhook import verify_signature
    ok = verify_signature(secret, raw_body_bytes, request.headers["X-Authorization-HMAC-256"])

CLI:
    python verify_webhook.py --secret "$WEBHOOK_SECRET" --signature <hex> --body payload.json
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import sys


def canonical_body(payload) -> bytes:
    """Match JavaScript JSON.stringify(payload): compact separators, keys in original order."""
    if isinstance(payload, (bytes, bytearray)):
        return bytes(payload)
    if isinstance(payload, str):
        payload = json.loads(payload)
    return json.dumps(payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8')


def compute_signature(secret: str, payload) -> str:
    return hmac.new(secret.encode('utf-8'), canonical_body(payload), hashlib.sha256).hexdigest()


def verify_signature(secret: str, payload, signature_header: str | None) -> bool:
    if not signature_header:
        return False
    expected = compute_signature(secret, payload)
    return hmac.compare_digest(expected.lower(), signature_header.strip().lower())


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--secret', required=True)
    p.add_argument('--signature', required=True, help='value of X-Authorization-HMAC-256')
    p.add_argument('--body', required=True, help='file with the raw request body (use - for stdin)')
    p.add_argument('--raw', action='store_true', help='hash the file bytes exactly as received instead of re-serialising JSON')
    a = p.parse_args(argv)
    data = sys.stdin.buffer.read() if a.body == '-' else open(a.body, 'rb').read()
    payload = data if a.raw else json.loads(data)
    ok = verify_signature(a.secret, payload, a.signature)
    print('VALID' if ok else 'INVALID')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
