# PlexTrac API gotchas, deprecations and breaking changes

## Common failures

| Symptom | Cause | Fix |
|---|---|---|
| 401 after a few minutes of work | JWT expired (15 minutes) | `PUT /api/v1/token/refresh` before expiry, or re-authenticate; the bundled client refreshes automatically |
| Login errors after several attempts, even with correct credentials | 10 authentication requests per minute per instance, all users combined | Cache the token; never log in per request; back off 60 s |
| Login returns `code` instead of `token` | MFA user | Complete `POST /api/v1/authenticate/mfa` with the authenticator code, or use a Service Account for automation |
| Login blocked with an MFA setup prompt | Tenant has "Require MFA" and the user has none | Use a user designated as Service Account (exempt), or enrol MFA |
| 403 "Not authorized ..." with a valid token | RBAC: the role lacks the permission for that route (e.g. View Report Findings, mark as published) | Check `GET /api/v2/whoami` roles; ask an admin to adjust the role; permissions endpoint only works for your own user |
| Request body ignored / validation error on POST | Missing `Content-Type: application/json` so the JSON landed in form/data | Always send the header (requests' `json=` does it) |
| Get Finding / Get Report returns 404 for a draft | Only published items are returned unless the user has "Ability to mark a finding as published" | Grant the permission or list drafts via the v2 list route with `visibility` filter |
| Update Finding lost fields | PUT is a replace with selective parsing | GET the finding, modify, PUT the whole object; never send a partial body |
| Pagination returns an error | `limit` not in the endpoint's allowed set, or `offset` used as a page number | Use 5/10/25/50/100 (1000 where allowed); `offset` counts records |
| Report findings `limit: 99999` rejected | Removed in release 2.23 (Nov 2025) | Page with limit ≤ 100 |
| Word export shows no images / base64 images missing | Inline base64 images are unsupported | Upload with `POST /api/v1/uploads` and embed `<img src="/api/v1/uploads/<uuid>.ext">`; a `fileUrl` without an extension means the upload was read as bytes, not a file |
| Word export fails or is empty | Report has no Report Template and no `templateID` query param | Pass `templateID=<export template id>` from `GET /api/v2/tenant/{tenantId}/export-templates` |
| Export takes very long | `includeEvidence=true` | Set it to false unless evidence is required |
| Import queued "successfully" but nothing appears | Streaming import always queues; the file or `source` was wrong | Poll `GET /api/v2/my-imports` and read `status`/`errorStatus` (entries expire after 1 hour) |
| `importAsync` route returns 404 | Removed in 2.22 (Oct 2025) | Use presigned-url → PUT → `preuploaded-import/{source}` |
| `GET /api/v1/client/{clientId}/assets` 404 | Removed in 2.12 | `POST /api/v2/tenant/assets`, `POST /api/v2/clients/{clientId}/assets`, or `GET /api/v2/clients/{clientId}/reports/{reportId}/assets` |
| Custom role not accepted on user create | Role key format | Default roles `ADMIN`/`STD_USER`/`ANALYST`; custom `TENANT_<tenantId>_ROLE_<KEY>` |
| Role endpoints 404 with an old roleId | Default role IDs became fixed values in 1.58 | ADMIN `cljhc9ggj000008l99gkyai90`, STD_USER `cljhc9rvn000208l9g4lpai54`, ANALYST `cljhc9yh1000308l9ar7j8mux` |
| Webhook delivered twice | 5-second timeout then retries | Respond 2xx immediately, process asynchronously, dedupe on payload `cuid` |
| Webhook HMAC mismatch | Payload re-serialised differently from `JSON.stringify` | Hash the raw request body bytes, or `json.dumps(payload, separators=(',',':'))` |
| Webhook creation rejected | SSRF protection on URL/IP/protocol, or no valid event | Public HTTPS URL; at least one event from `GET /api/internal/webhookevents` |
| `flaw_id` collides across reports | By design: derived from the title | Always address findings with clientId + reportId + flaw_id |

## Sunset endpoints (removed; will 404)

| Route | Removed (release) | Replacement |
|---|---|---|
| `GET /api/v1/clients/analytics/export`, `GET /api/v1/flaws`, `GET /api/v1/client/{clientId}/topFlaws`, `POST /api/v1/clients/topFlaws`, `GET /api/v1/clients/findings` | Apr 2023 (1.51) | `POST /api/v2/clients/{clientId}/reports/{reportId}/findings`, `POST /api/v2/client/{clientId}/findings` |
| `GET /api/v1/clients/analytics/bootstrap` | May 2023 (1.53) | none (`POST /api/v2/findingAnalytics/bootstrap`) |
| `GET /api/v1/client/{clientId}/analytics[/flaws/{status}|/flaws/aging]`, `GET /api/v1/tenant/analytics[/findings/{status}]` | May 2023 (1.54) | `POST /api/v1/clients/analytics`, `GET /api/v2/tenant/analytics[/findings/{status}]` |
| `POST /api/v2/clients/analytics/assets/suggestion` | Sep 2023 (1.59) | none |
| `POST /api/v1/client/{clientId}/assets/import/{source}` | Nov 2023 (1.61) | `POST /api/v2/client/{clientId}/assets/import/{source}` |
| `GET /api/v2/clients/{clientId}/reports/{reportId}/flaws/{flawId}/affected_assets` | Jan 2024 (2.0) | `GET /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` |
| `POST /api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence` (Bulk Get Evidence) | Jan 2024 (2.1) | `GET .../flaw/{findingId}/asset/{assetId}/scanoutput` |
| `POST /api/v1/client/{clientId}/report/{reportId}/import/{source}` | Feb 2024 (2.2) | streaming upload flow |
| `GET /api/v1/client/{clientId}/assets` | Dec 2024 (2.12) | tenant / client / report asset list routes |
| `POST .../flaw/{findingId}/createAndLinkJiraTicket`, `POST /api/v2/client/{clientId}/report/{reportId}/findings/createJiraTickets` | Jan 2025 (2.14) | `POST /api/v2/jira/integration/{integrationId}/issues/create` |
| `POST /api/v2/client/{clientId}/report/{reportId}/importAsync/{source}` | Oct 2025 (2.22) | `POST /api/v2/presigned-url` + `POST .../preuploaded-import/{source}` |

Still listed in the collection but deprecated: `POST /api/v1/tenant/{tenantId}/user/create` (use `/create/bulk`), `POST /api/v2/repositories/copyFlawToWriteupsRepository` (use `POST /api/v1/template/create`), Jira "Legacy Integration" folder.

## Breaking changes

- 1.58 (Aug 2023): default RBAC role IDs fixed (above).
- 1.61 (Nov 2023): Get Finding no longer returns third-level data (other findings of each affected asset); use Get Asset / asset list routes.
- 2.23 (Nov 2025): `limit: 99999` removed from Get Findings by Report.

PlexTrac gives at least 90 days' notice on the API Change Log before removing a route: https://docs.plextrac.com/plextrac-documentation/api-documentation/api-change-policy/api-change-log
