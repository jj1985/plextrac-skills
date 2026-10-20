# PlexTrac API quick reference

Base `https://<instance>`; header `Authorization: Bearer <JWT>`; JSON bodies need `Content-Type: application/json`.
Sources: official Postman collection (api-docs.plextrac.com) and docs.plextrac.com API section, captured 2026-10-20.

## Contents
1. Auth and sessions
2. Finding IDs
3. Pagination, sorting, filtering (v2 list bodies)
4. Clients and client users
5. Reports (CRUD, bulk, export, import)
6. Findings (CRUD, status, bulk, affected assets, evidence)
7. Scanner imports (streaming upload flow)
8. Assets
9. Content Library (WriteupsDB, NarrativesDB), templates
10. Users, roles, tags, SLAs, audit log
11. Assessments, Scheduler, Runbooks, Integrations
12. Webhooks

## 1. Auth and sessions

| Step | Request | Notes |
|---|---|---|
| Login (no MFA, or service account) | `POST /api/v1/authenticate` `{"username":"user@example.com","password":"..."}` | 200 → `{"status":"success","tenant_id":0,"token":"<JWT>","cookie":"<JWT>"}`. No auth header. |
| Login (MFA user) | same call returns `{"code":"..."}` → `POST /api/v1/authenticate/mfa` `{"code":"<from previous>","token":"<6-digit authenticator code>"}` | returns the same token envelope |
| Refresh | `PUT /api/v1/token/refresh` (no body, bearer header) | new 15-minute token; must be called while the old one is still valid |
| Who am I | `GET /api/v2/whoami` (also `GET /api/v1/user/whoami`) | `email`, `roles`, `mfa`, `authentication_provider`, `tenant_id` |
| Liveness | `GET /api/v1/` | `{"text":"Authenticate at /authenticate"}` |
| MFA setup for a user | `GET /api/v2/user/mfa/qr` → `POST /api/v2/user/mfa/qr/activate` | |

Limits: tokens expire after 15 minutes; 10 authentication requests per minute per instance (all users, success or fail). A 429/error on login means wait a minute. Service Accounts are exempt from the tenant "Require MFA" switch and are the right credential for scripts.

## 2. Finding IDs

| ID | Where |
|---|---|
| `tenantId` | `tenant_id` in the auth response (`0` on most instances) |
| `clientId` | `POST /api/v2/clients` → `data[].client_id`; or the number between `clients/` and `/reports` in the UI URL |
| `reportId` | `POST /api/v2/reports` → `data[].id`; `GET /api/v1/client/{clientId}/reports`; or the number at the end of the report URL |
| `findingId` (= `flaw_id`) | `POST /api/v2/clients/{clientId}/reports/{reportId}/findings` → `data[].flaw_id`; the "Finding ID" field in the UI |
| `assetId` | `POST /api/v2/clients/{clientId}/assets` → `data[].id` (CUID) |
| `repositoryId` (WriteupsDB/NarrativesDB CUID) | `POST /api/v2/repositories/getAllWriteupsRepositories`; end of the repository URL in Content Library |
| `roleId` | fixed for defaults (ADMIN `cljhc9ggj000008l99gkyai90`, STD_USER `cljhc9rvn000208l9g4lpai54`, ANALYST `cljhc9yh1000308l9ar7j8mux`); custom roles: `GET /api/v2/tenants/{tenantId}/security/role` or the URL under Account Admin > Security > Role Based Access |
| `substatusCuid` | `GET /api/v3/substatus` |
| template IDs (report, fields, export) | `GET /api/v1/tenant/{tenantId}/report-templates`, `GET /api/v1/field-templates`, `GET /api/v2/tenant/{tenantId}/export-templates` |

## 3. Pagination, sorting, filtering

v2 list endpoints take a POST body:

```json
{
  "pagination": {"offset": 0, "limit": 25},
  "sort": [{"by": "name", "order": "ASC"}],
  "filters": [{"by": "status", "value": "Draft"}, {"by": "tags", "value": ["prod"]}]
}
```

| Endpoint | Allowed `limit` | `sort.by` / `filters.by` |
|---|---|---|
| `POST /api/v2/clients` | 5, 25, 50, 100 | name, tags (array), clients |
| `POST /api/v2/reports` | 5, 10, 25, 50, 100, 1000 | sort: name, status · filters: name, reviewers[], operators[], clients[int], status[], cuids[] (one CUID = single report) |
| `POST /api/v2/clients/{clientId}/reports/{reportId}/findings` | 1, 10, 50, 100 (99999 removed in 2.23) | findingTags[], searchTerm, createdAt, updatedAt, reopenedAt, closedAt, assignedTo, flaw_id, client_id, severity, status, subStatus, visibility ... · sort: title, status, severity, ... |
| `POST /api/v2/client/{clientId}/findings` | (example uses 99999; prefer ≤100) | searchTerm, status, severity, reportId, subStatus, visibility (draft/published), tags[], commonIdentifiers[], assignedTo ... |
| `POST /api/v2/tenant/assets` | 5, 10, 25, 50, 100, 1000 | searchTerm, client_id, assetCriticality, tags, type, pci_status, system_owner, data_owner |
| `POST /api/v2/clients/{clientId}/assets` | 5, 10, 25, 50, 100 | asset, tags (`["none"]` = untagged) |
| `GET /api/v2/tenants/{tenantId}/users?offset=&limit=&sortBy=&order=&filter=` | query-string paging | |
| `GET /api/v2/auditlog?limit=&offset=` | query-string paging | event types: LoginSuccess, LoginFail, UserCreated, TenantRoleAssigned, ... |

Responses: `{"status":"success","data":[...],"meta":{"pagination":{"offset","limit","total"},"sort":[...],"filters":[...]}}`.
Loop: `offset += limit` while `offset < meta.pagination.total`.

## 4. Clients and client users

| Op | Request |
|---|---|
| List (summary) | `GET /api/v1/client/list` → `[{"id":"client_1254","doc_id":[1254],"data":[1254,"Name",null]}]`; paginated: `POST /api/v2/clients` |
| Get | `GET /api/v1/client/{clientId}` → full client object |
| Create | `POST /api/v1/client/create` `{"name":"Acme","tags":["t"],"description":"","poc":"","poc_email":"","custom_field":[{"label":"","value":""}]}` → `{"status":"success","client_id":598,"assign_message":{...}}` (only `name` required) |
| Update / delete | `PUT /api/v1/client/{clientId}` (full object) · `DELETE /api/v1/client/{clientId}` |
| Logo | `POST /api/v1/client/{clientId}/logo` (multipart) · `DELETE .../logo` |
| Client users | `GET /api/v2/tenants/{tenantId}/clients/{clientId}/users`; assign `POST /api/v2/tenant/{tenantId}/client/{clientId}/user/assign`; bulk `.../bulk/users/assign`; remove `POST /api/v1/tenant/{tenantId}/client/{clientId}/user/remove`; candidates `GET /api/v1/tenant/{tenantId}/client/{clientId}/users/available` |
| Findings across a client | `POST /api/v2/client/{clientId}/findings` (truncated finding objects) |

## 5. Reports

| Op | Request |
|---|---|
| List | `GET /api/v1/client/{clientId}/reports` · tenant-wide paginated `POST /api/v2/reports` |
| Get | `GET /api/v1/client/{clientId}/report/{reportId}` (published only unless the user can mark findings published) |
| Create | `POST /api/v1/client/{clientId}/report/create` `{"name":"Q3 Pentest","status":"Draft","includeEvidence":false,"tags":[],"custom_field":[],"template":"<reportTemplateId>","fields_template":"<findingsTemplateId>","start_date":"2026-05-17T19:00:11.146Z","end_date":"...","isTrackChanges":true}` → `{"message":"success","doc_id":"report_500006_client_4155","report_id":500006}`. Add other fields with Update afterwards. |
| Update | `PUT /api/v1/client/{clientId}/report/{reportId}` with the report object (`name`, `status`, `tags`, `custom_field`, `exec_summary.custom_fields[{id,label,text}]`, `template`, dates, `reviewers`, `operators`) → `{"status","message","data":<report>}`. Does not touch findings. |
| Delete / bulk | `DELETE /api/v1/client/{clientId}/report/{reportId}`; `POST /api/v2/reports/bulk/delete`, `/bulk/tags`, `/bulk/reviewers`, `/bulk/status` |
| Export Word | `GET /api/v1/client/{clientId}/report/{reportId}/export/doc?includeEvidence=false[&templateID=<exportTemplateId>]` → .docx bytes. `includeEvidence=true` is slow. `templateID` needed when the report has no Report Template set. |
| Export PDF / ptrac | `GET .../export/pdf` · `GET .../export/ptrac` (JSON `.ptrac`, re-importable) |
| Import ptrac | `POST /api/v1/client/{clientId}/report/import` multipart `file=<.ptrac>` |
| Search & replace | `POST /api/v1/search-replace/occurrences`, `POST /api/v1/search-replace` |
| Exhibit | `GET /api/v1/client/{clientId}/report/{reportId}/{exhibitId}` |

Report `status` values: Draft, Ready For Review, In Review, Approved, Published.

## 6. Findings

| Op | Request |
|---|---|
| List in report | `POST /api/v2/clients/{clientId}/reports/{reportId}/findings` (body §3) → `data[]` full-ish finding objects; legacy `GET /api/v1/client/{clientId}/report/{reportId}/flaws` |
| Get | `GET /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` → full finding (needs View Reports + View Report Findings; drafts need publish permission) |
| Create | `POST /api/v1/client/{clientId}/report/{reportId}/flaw/create` → `{"message":"success","doc_id":"flaw_<client>_<report>_<flaw>","flaw_id":1795388512}`. Required: `title`, `severity`, `status`, `description`. Typical body below. |
| Update | `PUT /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` with the finding object (GET first; it is a replace with selective parsing) |
| Delete / bulk delete | `DELETE .../flaw/{findingId}` · `POST .../flaws/delete` |
| Status history / update | `GET .../flaw/{findingId}/status` · `POST .../flaw/{findingId}/status/update` `{"assignedTo":"a@b.com","status":"Open","subStatus":"Ready","comment":"..."}` |
| Bulk tags / createdAt / visibility | `PUT /api/v2/clients/{clientId}/reports/{reportId}/findings` `{"findings":[<flawId>],"data":{"tags":["t"],"createdAt":1718776800000,"visibility":"published"}}` |
| Bulk status / assignee across reports | `PUT /api/v2/client/{clientId}/findings` `{"update":{},"statusUpdate":{"assignedTo":"","comment":"","status":"Open","substatusCuid":"..."},"data":{"<reportId>":[<flawId>,...]}}` |
| Affected assets | add via `affected_assets` on create/update (copy of a client asset + affected fields, keyed by asset id); import `POST /api/v2/clients/{clientId}/reports/{reportId}/flaws/{findingId}/affected-assets/import/{source}`; remove `DELETE /api/v1/.../flaw/{findingId}/asset/{assetId}`; status `POST .../asset/{assetId}/status/update`, bulk `POST /api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/status` |
| Evidence | `PUT /api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/{assetId}/evidence/{evidenceId}`; bulk upsert `PUT /api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence`; scanner output `GET .../asset/{assetId}/scanoutput` |
| Copy finding to WriteupsDB | GET the finding, add `"repositoryId":"<cuid>"`, `POST /api/v1/template/create` |

Create Finding body (trim to what you need):

```json
{
  "title": "SQL injection in /login",
  "severity": "Critical",
  "status": "Open",
  "substatusCuid": "<optional substatus cuid>",
  "assignedTo": "analyst@example.com",
  "description": "<p>HTML</p>",
  "recommendations": "<p>HTML</p>",
  "references": "<p>HTML</p>",
  "tags": ["web"],
  "fields": {
    "scores": {"cvss3": {"label": "cvss3.1", "value": "9.8", "calculation": "AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"}},
    "custom_key": {"label": "Custom Field", "value": "text"}
  },
  "risk_score": {"CVSS3_1": {"overall": 9.8, "subScore": {"base": 9.8, "temporal": 9.8, "environmental": 9.8}, "vector": "AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"}},
  "calculated_severity": true,
  "common_identifiers": {"CVE": [{"name": "CVE-2024-1234", "year": 2024, "id": 1234, "link": ""}], "CWE": [{"name": "CWE-89", "id": 89, "link": ""}]},
  "affected_assets": {},
  "exhibits": [],
  "code_samples": [],
  "visibility": "draft",
  "slaData": [],
  "closedAt": 0
}
```

Enums: `severity` Critical | High | Medium | Low | Informational; `status` Open | In Process | Closed; `visibility` draft | published.

## 7. Scanner imports (streaming upload, current)

The old `POST /api/v1/.../import/{source}` (removed 2.2) and `POST /api/v2/client/{clientId}/report/{reportId}/importAsync/{source}` (removed 2.22, Oct 2025) are gone. Use:

1. `POST /api/v2/presigned-url` `{"name":"scan.nessus"}` → `{"status":"success","key":"<cuid>/scan.nessus","url":"https://.../cloud/uploads/..."}`
2. `PUT <url>` with the raw file bytes, `Content-Type: application/octet-stream` (no bearer header; the URL is presigned)
3. `POST /api/v2/client/{clientId}/report/{reportId}/preuploaded-import/{source}` `{"key":"<key from step 1>","fileName":"scan.nessus","tags":"{\"assets\":[],\"findings\":[\"tag\"]}","useParserActions":"true"}` → `{"status":"success","operationId":"<uuid>","importJob":{...,"status":"IN QUEUE"}}`. Queues even if the file is bad.
4. `GET /api/v2/my-imports` → `[{"key":"<operationId>","name","reportName","clientName","fileSize","status":"PROCESSING|IMPORT COMPLETE|ERROR","progress","errorStatus","source"}]`. Entries expire after 1 hour.

`source` = parser name: burp, burphtml, horizon, nessus, nexpose, ptrac, veracode (list from the V2 docs; qualys, nmap and others exist in the UI parser list — `GET /api/v1/tenant/{tenantId}/actions` returns the tenant's parsers). Client-asset imports: `POST /api/v2/client/{clientId}/assets/import/{source}` multipart `file` with source `nmap-xml`, `nmap-csv` (legacy `nmap`, `csv`).
Parser Actions (auto-tag/ignore rules per parser): `/api/v1/tenant/{tenantId}/actions/{parserName}/...`.

## 8. Assets

| Op | Request |
|---|---|
| Tenant-wide list | `POST /api/v2/tenant/assets` (body §3; includes related findings) |
| Client list | `POST /api/v2/clients/{clientId}/assets` (counts of findings only) |
| Report assets | `GET /api/v2/clients/{clientId}/reports/{reportId}/assets` (with finding instances and child assets) |
| Get | `GET /api/v1/client/{clientId}/asset/{assetId}` |
| Create | `PUT /api/v1/client/{clientId}/asset/0` with the asset object (`asset` name required; `doc_type":"client_asset"`) → `{"message":"success","doc_id":"client_asset_<client>-<id>","id":"<uuid>"}` |
| Update / delete | `PUT /api/v1/client/{clientId}/asset/{assetId}` · `DELETE ...` · bulk `POST /api/v1/client/{clientId}/bulk/assets/delete` |

`GET /api/v1/client/{clientId}/assets` (unpaginated) was removed in 2.12.

## 9. Content Library and templates

| Area | Requests |
|---|---|
| WriteupsDB writeups | `GET /api/v1/template/list`, `GET /api/v1/template/{writeupId}`, `POST /api/v1/template/create` (body like a finding + `repositoryId`), `PUT /api/v1/template/{writeupId}`, `DELETE ...`; add to report `PUT /api/v1/copy/{writeupId}`, bulk `POST /api/v2/writeups/bulk/addToReport`; repo-scoped `POST /api/v2/repositories/{repositoryId}/getWriteups` `{"repositoryId":"..."}`, `/addWriteups`, `/removeWriteup`; bulk copy/move/tags/delete `POST /api/v2/writeups/bulk/*`; import `POST /api/v2/writeups/import/{source}` |
| WriteupsDB repositories | `POST /api/v2/repositories/getAllWriteupsRepositories`, `GET /api/v2/repositories/listUserCanEdit`, `POST /api/v2/repositories/add`, `/{repositoryId}/update`, `/delete`; users `GET/POST/PUT /api/v2/repositories/{repositoryId}/users` |
| NarrativesDB | `POST /api/v2/narratives/getAllNarrativesRepositories`, `createNarrativesRepository`, `GET /api/v2/narratives/{id}/getNarrativesRepository`, sections `POST /api/v2/narratives/sections/all`, `POST /api/v2/narratives/sections`, `PUT /api/v2/narratives/sections/{sectionId}`, `POST /api/v2/narratives/sections/copy` |
| Templates | report templates `GET/PUT/DELETE /api/v1/tenant/{tenantId}/report-template[s]`; findings layouts `GET /api/v1/field-templates`, `PUT /api/v1/tenant/{tenantId}/field-template`; export (Word/Jinja2) templates `GET /api/v2/tenant/{tenantId}/export-templates`, `POST /api/v1/tenant/{tenantId}/template/import` |
| Files | `POST /api/v1/uploads` multipart `file` (+`setScope`) → `{"fileUrl":"uploads/<uuid>.jpg"}`; embed as `<img src="/api/v1/uploads/<uuid>.jpg">`. Artifacts: `POST /api/v1/file-manager/upload`, `POST /api/v1/file-manager/artifacts`, `GET/DELETE /api/v1/file-manager/artifacts/{artifactId}` |

## 10. Users, roles, tags, SLAs, audit

| Area | Requests |
|---|---|
| Users | `GET /api/v2/tenants/{tenantId}/users?offset=0&limit=10&sortBy=firstName&order=ASC`; `GET /api/v1/tenant/{tenantId}/user/list`; create `POST /api/v1/tenant/{tenantId}/user/create/bulk` `[{"email","name":{"first","last"},"role":"ADMIN|STD_USER|ANALYST|TENANT_<tenantId>_ROLE_<KEY>","default_group":true}]` (single-user create is deprecated); `PUT /api/v1/user/update`; `DELETE /api/v2/user/delete`; enable/disable `POST /api/v1/tenant/{tenantId}/user/toggledisabled`; passwords `PUT /api/v1/user/changepass`, `POST /api/v1/user/forgotpass`, `PUT /api/v1/tenant/{tenantId}/user/resetpass`; MFA `PUT /api/v1/user/mfa/token[/disable]`, admin `PUT /api/v1/tenant/{tenantId}/user/mfa/disable` |
| RBAC | `GET /api/v2/tenants/{tenantId}/security/role[/available]`, `GET .../role/{roleId}`, `POST .../role`, `PUT .../role/{roleId}/info`, `PUT .../role/{roleId}/permissions`, `DELETE .../role/{roleId}`; members `GET .../role/{roleKey}/users`, `PUT .../role/{roleId}/users`, `DELETE .../role/{roleId}/users/{userId}` |
| Auth providers / SAML | `GET /api/v2/authenticate/providers`, `GET/POST /api/v2/tenants/{tenantId}/providers/plextrac`, `PUT /api/v2/authenticate/tenants/{tenantId}/users/{userId}/configuration`, `GET/POST /api/v2/tenants/{tenantId}/saml/plextrac` |
| Tags | `GET /api/v1/tenant/{tenantId}/tag?limit=&offset=`, `POST .../tag`, `DELETE .../tag/{tagId}`, `GET .../tag/search?text=`, `POST .../tag/find` |
| SLAs | `GET/POST /api/v2/sla/benchmarks`, `GET/PUT/DELETE /api/v2/sla/benchmarks/{id}`; analytics `POST /api/v2/sla/analytics/mean-time`, `/findings` |
| Substatus | `GET/POST /api/v3/substatus`, `PATCH/DELETE /api/v3/substatus/{cuid}` |
| Audit log | `GET /api/v2/auditlog?limit=&offset=` (login/user/role events only) |
| Tenant | `GET/PUT /api/v1/tenant/{tenantId}`, notification settings, logos, `PUT /api/v2/tenants/{tenantId}/settings` |
| Analytics | `POST /api/v1/clients/analytics[/findings[/aging]]`, `POST /api/v2/findingAnalytics/bootstrap`, `POST /api/v2/clients/analytics/assets[/overview]`, trends `POST /api/v2/clients/analytics/trends/*` |

## 11. Assessments, Scheduler, Runbooks, Integrations

- **Assessments**: questionnaires `GET /api/v1/tenant/{tenantId}/assessments`, `GET/POST/PUT /api/v2/assessments/questionnaires[/{id}]`, questions `/questions`, export/import; client assessments `GET /api/v2/tenants/{tenantId}/clients/{clientId}/assessments[/{assessmentId}[/questions|/answers|/reviewers]]`, `POST /api/v1/tenant/{tenantId}/client/{clientId}/assessment` (create; to reuse one across clients GET it, drop `tenant_id, client_id, assess_id, completed_at`, set `saveOnly:true`, give every answer a non-empty `note`), report from assessment `POST .../assessment/{assessmentId}/report`, copy `POST /api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/copy`.
- **Scheduler**: `POST /api/v2/engagement-schedule-events/search`, `GET /api/v2/engagement-schedule-events/{cuid}`, create `POST /api/v2/engagement-schedule-events` (`title, clientCuid, testWindow, testType, objective, scope, accessInfo, specialInstructions, start, end, status:"PENDING"`) then `POST .../{cuid}/approve` (report details, dates, operators), `PATCH .../{cuid}`; artifacts `/api/v2/engagement-schedule-artifacts`.
- **Runbooks v2**: GraphQL only (`POST /graphql`), see `graphql-operations.md`: RunbookRepository*, RunbookMethodology*, RunbookTactic*, RunbookTechnique*, RunbookProcedure*, RunbookTestPlan*, RunbookEngagement*, RunbookEngagementProcedure* (logs, operators, targeted assets, attachments). File upload for procedure attachments: `POST /api/v2/runbooks/engagement-procedures/{id}/attachments/upload`. Legacy export/import `GET /api/v1/export/runbook/{runbookId}`, `POST /api/v1/import/runbook`.
- **Integrations**: generic `GET/POST /api/v2/integrations/configurations[/{configId}]`; Jira (new framework) `POST /api/v2/jira/connect`, projects, issue-type mappings, `POST /api/v2/jira/integration/{integrationId}/issues/create` (create tickets from findings), unlink; Tenable.io `GET/POST/DELETE /api/v2/tenant/{tenantId}/integrations/{product}`, tags sync.

## 12. Webhooks

Configure in UI (Account Admin > Integrations & Webhooks) or via internal routes: `GET /api/internal/webhookevents`, `POST /api/internal/webhooks` `{"clientCuids":[],"name":"","url":"https://...","sslVerification":true,"events":["ReportPublished"],"enabled":true,"secret":"<optional>"}`, `GET /api/internal/webhooks?page[size]=25&page[current]=1`, `PATCH/DELETE /api/internal/webhooks/{webhookCuid}`, test `POST /api/internal/webhooks/test`, logs `GET /api/internal/webhookslog?tenantCuid=&webhookCuid=&limit=&offset=`.

Payload: `{cuid, actorCuid, event, targetCuid | targetCuids[], targetType, text, clientId?, reportId?, findingId?, assessmentId?}`. Events documented with examples: Report Published, Report Finding Published, Assessment Submission, Scheduler Engagement Submission, plus Workflow Automation events (report / report finding creation or edit). Delivery: POST, 5-second timeout, up to 5 retries with exponential backoff (handle duplicates idempotently by `cuid`). Signature: header `X-Authorization-HMAC-256` = hex HMAC-SHA256 of `JSON.stringify(payload)` (compact separators) with the webhook secret; verify with `scripts/verify_webhook.py`.
