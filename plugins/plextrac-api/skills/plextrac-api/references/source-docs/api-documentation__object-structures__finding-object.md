# Finding Object

Findings are the most common object in PlexTrac and contain data detailing an exploit.&#x20;

Findings also exist in client asset information in the form of an affected asset and contain the relationship information about which client assets are affected, which is tracked in the `affected_assets` field.

For each client asset, the finding affects, an object exists in that field's list containing information and metadata about the client asset and how it relates to the finding. Since the objects stored in `affected_assets` contain this extra relationship metadata, these items are considered separate objects called *affected asset objects.*

<div align="left"></div>

## Finding Table

The following table explains the fields and data types stored for a finding. Fields are presented in alphabetical order by object field name.

> **info:**
The required fields when creating a finding are `title`, `severity`, `status` and `description`.

<table><thead><tr><th width="186">object field name</th><th width="221">description</th><th>data type</th></tr></thead><tbody><tr><td>affected_assets</td><td>name of affected assets</td><td>dict {str, {AFFECTED ASSET Object}</td></tr><tr><td>assignedTo</td><td>email address of user that finding is assigned to</td><td>string</td></tr><tr><td>client_id</td><td>client that the finding belongs to</td><td>integer</td></tr><tr><td>closedAt</td><td>when finding was closed</td><td>integer of epoch milliseconds <code>1662588579026</code></td></tr><tr><td>common_identifiers</td><td>includes CVE scores, CWE scores, and code that is related to the finding (added in the <strong>Code Sample</strong> tab when editing a finding)</td><td>"CVE":  [{ "name": str, "year": int, "id": int, "link": str } ], "CWE": [ { "name": str, "id": int, "link": str } ] }, "code_samples": [ { "caption": str, "code": str, "id": str } ] }</td></tr><tr><td>createdAt</td><td>when finding was created in </td><td>integer of epoch milliseconds <code>1662588579026</code></td></tr><tr><td>description</td><td>description of finding</td><td>string</td></tr><tr><td>doc_type</td><td>field in database to identify object</td><td>string</td></tr><tr><td>doc_version</td><td>version of PlexTrac when finding was created. Should not be added to create or update requests</td><td>string</td></tr><tr><td>exhibits</td><td>an image or video related to the finding (added in the <strong>Screenshots/Video</strong> tab when editing a finding)</td><td>array: {"assets": [ { "asset": str, "id": str } ], "caption": str, "exhibitID": str:, "index": int, "type": str: MIME type image, such as .png}</td></tr><tr><td>fields</td><td>includes any added custom fields, plus legacy place for CVSS 3.0 score, CVSS 2.0 score, and 'general' score values entered for a finding </td><td>dict {str, dict {label: str, value: str}, "scores": { "cvss", { "type": "cvss", "value": str, "label": str, "calculation": str }, "cvss3", { "type": "cvss3", "value": str, "label": str, "calculation": str }, "general", { "type": "general", "value": str, "label": str, "calculation": str } } },</td></tr><tr><td>flaw_id</td><td>the unique identifier of a finding and is generated based on the finding title, but since a finding with the same title can exist in different reports, this means <code>flaw_id</code> is not unique across the platform</td><td>integer</td></tr><tr><td>last_update</td><td>when finding was last modified</td><td>integer of epoch milliseconds <code>1662588579026</code></td></tr><tr><td>repoenedAt</td><td>when finding was reopened </td><td>integer of epoch milliseconds <code>1662588579026</code></td></tr><tr><td>report_id</td><td>ID of report finding is associated with</td><td>integer</td></tr><tr><td>report_name</td><td>name of report</td><td>string</td></tr><tr><td>risk_score</td><td>object to hold different scoring data, CVSS v4.0, CVSS v3.1, CVSS v3.0, CVSS v2.0, and Likelihood x Impact scoring</td><td>see <a href="https://api-docs.plextrac.com/#2744f99d-bf3a-4174-93f6-a0f05e99fcdc">example response payload</a> for details</td></tr><tr><td>selectedScore</td><td>the identified selected score for the finding</td><td>string</td></tr><tr><td>severity</td><td>severity of finding</td><td>string in ["Critical", "High", "Medium", "Low", "Informational"]</td></tr><tr><td>slaData</td><td>SLA status of finding</td><td>{"title": str, "timeToExpire": str } </td></tr><tr><td>source</td><td>source of finding</td><td>string</td></tr><tr><td>status</td><td>status of finding</td><td>string in ["Open", "In Process", "Closed"]</td></tr><tr><td>subStatus</td><td>substatus of finding</td><td>string</td></tr><tr><td>substatusCuid</td><td>CUID of substatus</td><td>string | null | undefined</td></tr><tr><td>tags</td><td>any tags associated with finding</td><td>string array</td></tr><tr><td>title</td><td>title of finding</td><td>string</td></tr><tr><td>visibility</td><td>visibility of finding</td><td>string</td></tr></tbody></table>

## Finding Structure

The finding object stored in the database is a nested JSON object. Below are screenshots and a sample downloadable file that displays the structure of different database objects.

<div align="left"></div>

*continued*

<div align="left"></div>

(downloadable sample file on the source page)
