# API Change Log

The page shows which endpoints will be impacted, providing ample time and warning for affected users to transition to an alternative solution. Users may need to update their code, adjust settings, or search for a different endpoint. Staying up-to-date with API changes is essential to ensure the proper functioning of applications.

* **Deprecation** refers to the process of phasing out or discontinuing an API. PlexTrac will no longer support it, even though it may still be operational.
* **Sunsetting** means that the API will be removed and not function.
* **Breaking Changes** are modifications that render current solutions ineffective, causing existing code or integrations to fail or produce incorrect results, even if the endpoint itself is not changing.

## Deprecations

The following table serves as a quick reference guide to all the changes made, offering a concise summary for easy navigation. Each entry is designed to provide a snapshot of the modifications, enabling users to grasp the key points quickly.&#x20;

After the table, expandable sections divided by release are included for those seeking more in-depth information. By clicking on these sections, users can access detailed explanations, context, and additional insights related to each change.

> **info:**
APIs below will be removed from the codebase on the posted **Sunset Date**.&#x20;

<table data-full-width="true"><thead><tr><th width="146">API</th><th width="397">Route</th><th width="181">Deprecation Date</th><th>Sunset Date - Release</th></tr></thead><tbody><tr><td></td><td><code>GET /api/v1/clients/analytics/export</code></td><td></td><td>April 6, 2023 - 1.51</td></tr><tr><td></td><td><code>GET /api/v1/flaws</code></td><td></td><td>April 6, 2023 - 1.51</td></tr><tr><td>Get Client Flaws</td><td><code>GET /api/v1/client/{clientID}/topFlaws</code></td><td></td><td>April 6, 2023 - 1.51</td></tr><tr><td>Get Multiple Client Flaws</td><td><code>POST /api/v1/clients/topFlaws</code></td><td></td><td>April 6, 2023 - 1.51</td></tr><tr><td></td><td><code>GET /api/v1/clients/findings</code></td><td></td><td>April 6, 2023 - 1.51</td></tr><tr><td>Get Analytics Bootstrap Findings</td><td><code>GET /api/v1/clients/analytics/bootstrap</code></td><td></td><td>May 8, 2023 - 1.53</td></tr><tr><td></td><td><code>GET /api/v1/client/{clientID}/analytics/flaws/aging</code></td><td>February 24, 2023</td><td>May 30, 2023 - 1.54</td></tr><tr><td></td><td><code>GET /api/v1/client/{clientID}/analytics/flaws/{status}</code></td><td>February 24, 2023</td><td>May 30, 2023 - 1.54</td></tr><tr><td></td><td><code>GET /api/v1/tenant/analytics</code></td><td>February 24, 2023</td><td>May 30, 2023 - 1.54</td></tr><tr><td></td><td><code>GET /api/v1/tenant/analytics/findings/{status}</code></td><td>February 24, 2023</td><td>May 30, 2023 - 1.54</td></tr><tr><td></td><td><code>GET /api/v1/client/{clientID}/analytics</code></td><td>February 24, 2023</td><td>May 30, 2023 - 1.54</td></tr><tr><td>Retrieve Analytics Assets - Suggestion</td><td><code>POST /api/v2/clients/analytics/assets/suggestion</code></td><td>June 7, 2023</td><td>September 13, 2023 - 1.59</td></tr><tr><td>Import Client Assets v1</td><td><code>POST /api/v1/client/{clientId}/assets/import/{{source}}</code></td><td>August 15, 2022</td><td>November 7, 2023 - 1.61</td></tr><tr><td>Get Affected Assets by Finding</td><td><code>GET/api/v2/clients/{clientId}/reports/{reportId}/flaws/{flawId}/affected_assets</code></td><td>October 18, 2023</td><td>January 2, 2024 - 2.0</td></tr><tr><td>Add Findings from File Imports</td><td><code>POST /api/v1/client/{clientId}/report/{reportId}/import/{source}</code></td><td>October 31, 2023</td><td>February 21, 2024 - 2.2</td></tr><tr><td>Bulk Get Evidence</td><td><code>POST /api/v2/tenant/{{tenantId}}/client/{{clientId}}/report/{{reportId}}/finding/{{findingId}}/asset/evidence</code></td><td>November 27, 2023</td><td>January 30, 2024 - 2.1</td></tr><tr><td>List Client Assets</td><td> <code>GET /api/v1/client/{clientID}/assets</code></td><td>September 13, 2024</td><td>December 3, 2024 - 2.12</td></tr><tr><td>Create Jira Ticket from Finding </td><td><code>POST /api/v1/client/{clientID}/report/{reportID}/flaw/{flawID}/createAndLinkJiraTicket</code></td><td>October 28, 2024</td><td>January 28, 2025 - 2.14</td></tr><tr><td></td><td><code>POST /api/v2/client/{clientId}/report/{reportId}/findings/createJiraTickets</code></td><td>October 28, 2024</td><td>January 28, 2025 - 2.14</td></tr><tr><td>Add Findings from File Imports V2</td><td><code>POST /api/v2/client/{clientId}/report/{reportId}/importAsync/{source}</code></td><td>June 23, 2025</td><td>October 8, 2025 - 2.22</td></tr></tbody></table>

### Additional Information By Release

<details>

<summary>Release 1.53 - May 8, 2023</summary>

**Deprecated endpoint name**: Get Analytics Bootstrap Findings - `GET /api/v1/clients/analytics/bootstrap`

**Context**: Deprecating legacy bootstrap implementation of analytics.

**Replacement**: none

</details>

<details>

<summary>Release 1.51 - April 6, 2023</summary>

**Deprecated endpoint name**: `GET /api/v1/clients/analytics/export`

**Context**: The legacy endpoint had poor performance and was no longer used by the PlexTrac frontend.

**Replacement**: none

**-----**

**Deprecated endpoint name**: `GET /api/v1/flaws`

**Context**: This endpoint was returning an empty array with no data.

**Replacement**:

These replacements provide similar functionality but don't retrieve all findings across an instance.

* [Get Findings by Report](https://api-docs.plextrac.com/#88b61efa-7f17-42ba-b383-81dad70ff7b7) - `POST /api/v2/clients/{clientId}/reports/{reportId}/findings`
* [List Client Findings](https://api-docs.plextrac.com/#4414885e-98fc-4a93-b582-a72decb6a672) - `POST /api/v2/client/{clientId}/findings`

**-----**

**Deprecated endpoint name**: Get Client Flaws - `GET /api/v1/client/{clientID}/topFlaws`

**Context**: Deprecated in favor of v2 endpoint with similar functionality and better data fetching performance.

**Replacement**:

* [List Client Findings](https://api-docs.plextrac.com/#4414885e-98fc-4a93-b582-a72decb6a672) - `POST /api/v2/client/{clientId}/findings`

**-----**

**Deprecated endpoint name**: Get Multiple Client Flaws - `POST /api/v1/clients/topFlaws`

**Context**: Deprecated in favor of v2 endpoint with similar functionality and better data fetching performance.

**Replacement**:

* [List Client Findings](https://api-docs.plextrac.com/#4414885e-98fc-4a93-b582-a72decb6a672) - `POST /api/v2/client/{clientId}/findings`

**-----**

**Deprecated endpoint name**: `GET /api/v1/clients/findings`

**Context**: The v1 endpoint returned finding information for all clients across the tenant. This resulted in poor performance and was deprecated in favor of data segmentation by client to improve performance.

**Replacement**:

The replacement provides similar functionality but doesn't retrieve all findings across an instance.

* [List Client Findings](https://api-docs.plextrac.com/#4414885e-98fc-4a93-b582-a72decb6a672) - `POST /api/v2/client/{clientId}/findings`

</details>

<details>

<summary>Release 1.54 - May 30, 2023</summary>

**Deprecated endpoint name**: `GET /api/v1/client/{clientID}/analytics`

**Context**: Removing functionality to get data for a single client in favor of the more performant way of getting all data simultaneously.

**Replacement**:

* `POST /api/v1/clients/analytics`

\-----

**Deprecated endpoint name**: `GET /api/v1/tenant/analytics/findings/{status}`

**Context**: Deprecating legacy implementation of analytics.

**Replacement**:

* `GET /api/v2/tenant/analytics/findings/{status}`

\-----

**Deprecated endpoint name**: `GET /api/v1/tenant/analytics`

**Context**: Deprecating legacy implementation of analytics.

**Replacement**:

* `GET /api/v2/tenant/analytics`

\-----

**Deprecated endpoint name**: `GET /api/v1/client/{clientID}/analytics/flaws/{status}`

**Context**: Deprecating legacy implementation of analytics.

**Replacement**:

* `GET /api/v2/tenant/analytics/findings/{status}`

\-----

**Deprecated endpoint name**: `GET /api/v1/client/{clientID}/analytics/flaws/aging`

**Context**: Deprecating legacy implementation of analytics.

**Replacement**: none

</details>

<details>

<summary>Release 1.59 - September 13, 2023</summary>

**Deprecated endpoint name**: Retrieve Analytics Assets - Suggestion - `POST /api/v2/clients/analytics/assets/suggestion`

**Context**: Deprecating legacy implementation of analytics.

**Replacement**: none

</details>

<details>

<summary>Release 1.61 - November 7, 2023</summary>

**Deprecated endpoint name**: Import Client Assets v1 - `POST /api/v1/client/{clientId}/assets/import/{source}`

**Context**: This endpoint has been marked as deprecated in our Postman docs since adding the v2 endpoint with the same functionality, but was not planned for immediate removal.

**Replacement**: [Import Client Assets v2](https://api-docs.plextrac.com/#572a3a48-f168-4089-9049-e60b559e48a4) - `POST /api/v2/client/{clientId}/assets/import/{source}`

</details>

<details>

<summary>Release 2.0 - January 2, 2023</summary>

**Deprecated endpoint name**: Get Affected Assets by Finding - `GET/api/v2/clients/{clientId}/reports/{reportId}/flaws/{flawId}/affected_assets`

**Context**: This endpoint returns a subset of the finding information regarding the affected assets. In order to minimize the number of endpoints we have to maintained, this is being deprecated in favor of using the endpoint that retrieves the entire finding, including the affected asset information from this endpoint.

**Replacement**: [Get Finding](https://api-docs.plextrac.com/#2744f99d-bf3a-4174-93f6-a0f05e99fcdc) - `GET /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}`

</details>

<details>

<summary>Release 2.1 - January 30, 2023</summary>

**Deprecated endpoint name:** [Bulk Get Evidence](https://api-docs.plextrac.com/#03c34b76-276a-4b57-8a7d-cbaf457809dd) - `POST /api/v2/tenant/{{tenantId}}/client/{{clientId}}/report/{{reportId}}/finding/{{findingId}}/asset/evidence`

**Context:** A bug in evidence handling was identified where the same evidence could be linked to multiple affected assets, leading to unintended modifications. As a result, the endpoint will be deprecated due to changes in the response, which now includes duplicate data for certain evidence objects. Acknowledging this modification and adjusting implementations accordingly before the endpoint is sunset is crucial.

**Overview of Changes**

**Important:** The response will change and contain seemingly duplicate evidence entries in version 1.62. The endpoint will be removed in version 1.63.

**Replacement:** [Get Scanner Output](https://api-docs.plextrac.com/#8a37ee7a-e9c9-4572-8afc-59da77733320) - `GET /api/v1/client/{{clientId}}/report/{{reportId}}/flaw/{{findingId}}/asset/{{assetId}}/scanoutput`

</details>

<details>

<summary>Release 2.2 - February 21, 2024</summary>

**Deprecated endpoint name**: [Add Findings from File Imports V1](https://api-docs.plextrac.com/#b9a3f933-f19b-4d49-9e3d-89dcb722c7ad) - `POST /api/v1/client/{clientId}/report/{reportId}/import/{source}`

**Context**: This endpoint has a V2 that was created to fix performance issues. The V2 endpoint does not leave the HTTP request open throughout the entire import process, removing the possibility that the request could fail due to timeout errors on larger imports.

[**Overview of Changes**](https://docs.plextrac.com/plextrac-endpoint-change/)

The V1 endpoint will be removed in favor of the V2 endpoint. **Please read the differences between endpoints!** Updating to the V2 endpoint is not as simple as replacing the route.

[V1 Description](https://api-docs.plextrac.com/#b9a3f933-f19b-4d49-9e3d-89dcb722c7ad) vs [V2 Description](https://api-docs.plextrac.com/#941bdcaa-5561-4e31-83cd-02e44d141613)

**Replacement**: [Add Findings from File Imports V2](https://api-docs.plextrac.com/#941bdcaa-5561-4e31-83cd-02e44d141613) - `POST /api/v2/client/{clientId}/report/{reportId}/importAsync/{source}`

</details>

<details>

<summary>Release 2.12 - December 3, 2024</summary>

**Deprecated endpoint name:** [List Client Assets](https://api-docs.plextrac.com/#3901a546-f94e-43ec-90df-8bffc68494dc) - `GET /api/v1/client/{clientID}/assets`

**Context**: This endpoint is being removed as it returns an unpaginated list of assets that can be very large and result in database errors.

**Replacements:** Depending on the need, the following could be used to retrieve assets:

* [Get Tenant Assets](https://api-docs.plextrac.com/#47b8f7ee-84f6-48c6-81e9-f3eeae4edb70) (all assets)\ <mark style="color:green;">+ full related finding information</mark>

  <mark style="color:red;">- no child asset information</mark>
* [Get Assets by Client](https://api-docs.plextrac.com/#cdea281d-03ce-409d-a434-bbec23cdb817) (client-specific assets)\ <mark style="color:red;">- only has a count of related findings with no finding information</mark>\ <mark style="color:red;">- no child assets information</mark>
* [List Report Assets](https://api-docs.plextrac.com/#2c9acc54-4481-443e-9246-8ed0b452f697) (report-specific assets)\ <mark style="color:green;">+ full related finding information and count of related findings</mark>\ <mark style="color:green;">+ includes child asset information</mark>

</details>

<details>

<summary>Release 2.14 - January 28, 2025</summary>

**Deprecated endpoint name:** [Create and Link Jira Ticket to Finding](https://api-docs.plextrac.com/#9e0b9007-19fd-4064-bafc-d0f362f4358b) - `POST /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/createAndLinkJiraTicket`

**Context:** The Jira integration has been updated to follow a new integration framework pattern. This includes a new set of API endpoints that will follow the pattern for all future integrations.

**Replacements:** [Create Jira Ticket from Findings](https://api-docs.plextrac.com/#90ff6d8c-b803-43d0-992f-244d0389e65f)

***

**Deprecated endpoint name:** [Bulk Create and Link Jira Tickets to Findings](https://api-docs.plextrac.com/#2c389f6c-b476-413b-8f4a-478981f4d4ab) - `POST /api/v2/client/{clientId}/report/{reportId}/findings/createJiraTickets`

**Context:** The Jira integration has been updated to follow a new integration framework pattern. This includes a new set of API endpoints that will follow the pattern for all future integrations.

**Replacements:** [Create Jira Ticket from Findings](https://api-docs.plextrac.com/#90ff6d8c-b803-43d0-992f-244d0389e65f)

</details>

<details>

<summary>Release 2.22 - October 8, 2025</summary>

**Deprecated endpoint name**: [Add Findings from File Imports V2](https://api-docs.plextrac.com/#941bdcaa-5561-4e31-83cd-02e44d141613) - `POST /api/v2/client/{clientId}/report/{reportId}/importAsync/{source}`

**Context**: This endpoint is being replaced with a new, multi-step asynchronous import process that separates file upload from import execution. The new architecture improves reliability, system responsiveness, and scalability during heavy platform usage.

[**Overview of Changes**](/plextrac-documentation/api-documentation/api-change-policy/2025-june-file-import-route-deprecation.md)

The original **importAsync V2 endpoint** will be removed in favor of the **Streaming Upload workflow**. **Please read the differences!** Updating to the new workflow is not as simple as replacing the route.

[V2 Description](https://api-docs.plextrac.com/#941bdcaa-5561-4e31-83cd-02e44d141613) vs [Streaming Upload Description](https://api-docs.plextrac.com/#e0eff080-a18b-4049-9df3-7218a13465a7)

**Replacement**:

[Request Presigned URL](https://api-docs.plextrac.com/#1846a031-70ba-44a4-b478-19c9632a4d81)

`POST /api/v2/presigned-url`&#x20;

[Add Findings Async from Preuploaded File Imports](https://api-docs.plextrac.com/#df786b71-5740-49e5-87b4-413f29f5a960)

`POST /api/v2/client/{clientId}/report/{reportId}/preuploaded-import/{source}`

</details>

## Breaking Changes

This section includes modifications in an API update incompatible with the previous version, potentially causing existing code or integrations to fail. Breaking changes can involve the removal of functionality, modification of behavior, changes in response structure or input requirements, and altering data types or values.

The following table serves as a quick reference guide to all the changes made, offering a concise summary for easy navigation. Each entry is designed to provide a snapshot of the modifications, enabling users to grasp the key points quickly.&#x20;

After the table, expandable sections divided by release are included for those seeking more in-depth information. By clicking on these sections, users can access detailed explanations, context, and additional insights related to each change.

<table data-full-width="true"><thead><tr><th>API</th><th width="337">Route</th><th width="211">Change</th><th>Change Date - Release</th></tr></thead><tbody><tr><td>Get Security Role</td><td><code>GET /api/v2/tenants/{tenantId}/security/role/{roleId}</code></td><td>Update RBAC ID Values</td><td>August 21, 2023 - 1.58</td></tr><tr><td>Update Security Role Info</td><td><code>PUT /api/v2/tenants/{tenantId}/security/role/{roleId}/info</code></td><td>Update RBAC ID Values</td><td>August 21, 2023 - 1.58</td></tr><tr><td>Update Security Role Permission</td><td><code>PUT /api/v2/tenants/{tenantId}/security/role/{roleId}/permissions</code></td><td>Update RBAC ID Values</td><td>August 21, 2023 - 1.58</td></tr><tr><td>Add Role User</td><td><code>PUT /api/v2/tenants/{tenantId}/security/role/{roleId}/users</code></td><td>Update RBAC ID Values</td><td>August 21, 2023 - 1.58</td></tr><tr><td>Remove Role User</td><td><code>DELETE /api/v2/tenants/{tenantId}/security/role/{roleId}/users/{userId}</code></td><td>Update RBAC ID Values</td><td>August 21, 2023 - 1.58</td></tr><tr><td>Delete Security Role</td><td><code>DELETE /api/v2/tenants/{tenantId}/security/role/{roleId}</code></td><td>Update RBAC ID Values</td><td>August 21, 2023 - 1.58</td></tr><tr><td>Get Finding</td><td><code>GET /api/v1/client/{{clientId}}/report/{{reportId}}/flaw/{{findingId}}</code></td><td>Decouple Finding/Assets</td><td>November 7, 2023 - 1.61</td></tr><tr><td>Get Findings by Report</td><td><code>/api/v2/clients/{{clientId}}/reports/{{reportId}}/findings</code></td><td>Remove Pagination Option</td><td>November 6, 2025 - 2.23</td></tr></tbody></table>

### Additional Information By Release

<details>

<summary>Decouple Finding/Assets - November 7, 2023</summary>

**Summary**: This change has been carefully designed to enhance your experience by speeding up the delivery of a more concise data set. We are proactively contacting you to ensure that there will be no data disruption on your account.

**Details**:

*Get Finding API Functionality*: The Get Finding endpoint returns the finding information about the finding and related affected assets. The standard use case for this endpoint is to gather data relevant to the finding of the `findingId` specified in the request. Currently, the returned affected asset information also references relational data to other findings not specified in the request.

*What's changing*: This update modifies the data that will be returned using the Get Finding endpoint. We have increased performance and security by maintaining the findings and related assets and excluding the third level of data (data for every other finding related to each affected asset in the requested finding) in the returned data set. If you were using the Get Finding endpoint to access these findings related to an asset, please see the recommended routes below.

*Routes for Accessing Findings Related to an Asset*: We understand that you might have specific requirements for other data needed. To address this, we have existing designated routes to get you access to findings related to an asset. The [Get Asset](https://api-docs.plextrac.com/#25f3e32d-07a5-4f16-939d-d5b792ee92d7) route will retrieve a single record, or for multiple records in a single request, use the [List Client Assets](https://api-docs.plextrac.com/#3901a546-f94e-43ec-90df-8bffc68494dc) route.

**Impacted Endpoints**:

* [Get Finding](https://api-docs.plextrac.com/#2744f99d-bf3a-4174-93f6-a0f05e99fcdc) - `GET /api/v1/client/{{clientId}}/report/{{reportId}}/flaw/{{findingId}}`

</details>

<details>

<summary>Update RBAC ID Values - August 21, 2023</summary>

**Summary**: Replaces the randomly generated `roleID` with set values.

**Details**: Currently, the admin, standard, and analyst `roleID` are randomly generated when the tenancy is created. In the future, this will be a standard set value. Users must locate all occurrences of this variable and update the endpoint.&#x20;

For example, with the admin role, change `/api/v2/tenants/0/security/role/cl75q1auk00040yoff389h206` (random `roleID` value) to `/api/v2/tenants/0/security/role/cljhc9ggj000008l99gkyai90` (the new standard value).

Release 1.58 will implement this modification, supporting the legacy and the new solution. Release 1.59 will no longer provide support for the legacy method.

The new set ID values for each default RBAC role are listed below.

* ADMIN: cljhc9ggj000008l99gkyai90
* STD\_USER: cljhc9rvn000208l9g4lpai54
* ANALYST: cljhc9yh1000308l9ar7j8mux

**Impacted Endpoints**:

* <mark style="color:green;">`GET`</mark>` ``/api/v2/tenants/{tenantId}/security/role/{roleId}`
* <mark style="color:blue;">`PUT`</mark>` ``/api/v2/tenants/{tenantId}/security/role/{roleId}/info`
* <mark style="color:blue;">`PUT`</mark>` ``/api/v2/tenants/{tenantId}/security/role/{roleId}/permissions`
* [<mark style="color:blue;">`PUT`</mark>](#user-content-fn-1)[^1] `/api/v2/tenants/{tenantId}/security/role/{roleId}/users`
* <mark style="color:red;">`DELETE`</mark>` ``/api/v2/tenants/{tenantId}/security/role/{roleId}/users/{userId}`
* <mark style="color:red;">`DELETE`</mark>` ``/api/v2/tenants/{tenantId}/security/role/{roleId}`

</details>

<details>

<summary>Release 2.23 - November 6, 2025</summary>

**Summary:** Removes support for `limit=99999` on the report findings endpoint.

**Details:** The [**Get Findings by Report**](https://api-docs.plextrac.com/#88b61efa-7f17-42ba-b383-81dad70ff7b7) endpoint currently accepts a `limit` parameter to control the number of findings returned per request. Accepted values include 1, 10, 50, 100, and 99999. The `99999` option has been used to return all findings from a report in a single call.\
However, this endpoint is one of the most resource-intensive in the platform, as it enriches each finding with related asset and instance data. Supporting unbounded responses has led to performance and stability issues.

To ensure consistent and predictable behavior, support for `"limit": 99999` will be deprecated in Release 2.19, and fully removed in Release 2.23.

Users should adopt a true paginated approach using the other supported limits before the functionality is removed.

**Impacted Endpoint:**

* `POST /api/v2/clients/{clientId}/reports/{reportId}/findings`

</details>

[^1]:
