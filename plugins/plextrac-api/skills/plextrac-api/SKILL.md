---
name: plextrac-api
description: >-
  Work with the PlexTrac penetration-testing and reporting platform through its REST API (/api/v1,
  /api/v2, /api/v3), GraphQL endpoint (Runbooks v2) and outbound webhooks. Use it whenever a task
  mentions PlexTrac, plextrac.com, pentest reports/findings/writeups/WriteupsDB/NarrativesDB, importing
  Nessus/Burp/Qualys/Nexpose scan results, exporting reports to Word/PDF/ptrac, client assets, affected
  assets, assessments/questionnaires, runbooks, RBAC roles, or automating, scripting, syncing or
  bulk-loading anything in a PlexTrac tenant, even if the user never says "API". Covers JWT auth
  (15-minute tokens, MFA, service accounts, refresh, 10 logins/minute limit), tenant/client/report/
  finding IDs, offset pagination with fixed limit sets, finding/asset/report object shapes, the
  presigned-URL streaming import flow, deprecated routes and their replacements, and HMAC webhook
  verification. Bundles an OpenAPI 3.1 spec (293 operations), a GraphQL operation catalog and a
  stdlib Python client.
---

# PlexTrac API

PlexTrac is self-consuming: everything the web UI does is an HTTP call to the same backend, so any
UI task can be scripted. The official reference is a public Postman collection
(https://api-docs.plextrac.com/, 363 requests) plus a short docs section
(https://docs.plextrac.com/plextrac-documentation/api-documentation). Both were captured on
2026-10-20 into this skill: the collection became `references/plextrac.openapi.yaml` and
`references/endpoint-catalog.md`; the docs pages are in `references/source-docs/` (see `INDEX.md`).

## Pick the entry point

| Task | Use | Where to look |
|---|---|---|
| Log in, keep a session alive | `POST /api/v1/authenticate` (+ `/mfa`), `PUT /api/v1/token/refresh` | `references/quickref.md` §Auth |
| Find IDs (tenant, client, report, finding, repository, role) | auth response, list endpoints, URL in the UI | `references/quickref.md` §IDs |
| Clients, reports, findings, assets CRUD | v1 object routes (`/api/v1/client/{id}/report/{id}/flaw/...`) | `references/quickref.md`, `references/objects.md` |
| List/search with filters and sorting | v2 POST list routes with `{pagination, sort, filters}` | `references/quickref.md` §Pagination |
| Import scanner output (Nessus, Burp, Qualys...) | presigned-url → PUT upload → `preuploaded-import/{source}` → `/api/v2/my-imports` | `references/quickref.md` §Imports |
| Export a report | `.../export/doc`, `/export/pdf`, `/export/ptrac` | `references/quickref.md` §Reports |
| Reusable content (WriteupsDB, NarrativesDB), templates | `/api/v1/template/*`, `/api/v2/repositories/*`, `/api/v2/narratives/*` | `references/endpoint-catalog.md` Content Library |
| Users, RBAC roles, tags, SLAs, audit log, integrations (Jira, Tenable) | Admin and Users folders | `references/endpoint-catalog.md` |
| Runbooks v2 (methodologies, procedures, engagements) | `POST /graphql` named operations | `references/graphql-operations.md` |
| React to events (report published, finding published, assessment submitted) | webhooks with HMAC-SHA256 header | `references/quickref.md` §Webhooks, `scripts/verify_webhook.py` |
| Exact request/response shape of any endpoint | OpenAPI spec (search by `operationId` or path) | `references/plextrac.openapi.yaml` |

## Core mechanics

**Base URL.** `https://<instance>` (SaaS `https://<tenant>.plextrac.com`, or an on-prem host). Every
route starts with `/api/v1`, `/api/v2`, `/api/v3` or `/graphql`. `GET /api/v1/` returns
`{"text":"Authenticate at /authenticate"}` and is a cheap liveness check.

**Auth.** `POST /api/v1/authenticate` with `{"username","password"}` returns `{status, tenant_id,
token, cookie}`. Send `Authorization: Bearer <token>` on every other call. Tokens live **15 minutes**;
call `PUT /api/v1/token/refresh` (no body, same header) before expiry or log in again. Users with MFA
get a `code` back and must `POST /api/v1/authenticate/mfa` with `{"code", "token": "<6-digit>"}`.
Only **10 authentication requests per minute** per instance, counted across all users, so cache the
token and refresh instead of re-logging in per request. For automation use a user flagged as a
**Service Account** (exempt from tenant-wide MFA enforcement) and store its credentials in env vars
(`PLEXTRAC_URL`, `PLEXTRAC_USERNAME`, `PLEXTRAC_PASSWORD`), never in code or output.

**Permissions.** The token carries the user's RBAC permissions; a 403 means the role lacks the
permission, not that the token is bad. `GET /api/v2/whoami` shows roles; `GET
/api/v2/tenants/{tenantId}/user/{userId}/permissions` only works for your own user.

**IDs.** `tenant_id` comes from the auth response (usually `0` on single-tenant instances).
`clientId`, `reportId` are integers; `findingId` is the integer `flaw_id` (not unique across reports);
most newer objects (assets, writeups, repositories, substatuses, schedule events, webhooks) are
addressed by `cuid` strings. Default role IDs are fixed: ADMIN `cljhc9ggj000008l99gkyai90`, STD_USER
`cljhc9rvn000208l9g4lpai54`, ANALYST `cljhc9yh1000308l9ar7j8mux`.

**Pagination.** v2 list endpoints are `POST` with a JSON body `{"pagination":{"offset":0,"limit":25},
"sort":[{"by":"name","order":"ASC"}],"filters":[{"by":"tags","value":["x"]}]}`. `limit` must be one
of a fixed set that differs per endpoint (commonly `5,10,25,50,100`; tenant assets and report list
allow `1000`; report findings allow `1,10,50,100`). `offset` is a record offset, not a page number.
`limit: 99999` on report findings was removed in release 2.23. Loop until `meta.pagination.total`
is reached or a page comes back short.

**Response envelope.** Most v2 routes return `{"status":"success","data":[...],"meta":{...}}`; v1
routes return the raw object or `{"message":"success","doc_id":...}`. Errors are HTTP 4xx with a
JSON message. There is no silent-failure envelope like some platforms have, but **Update Finding is a
replace**: GET the finding, modify, PUT the whole object.

**JSON bodies need `Content-Type: application/json`**; without it the payload lands in the wrong
request field and the call fails.

**Rich text.** Description, recommendations, references and narrative fields are HTML (CKEditor).
Images must be uploaded first (`POST /api/v1/uploads` multipart) and referenced as
`<img src="/api/v1/uploads/<uuid>.png">`; base64 inline images break Word export.

## Workflow for a typical task

1. **Confirm scope**: instance URL, credential type (service account vs MFA user), which client and
   report. Read env vars; never echo secrets.
2. **Authenticate once** and keep the token in memory; refresh every ~12 minutes on long runs
   (`scripts/plextrac_api.py` does this automatically).
3. **Resolve IDs** with list calls (`POST /api/v2/clients`, `POST /api/v2/reports`,
   `POST /api/v2/clients/{clientId}/reports/{reportId}/findings`) rather than hard-coding.
4. **Read before write**: GET the object, change fields, send it back. Create endpoints accept the
   minimal required fields (client: `name`; finding: `title, severity, status, description`;
   asset: `asset`); extra fields are set with a follow-up PUT.
5. **Batch where the API offers it**: bulk finding updates, bulk tag/status/delete routes, bulk user
   creation, bulk writeup copy/move. Otherwise loop with a small delay; the auth limit is the only
   documented rate limit.
6. **Verify** by re-reading (`GET .../flaw/{findingId}`, `GET /api/v2/my-imports` for imports).
7. **Check the change log** before relying on a route: `references/gotchas.md` lists sunset and
   deprecated endpoints with replacements.

## Scripts

- `scripts/plextrac_api.py` - stdlib-only client + CLI: login (password, MFA, auto-refresh), generic
  request, paginated list helper, clients/reports/findings/assets helpers, create/update finding,
  report export, streaming scanner import with status polling, whoami. `python scripts/plextrac_api.py --help`.
- `scripts/verify_webhook.py` - HMAC-SHA256 verification of a PlexTrac webhook payload
  (`X-Authorization-HMAC-256`), usable as a library or CLI.

Both verify TLS; use `--ca-bundle` for self-signed on-prem certificates.

## References

- `references/quickref.md` - auth, IDs, pagination, the main CRUD and import/export flows with bodies.
- `references/objects.md` - client, report, finding, asset, affected asset, evidence, writeup shapes and enums.
- `references/endpoint-catalog.md` - all 363 documented requests by folder with paths and operation IDs.
- `references/graphql-operations.md` - the 62 GraphQL operations (Runbooks v2 and others) with query text.
- `references/gotchas.md` - deprecations, breaking changes, and common failure causes.
- `references/plextrac.openapi.yaml` - OpenAPI 3.1 generated from the Postman collection (schemas inferred from examples).
- `references/source-docs/` - the 17 docs pages as Markdown plus the raw Postman collection JSON.

## Conventions when answering

- Show `METHOD /path` with a JSON body; mention the bearer header once.
- Prefer v2 list routes and the streaming import flow; call out when a route is deprecated and name the replacement.
- Use placeholders `{clientId}`, `{reportId}`, `{findingId}` and say how to find them when the user has not given them.
- For one-off questions, answer from `quickref.md` or the spec directly instead of walking the whole workflow.
