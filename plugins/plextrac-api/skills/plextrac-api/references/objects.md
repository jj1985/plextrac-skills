# PlexTrac object structures

Containers: Clients hold Assets and Reports; Reports hold Findings; Findings hold Affected Assets (copies of client assets with extra relationship fields) and Evidence. Condensed from docs.plextrac.com "Object Structures" (full tables in `source-docs/api-documentation__object-structures__*.md`).

## Client (`doc_type: "client"`)
Required on create: `name`.

| Field | Type |
|---|---|
| client_id | int |
| cuid | string |
| name, description, poc, poc_email | string |
| tags | string[] |
| custom_field | `[{"label": str, "value": str}]` |
| users | `{ "<email>": {"classificationId": cuid|null, "role": "ADMIN"|"STD_USER"|"ANALYST"} }` |
| classificationId | cuid or null |
| tenant_id | int |

## Report (`doc_type: "report"`)

| Field | Type |
|---|---|
| report_id / id | int |
| client_id | int |
| name | string |
| status | "Draft" \| "Ready For Review" \| "In Review" \| "Approved" \| "Published" |
| includeEvidence | bool |
| reportType | "default" |
| tags | string[] |
| custom_field | `[{"label","value"}]` |
| exec_summary | `{"custom_fields": [{"id": cuid, "label", "tags": [], "text": html, "isFromNarrativesDB": null|true}]}` |
| template | report template UUID or null |
| fields_template | findings layout UUID or null |
| start_date, end_date | ISO 8601 or null |
| reviewers, operators | string[] (emails) |
| isTrackChanges | bool |
| created_at | epoch ms |

## Finding (`doc_type: "flaw"`)
Required on create: `title`, `severity`, `status`, `description`.

| Field | Type |
|---|---|
| flaw_id | int (unique within a report, not across the platform) |
| client_id, report_id | int |
| report_name | string |
| title, description, recommendations, references | string (HTML) |
| severity | "Critical" \| "High" \| "Medium" \| "Low" \| "Informational" |
| status | "Open" \| "In Process" \| "Closed" |
| subStatus, substatusCuid | string / cuid |
| visibility | "draft" \| "published" |
| assignedTo | email |
| tags | string[] |
| fields | `{"scores": {"cvss"|"cvss3"|"general": {"type","value","label","calculation"}}, "<custom_key>": {"label","value"}}` |
| risk_score | `{"CVSS3_1": {"overall": num, "subScore": {"base","temporal","environmental"}, "vector": str}, "CVSS4_0"?, "CVSS3_0"?, "CVSS2_0"?, "LikelihoodImpact"?}` |
| selectedScore, calculated_severity | string / bool |
| common_identifiers | `{"CVE": [{"name","year","id","link"}], "CWE": [{"name","id","link"}], "code_samples": [{"caption","code","id"}]}` |
| affected_assets | `{ "<assetId>": <AffectedAsset> }` |
| exhibits | `[{"assets": [{"asset","id"}], "caption", "exhibitID", "index", "type"}]` |
| evidence (per affected asset) | cuid[] |
| slaData | `{"title","timeToExpire"}` or `[]` |
| source | string (scanner) |
| createdAt, last_update, closedAt, reopenedAt | epoch ms |
| jiraIssueKey, jiraIssueLink, serviceNowTicketKey | string or null |
| doc_version | string (never send) |

## Asset (`doc_type: "client_asset"`)
Required on create: `asset` (name). Create with `PUT /api/v1/client/{clientId}/asset/0`.

| Field | Type |
|---|---|
| id / cuid | string (UUID or CUID) |
| asset | string (name) |
| type | "Server" \| "Workstation" \| "Network Device" \| "Application" \| "General" |
| assetCriticality | "Critical" \| "High" \| "Medium" \| "Low" \| "Information" |
| hostname, host_fqdn, host_rdns, dns_name, netbios_name, mac_address, physical_location, system_owner, data_owner, description | string |
| knownIps | string[] (validated IPs) |
| operating_system | string[] |
| ports | `{"<number>_<service>_<protocol>_<version>": {"number","service","protocol","version"}}` |
| tags | string[] |
| notes | string[] |
| pci_status | "pass" \| "fail" |
| parent_asset | `{"id","asset"}` or null |
| child_assets | `{ "<id>": <Asset> }` |
| fields | `{"<key>": {"cuid","key","label","value","sortOrder"}}` (custom fields) |
| findings | `{ "<flawId>": <Vulnerability instance> }` (auto-maintained) |
| total_cves | int |
| created / createdAt / updatedAt | ISO / epoch ms |

## Affected asset (inside `finding.affected_assets`)
A copy of the client asset (`asset`, `id`, `cuid`, `client_id`, ...) plus:

| Field | Type |
|---|---|
| status | "Open" \| "In Process" \| "Closed" |
| subStatus, substatusCuid | string / cuid |
| closedAt, reopenedAt | null or datestamp |
| evidence | cuid[] (Evidence objects) |
| locationUrl | string |
| vulnerableParameters | `[{"id": cuid, "text"}]` |
| notes | string (not the client-asset string[]) |
| ports | subset of the asset's ports, same shape |

Workflow: create the client asset first, then put an entry keyed by its id into `affected_assets` on the finding with all of the fields above present.

## Evidence
`{"id": uuid, "caption": str, "code": str}` attached to an affected asset; bulk upsert via `PUT /api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence`.

## Writeup (WriteupsDB, `doc_type: "template"`)
Same shape as a finding (`title`, `severity`, `description`, `recommendations`, `references`, `fields`, `tags`, `risk_score`, `calculated_severity`, `common_identifiers`) plus `repositoryId` (cuid), `doc_id` (int), `cuid`, `source`, `createdAt`, `createdBy`, `isDeleted`. Create with `POST /api/v1/template/create`.

## User
`{"cuid", "email", "name": {"first","last"}, "fullName", "roles": ["ADMIN"], "scope": [...], "authentication_provider": "plextrac"|..., "mfa": {"enabled","activatedAt"}, "disabled", "default_group", "dateFormat", "tenant_id", "createdAt", "lastLogin"}`.

## Webhook payload
`{"cuid","actorCuid","event","targetCuid" | "targetCuids": [],"targetType","text","clientId"?,"reportId"?,"findingId"?,"assessmentId"?}`.

## Import job (`/api/v2/my-imports`)
`{"key": operationId, "name", "reportName", "clientName", "fileSize", "status": "IN QUEUE"|"PROCESSING"|"IMPORT COMPLETE"|"ERROR", "progress", "errorStatus", "source"}`; entries expire after one hour.

## Time formats
Findings and assets use epoch milliseconds (`createdAt: 1662588579026`); reports and schedule events use ISO 8601 (`2024-08-16T15:24:19.000Z`).
