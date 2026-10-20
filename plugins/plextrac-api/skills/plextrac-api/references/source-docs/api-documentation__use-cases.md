# Use Cases

This page describes how the API can achieve a goal or objective and outlines the steps involved in a scenario, the tasks or actions to be performed, and the expected results or outcomes.

The use cases are set to a specific objective and outcome and intended as a template to leverage for all API needs.

## Use Cases Groupings

The use cases are separated into three categories:

1. **Introductory Use Cases:** Objectives common for all PlexTrac users when getting started. These use cases are relatively straightforward.
2. **Intermediate Use Cases:** Objectives that are easy to achieve within the platform but contain non-intuitive steps when done via API. Some platform interactions send multiple API requests, which can be confusing to replicate when manually calling API endpoints.
3. **Advanced Use Cases:** Objectives are not available within the platform but are doable via API. Since certain platform functionality consists of making requests to multiple API endpoints,  new functionality can be created by combining various API requests and data transformation. \
   \
   An example of an advanced use case is with data import/export. While Plextrac doesn't have the functionality to import/export all stored data, <mark style="color:yellow;">POST</mark> requests to create and <mark style="color:green;">GET</mark> requests exist in the database. Combining a <mark style="color:green;">GET</mark> request with saving the response to a JSON can make the functionality to export the data. Data can be imported by combining some data transformation to remove IDs and a <mark style="color:yellow;">POST</mark> request to create a new data object.&#x20;

## **Introductory Use Cases**

<details>

<summary>Generating Session Token Without MFA</summary>

**Objective:** Obtain a valid token and cookie for a session.

**Notes:** [<mark style="color:orange;">POST</mark> Authentication](https://api-docs.plextrac.com/#65d40d98-bfaf-4452-8ab0-3ffeeb280923) is the auth endpoint for a user without MFA.&#x20;

1. Execute the <mark style="color:orange;">POST</mark> Authentication API: `{{instanceUrl}}/api/v1/authenticate` by providing a valid instance url, user name and password in the parameters of the request.&#x20;
2. If successful, the `tennant_id`, `cookie`, and `token` values will be returned.<br>

   <div align="left"></div>
3. Extract the session token from the response body.
4. Use the value in the `token` field as the required Bearer token sent to other endpoints.

The token is good for 15 minutes.

</details>

<details>

<summary>Retrieving List of Tenant Users</summary>

**Objective:** Obtain a list of all users for a tenancy.

**Notes:** [<mark style="color:green;">GET</mark> Tenant Users](https://api-docs.plextrac.com/#33875455-51fc-437c-b064-57acea3b65e9) is the endpoint for obtaining a list of tenant users.&#x20;

1. Execute the <mark style="color:green;">GET</mark> Tenant Users API: `{{instanceUrl}}/api/v2/tenants/{{tenantId}}/users` by providing a valid instance url and tenant ID in the parameters of the request.
2. If successful, a list of users will be returned with several attributes tied to each user, such as when the user was created, what role they belong to, email address, and last login date.\
   ![](https://4252973360-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LXA6EayCcg12qfDcfXd%2Fuploads%2FJoL8zF4CBwUHZgXjDUKu%2Fimage.png?alt=media\&token=0ba825ea-9c23-4347-b4f9-4eca5c99062f)

</details>

## **Intermediate Use Cases**&#x20;

<details>

<summary>Adding Images to CKEditor Fields</summary>

**Objective:** Add images through the API that are rendered in the platform and on export as a Microsoft Word document.&#x20;

**Notes:** This functionality exists within the platform, but accomplishing it through the API is not intuitive. <mark style="color:orange;">POST</mark> Upload Image to `Tenant[https://api-docs.plextrac.com/#35efb6b8-22d3-4271- 98fa-b9865d072461]` is used in conjunction with any endpoint that creates or updates an object that contains a CKEditor field

**Summary:** When passing images through API requests, one common practice is to send the Base64 encoded image as a string. This will not work if exporting a report with the image to Microsoft Word, as this format does not support Base64 encoded images.&#x20;

**Steps:**

1. Add the image to your instance with the <mark style="color:orange;">POST</mark> Upload Image to `Tenant[https://api- docs.plextrac.com/#35efb6b8-22d3-4271-98fa-b9865d072461]` endpoint.
2. The fileUrl value should appear in the response. NOTE: If the file extension is not listed, it means the file was read as a byte stream, not as a file, and as such is not accessible (i.e. "uploads/0f645c65-ad95- 4a71-9c53-fb096442dfb8").<br>

   <div align="left"></div>
3. Add the HTML tag `<img src="/api/v1/{VALUE OF fileUrl FROM RESPONSE}">`. For example: `<img src="/api/v1/uploads/fee189cd-d7fa-46cd-962d-0cc5631099d6.jpg">`
4. Create the JSON payload to generate a new finding and add this HTML tag to the description value.
5. Send the created JSON payload on the <mark style="color:orange;">POST</mark> `Create Finding[https://api-docs.plextrac.com/#c7877845-5b51-40c9-ba50-931114aa0a30]` request

</details>

<details>

<summary>Copying a Finding from a Report to a WriteupsDB repository</summary>

**Objective**: Copy a finding from a report to the WriteupsDB repository.

**Notes**: This is currently done in the PlexTrac frontend with a deprecated endpoint, <mark style="color:orange;">`POST`</mark>` ``/api/v2/repositories/copyFlawToWriteupsRepository`. This endpoint has the same functionality as <mark style="color:orange;">`POST`</mark>` ``/api/v1/template/create`, which should be used instead.

**Summary**: In the platform, when viewing the finding list in a report, a writeup can be copied to a WriteupDB repository by clicking the metaballs menu in the finding row and clicking **Copy to WriteupDB**. This use case triggers a multi-step process to get the finding data and send it in a request to create a new writeup.

**Steps:**

1. Call the <mark style="color:green;">`GET`</mark>` ``/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` endpoint to get the finding JSON.
2. Navigate into the WriteupsDB repository to copy the finding. Look at the page URL and [copy down the CUID of the repository](/plextrac-documentation/api-documentation/retrieving-parameter-ids.md#repository-ids).
3. Add the key "repositoryId" and the value "" to the finding JSON (i.e., "repositoryId": "clgn7pad8046c28n27tbg8ue3").\
   ![](https://4252973360-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LXA6EayCcg12qfDcfXd%2Fuploads%2F4tjM0pEygL0Yv0cgaeBm%2Fimage.png?alt=media\&token=c9400ed2-8d9e-4c02-88fe-1ed678c1ea74)
4. Send the updated finding JSON as the payload in the <mark style="color:orange;">`POST`</mark>` ``/api/v1/template/create endpoint.`

</details>

## **Advanced Use Cases**

<details>

<summary>Reusing an Assessment</summary>

**Objective:** Take an existing completed client assessment and create a new In Process assessment for another client.

**Notes:** The functionality to create a new In Process assessment for the same client exists within the platform, but this assessment cannot be created on a different client. However, this can be accomplished through the API with the [<mark style="color:green;">GET</mark> Client Assessment](https://api-docs.plextrac.com/#b2c33cc9-7bbd-40f0-b15c-2017f8d9e418) and [<mark style="color:orange;">POST</mark> Create Client Assessment](https://api-docs.plextrac.com/#3bbdf8e8-3ab0-4f80-b6b9-bc7a9961e30e) endpoints.

1. Identify the existing assessment to reuse.&#x20;
2. Use the <mark style="color:green;">GET</mark> Client Assessment API on the completed client assessment. This will return the JSON of that assessment data including questions and answers.
3. Modify the JSON by removing the properties `tenant_id`, `client_id`, `assess_id`, and `completed_at`. Change the value of `saveOnly` to `true`.
4. Go through the list of answers and update the `note` field to be a non-empty string.
5. Use the <mark style="color:orange;">POST</mark> Create Client Assessment to create the new in process client assessment. Set the new `tenantId` and `clientId` in the URL and send the modified JSON as the payload.

</details>
