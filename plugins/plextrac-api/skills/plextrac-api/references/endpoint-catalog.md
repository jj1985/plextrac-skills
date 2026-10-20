# PlexTrac API endpoint catalog

Generated from the official Postman collection (api-docs.plextrac.com) on 2026-10-20: 363 requests in 24 top-level folders.
Paths are relative to the instance URL. `{param}` = path parameter. Operation IDs match the bundled OpenAPI spec.

## Contents

- [Authentication](#authentication)
- [Admin](#admin)
- [Affected Assets](#affected-assets)
- [Analytics](#analytics)
- [Assessments](#assessments)
- [Assets](#assets)
- [Content Library](#content-library)
- [Clients](#clients)
- [Files](#files)
- [Findings](#findings)
- [Integrations](#integrations)
- [Mailer](#mailer)
- [Parser Actions](#parser-actions)
- [QA Workflow](#qa-workflow)
- [Reports](#reports)
- [Runbooks](#runbooks)
- [Scheduler](#scheduler)
- [Substatus](#substatus)
- [Templates](#templates)
- [Tenant](#tenant)
- [Users](#users)
- [Graph QL Queries](#graph-ql-queries)
- [Graph QL Mutations](#graph-ql-mutations)
- [Webhooks](#webhooks)

## Authentication

This collection contains requests related to logging in to PlexTrac:

authenticating via a user's name and password

authenticating the user via multi-factor authentication

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/api/v1/authenticate` | `authentication` (Authentication) | Authenticate | For more info visit: https://docs.plextrac.com/plextrac-documentation/master/plextrac-api-overview#getting-started · body |
| POST | `/api/v1/authenticate/mfa` | `multiFactorAuthentication` (Multi-Factor Authentication) | Authenticate | This request validates access via multifactor authentication (MFA) and requires additional verification. Below is a list of information needed to fulfil the request. · body |
| PUT | `/api/v1/token/refresh` | `refreshToken` (Refresh Token) | Authenticate | This endpoint is used to refresh the authentication token. |
| GET | `/api/v2/user/mfa/qr` | `generateQRCode` (Generate QR code) | Setup MFA | This request generates a QR code link that can be used to set up multi-factor authorization (MFA). |
| POST | `/api/v2/user/mfa/qr/activate` | `activateMFA` (Activate MFA) | Setup MFA | This request activates a QR code that is used to set up multi-factor authorization (MFA) by including the six-digit MFA code provided by the third-party authorization tool as a variable in the body. · body |

## Admin

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| GET | `/api/v2/authenticate/providers` | `getAvailableAuthenticationProviders` (Get Available Authentication Providers) | Auth | Return a list of supported authentication providers |
| GET | `/api/v2/tenants/{tenantId}/providers/plextrac` | `getTenantProviderAuthenticationConfiguration` (Get Tenant Provider Authentication Configuration) | Auth | Admin only route, update authentication provider configuration |
| POST | `/api/v2/tenants/{tenantId}/providers/plextrac` | `updateTenantAuthenticationProviderConfiguration` (Update Tenant Authentication Provider Configuration) | Auth | Update configuration for tenant authentication providers (Okta, Azure AD, Google) (Admin only) · body |
| PUT | `/api/v2/authenticate/tenants/{tenantId}/users/{userId}/configuration` | `updateTenantUserAuthenticationMethod` (Update Tenant User Authentication Method) | Auth | Update the authentication method a tenant user is authorized to log in with (admin only) · body |
| GET | `/api/v2/tenants/{tenantId}/saml/plextrac` | `getSamlProvider` (Get Saml Provider) | Auth | Endpoint for getting a single saml provider configuration, validate: { |
| POST | `/api/v2/tenants/{tenantId}/saml/plextrac` | `upsertSamlConfiguration` (Upsert Saml Configuration) | Auth | Endpoint for updating and creating saml providers for a tenant. |
| GET | `/api/v2/tenants/{tenantId}/user/{userId}/permissions` | `getUserPermissions` (Get User Permissions) | Security / RBAC / Users | Gets a user's RBAC permissions. |
| GET | `/api/v2/tenants/{tenantId}/security/role/{roleKey}/users` | `getRoleUsers` (Get Role Users) | Security / RBAC / Users | Gets all users associated with a certain RBAC security role. |
| PUT | `/api/v2/tenants/{tenantId}/security/role/{roleId}/users` | `addRoleUser` (Add Role User) | Security / RBAC / Users | Adds a user to an RBAC Security Role. · body |
| DELETE | `/api/v2/tenants/{tenantId}/security/role/{roleId}/users/{userId}` | `removeRoleUser` (Remove Role User) | Security / RBAC / Users | Removes a user from an RBAC security role. |
| GET | `/api/v2/tenants/{tenantId}/security/role/available` | `getAvailableSecurityRoles` (Get Available Security Roles) | Security / RBAC | Gets a list of RBAC security roles and returns the name and CUID of each role. |
| GET | `/api/v2/tenants/{tenantId}/security/role` | `getSecurityRoles` (Get Security Roles) | Security / RBAC | Get a list of RBAC security roles. |
| GET | `/api/v2/tenants/{tenantId}/security/role/{roleId}` | `getSecurityRole` (Get Security Role) | Security / RBAC | Gets an RBAC security role. |
| POST | `/api/v2/tenants/{tenantId}/security/role/availability` | `getRoleNameAvailability` (Get Role Name Availability) | Security / RBAC | Determines availability for a new RBAC Security Role. · body |
| POST | `/api/v2/tenants/{tenantId}/security/role` | `createSecurityRole` (Create Security Role) | Security / RBAC | Creates a new RBAC security role. |
| PUT | `/api/v2/tenants/{tenantId}/security/role/{roleId}/info` | `updateSecurityRoleInfo` (Update Security Role Info) | Security / RBAC | Updates a security role's info fields. · body |
| PUT | `/api/v2/tenants/{tenantId}/security/role/{roleId}/permissions` | `updateSecurityRolePermission` (Update Security Role Permission) | Security / RBAC |  |
| DELETE | `/api/v2/tenants/{tenantId}/security/role/{roleId}` | `deleteSecurityRole` (Delete Security Role) | Security / RBAC |  |
| GET | `/api/v1/tenant/{tenantId}/tag` | `listTenantTags` (List Tenant Tags) | Tags | This request retrieves a list of all tags for a tenant with filter options. |
| POST | `/api/v1/tenant/{tenantId}/tag` | `createTenantTag` (Create Tenant Tag) | Tags | This request creates a new tag for a tenant. A created tag will be listed on the tag dropdown that appears when typing to add a tag anywhere in the platform. This functionality is found in the platfor · body |
| DELETE | `/api/v1/tenant/{tenantId}/tag/{tagId}` | `deleteTenantTag` (Delete Tenant Tag) | Tags | This request creates a new tag for a tenant. This functionality is found in the platform under Account Admin > Tag Settings > Actions > Delete |
| GET | `/api/v1/tenant/{tenantId}/tag/search` | `searchTenantTags` (Search Tenant Tags) | Tags | This endpoint allows users to search for tags within a specific tenant. |
| POST | `/api/v1/tenant/{tenantId}/tag/find` | `findTenantTag` (Find Tenant Tag) | Tags | This endpoint allows developers to find a tag for a specific tenant. · body |
| GET | `/api/v2/sla/benchmarks` | `getSLABenchmarks` (Get SLA Benchmarks) | SLAs | This request retrieves all SLA benchamrks for a tenant. |
| POST | `/api/v2/sla/benchmarks` | `createSLABenchmark` (Create SLA Benchmark) | SLAs | This request creates a new SLA benchmark within a tenant. · body |
| GET | `/api/v2/sla/benchmarks/{slaBenchmarkId}` | `getSLABenchmark` (Get SLA Benchmark) | SLAs | This request retrieves information on a SLA benchmark. |
| PUT | `/api/v2/sla/benchmarks/{slaBenchmarkId}` | `updateSLABenchmark` (Update SLA Benchmark) | SLAs | This request updates an existing SLA benchamrk. This is a PUT request and will overwrite the current SLA with the new payload. · body |
| DELETE | `/api/v2/sla/benchmarks/{slaBenchmarkId}` | `deleteSLABenchmark` (Delete SLA Benchmark) | SLAs | This request removes a SLA benchmark from a tenant. |
| GET | `/api/v2/auditlog` | `getAuditLog` (Get Audit Log) | Audit Log | This endpoint retrieves audit log data. The logs that show up under Admin Dashboard > Security & User Management > Audit Logs are not the comprehensive app logs, but only a subset.   |

## Affected Assets

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/api/v2/clients/{clientId}/reports/{reportId}/flaws/{findingId}/affected-assets/import/{source}` | `importFindingAffectedAssets` (Import Finding Affected Assets) | - | URL source accepts 'csv', 'xml' · body |
| DELETE | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}` | `removeAffectedAssetFromFlaw` (Remove Affected Asset from Flaw) | - |  |
| POST | `/api/v2/client/{clientId}/report/{reportId}/flaw/{findingId}/assets/status` | `bulkGetAffectedAssetsStatus` (Bulk Get Affected Assets Status) | - | For affected assets on a report finding, gets the most recent status tracker update for each affected asset requested. Affected assets without any status tracker update will not return an entry in the · body |
| GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/status` | `getAffectedAssetStatusList` (Get Affected Asset Status List) | - | Retrieves the list of all status tracker updates for an affected asset. |
| POST | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/status/update` | `createAffectedAssetStatus` (Create Affected Asset Status) | - | Adds a status tracker update for an affected asset on a finding. The payload of this request should be the entire finding object retrieve from the Get Findings endpoint. · body |
| POST | `/api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/status` | `bulkCreateAffectedAssetStatus` (Bulk Create Affected Asset Status) | - | body |

## Analytics

The Analytics module provides metrics and trends on findings, assets, runbooks, and SLAs.

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/api/v1/clients/analytics` | `retrieveAnalytics` (Retrieve Analytics) | Findings | Rate Limits: Due to how heavy this request is on the DB we have enable rate limiting. You can make 1 request per 5 seconds. · body |
| POST | `/api/v1/clients/analytics/findings` | `retrieveAnalyticsFindings` (Retrieve Analytics Findings) | Findings | Rate Limits: Due to how heavy this request is on the DB we have enable rate limiting. You can make 1 request per 5 seconds. · body |
| POST | `/api/v1/clients/analytics/findings/aging` | `retreiveAnalyticsFindingsAging` (Retreive Analytics Findings Aging) | Findings | This request retrieves analytics on findings based on the date of finding per client, providing a total count of findings per client and total count by severity. The query defaults to 30 days but can  · body |
| POST | `/api/v2/findingAnalytics/bootstrap` | `getFindingAnalyticsBootstrap` (Get Finding Analytics Bootstrap) | Findings | StartFragment · body |
| POST | `/api/v2/clients/analytics/assets/overview` | `retrieveAnalyticsAssets` (Retrieve Analytics Assets) | Assets | Rate Limits: Due to how heavy this request is on the DB we have enable rate limiting. You can make 1 request per 5 seconds. · body |
| POST | `/api/v2/clients/analytics/assets` | `retrieveAnalyticsAssetsWithFilter` (Retrieve Analytics Assets with Filter) | Assets | This request retrieves information about assets stored under clients and provides the ability to filter and limit the data set returned. · body |
| POST | `/api/v2/clients/analytics/trends/opened-closed` | `analyticsTrendsOpenedClosed` (Analytics - Trends - Opened Closed) | Trends | POST: · body |
| POST | `/api/v2/clients/analytics/trends/from-creation-to-close` | `analyticsTrendsFromCreationToClose` (Analytics - Trends - From creation to close) | Trends | POST: · body |
| POST | `/api/v2/clients/analytics/trends/age-of-open-findings` | `analyticsTrendsAgeOfOpenFindings` (Analytics - Trends - Age of open findings) | Trends | POST: · body |
| POST | `/api/v2/sla/analytics/mean-time` | `analyticsTrendsSLAs` (Analytics - Trends - SLAs) | Trends | body |
| POST | `/api/v2/sla/analytics/findings` | `analyticsTrendsSLAFindings` (Analytics - Trends - SLA Findings) | Trends | body |

## Assessments

The Assessments module in PlexTrac allows users to create questionnaires, which when completed can then be used to build reports.

This collection contains subfolders for Questionnaires and Client Assessments.

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| GET | `/api/v2/assessments/questionnaires/{questionnaireId}/questions` | `listQuestions` (List Questions) | Questionnaires / Questions | This request retrieves all questions that exist for a specific questionnaire. |
| GET | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}` | `getQuestion` (Get Question) | Questionnaires / Questions | This request retrieves a specific question from a specific questionnaire. |
| POST | `/api/v2/assessments/questionnaires/{questionnaireId}/questions` | `createQuestion` (Create Question) | Questionnaires / Questions | This request creates a question for a specific questionnaire. · body |
| PUT | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}` | `updateQuestion` (Update Question) | Questionnaires / Questions | This request updates a questions that exists for a specific questionnaire. · body |
| PUT | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}/order` | `changeQuestionOrder` (Change Question Order) | Questionnaires / Questions | This request changes the order of a specific question for a specific questionnaire. · body |
| DELETE | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}` | `deleteQuestion` (Delete Question) | Questionnaires / Questions | This request deletes a specific question for a specific questionnaire. |
| POST | `/api/v2/tenant/{tenantId}/client/{clientId}/answertypes` | `listAnswerTypes` (List Answer Types) | Questionnaires / Answer Types | This request retrieves all answer types that exist for a client. · body |
| GET | `/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}` | `getAnswerType` (Get Answer Type) | Questionnaires / Answer Types | This request retrieves a specific answer type using answerTypeId. |
| PUT | `/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}` | `updateAnswerType` (Update Answer Type) | Questionnaires / Answer Types | This request updates a specific answer type for a specific client using answerTypeId. · body |
| POST | `/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/create` | `createAnswerType` (Create Answer Type) | Questionnaires / Answer Types | This request creates an answer for a specific client. · body |
| DELETE | `/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}` | `deleteAnswerType` (Delete Answer Type) | Questionnaires / Answer Types | This request deletes a specific answer type for a specific client using answerTypeId. |
| GET | `/api/v1/tenant/{tenantId}/assessments` | `listQuestionnaires` (List Questionnaires) | Questionnaires | This request retrieves all assessments for a tenant. |
| GET | `/api/v2/assessments/questionnaires/{questionnaireId}` | `getQuestionnaire` (Get Questionnaire) | Questionnaires | This request retrieves a specific questionnaire from the Assessments module. |
| POST | `/api/v2/assessments/questionnaires` | `createQuestionnaire` (Create Questionnaire) | Questionnaires | This request creates a questionnaire to be stored in the Assessments module. · body |
| PUT | `/api/v2/assessments/questionnaires/{questionnaireId}` | `updateQuestionnaire` (Update Questionnaire) | Questionnaires | This request updates information for a specific questionnaire in the Assessments module. · body |
| DELETE | `/api/v1/tenant/{tenantId}/assessment/{questionnaireId}` | `deleteQuestionnaire` (Delete Questionnaire) | Questionnaires | This request removes an assessment from a tenant. |
| GET | `/api/v2/assessments/questionnaires/{questionnaireId}/export` | `exportQuestionnaire` (Export Questionnaire) | Questionnaires | This request exports a specific questionnaire from the Assessments module. |
| POST | `/api/v2/import/questionnaire` | `importQuestionnaire` (Import Questionnaire) | Questionnaires | This request imports a questionnaire to the Assessments module. · body |
| GET | `/api/v2/tenants/{tenantId}/assessments` | `listTenantAssessments` (List Tenant Assessments) | Client Assessments | This request retrieves a list of assessments for a specific tenant with the ability to sort and filter results. |
| GET | `/api/v1/tenant/{tenantId}/client/{clientId}/assessments` | `listClientAssessments` (List Client Assessments) | Client Assessments | This request retrieves a list of all assessments for a specific client within a tenant. |
| GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments` | `listClientAssessmentsFiltered` (List Client Assessments (Filtered)) | Client Assessments |  |
| GET | `/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}` | `getClientAssessmentWithQuestionsAndAnswers` (Get Client Assessment (with questions and answers)) | Client Assessments | This request retrieves a list of a specific assessment for a specific client within a tenant. |
| GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}` | `getClientAssessment` (Get Client Assessment) | Client Assessments | This request returns the data for a specific assessment started for a specific client. |
| GET | `/api/v2/assessments/{assessmentCuid}` | `getAssessmentByCUID` (Get Assessment by CUID) | Client Assessments |  |
| GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/questions` | `getAssessmentQuestions` (Get Assessment Questions) | Client Assessments | This request retrieves questions for a specific assessment for a specific client with the ability to sort and filter results. |
| GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers` | `getAssessmentAnswers` (Get Assessment Answers) | Client Assessments | This request retrieves answers for a specific assessment for a specific client with the ability to sort and filter results. |
| PUT | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers` | `updateAssessmentAnswers` (Update Assessment Answers) | Client Assessments | This request updates answers for an assessment. · body |
| GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/reviewers` | `getAssessmentReviewers` (Get Assessment Reviewers) | Client Assessments | This request retrieves a list of reviewers for a an assessment. |
| POST | `/api/v1/tenant/{tenantId}/client/{clientId}/assessment` | `createClientAssessment` (Create Client Assessment) | Client Assessments | This request creates a new assessment for a specific client within a tenant. · body |
| PUT | `/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}` | `updateClientAssessment` (Update Client Assessment) | Client Assessments | This request updates an assessment. · body |
| DELETE | `/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}` | `deleteClientAssessment` (Delete Client Assessment) | Client Assessments | This request will delete an assessment for a client. |
| POST | `/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}/report` | `createReportFromAssessmentQuestionnaire` (Create Report From Assessment Questionnaire) | Client Assessments | This request will create a report from assessments for a client. · body |
| POST | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/copy` | `copyAsessmentQuestionnaire` (Copy Asessment Questionnaire) | Client Assessments | This request creates a new assessment from a previously completed assessment, copying over questions and answers. |

## Assets

This collection contains the following requests related to assets:

get a list of all client assets

get a specific asset

create a client asset

update a client asset

delete a client asset

import an asset from Network Mapper

bulk deletion of assets

remove an asset from a finding

get a scanner output

get a list of affected assets

create affected asset status

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/api/v2/tenant/assets` | `getTenantAssets` (Get Tenant Assets) | - | This request retrieves the list of assets for a tenant. · body |
| POST | `/api/v2/clients/{clientId}/assets` | `getAssetsByClient` (Get Assets by Client) | - | This request retrieves the list of assets for a specific client. · body |
| GET | `/api/v1/client/{clientId}/assets` | `listClientAssets` (List Client Assets) | - | DEPRECATED will be removed 12/03/2024 |
| GET | `/api/v2/clients/{clientId}/reports/{reportId}/assets` | `listReportAssets` (List Report Assets) | - | This request retrieves a list of assets for a specific report. |
| GET | `/api/v1/client/{clientId}/asset/{assetId}` | `getAsset` (Get Asset) | - | This request retrieves a specific asset for a specific client. |
| PUT | `/api/v1/client/{clientId}/asset/0` | `createAsset` (Create Asset) | - | This request creates an asset for a client. · body |
| PUT | `/api/v1/client/{clientId}/asset/{assetId}` | `updateAsset` (Update Asset) | - | This request updates a specific asset for a client. · body |
| DELETE | `/api/v1/client/{clientId}/asset/{assetId}` | `deleteAsset` (Delete Asset) | - | This request deletes a specific asset for a client. |
| POST | `/api/v1/client/{clientId}/assets/import/{source}` | `importClientAssetsV1` (Import Client Assets v1) | - | Deprecated. Please use Import Client Assets v2 · body |
| POST | `/api/v2/client/{clientId}/assets/import/{source}` | `importClientAssetsV2` (Import Client Assets v2) | - | This request imports assets from an outside tool into PlexTrac for a specific client. · body |
| POST | `/api/v1/client/{clientId}/bulk/assets/delete` | `bulkDeleteClientAssets` (Bulk Delete Client Assets) | - | This requests deletes the Client Assets sent in the payload. · body |
| GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/scanoutput` | `getScannerOutput` (Get Scanner Output) | - | Retrieve all Evidence on an Affected Asset. |

## Content Library

This collection contains requests related to working with the WriteupsDB module, which is found under the Content Library menu item in the PlexTrac tool.

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/api/v2/narratives/sections/all` | `listAllSections` (List All Sections) | NarrativesDB / Narratives (Sections) | This request retrieves all sections that exist in the NarrativesDB module for a tenant. · body |
| POST | `/api/v2/narratives/{repositoryId}/sections` | `listNarrativeRepositorySections` (List Narrative Repository Sections) | NarrativesDB / Narratives (Sections) | This request retrieves all sections for a specific repository exists in the NarrativesDB module. · body |
| GET | `/api/v2/narratives/sections/{sectionId}` | `getNarrativeRepositorySection` (Get Narrative Repository Section) | NarrativesDB / Narratives (Sections) | This request retrieves a specific section that exist in the NarrativesDB module. |
| POST | `/api/v2/narratives/createNarrativesRepository` | `createNarrativesDBRepository` (Create NarrativesDB Repository) | NarrativesDB / Narratives (Sections) | This request creates a NarrativesDB repository that is put in the NarrativesDB module of the Content Library. · body |
| POST | `/api/v2/narratives/sections` | `createNarrativesRepositorySection` (Create Narratives Repository Section) | NarrativesDB / Narratives (Sections) | This request creates a section in the NarrativesDB module of the Content Library. · body |
| PUT | `/api/v2/narratives/sections/{sectionId}` | `updateNarrativeDBSection` (Update NarrativeDB Section) | NarrativesDB / Narratives (Sections) | This request updates a section that exists in the NarrativesDB module. · body |
| DELETE | `/api/v2/narratives/{repositoryId}/sections/{sectionId}` | `deleteNarrativeDBSection` (Delete NarrativeDB Section) | NarrativesDB / Narratives (Sections) | This request deletes a section from a specific repository in the NarrativesDB module. |
| POST | `/api/v2/narratives/getAllNarrativesRepositories` | `listNarrativeDBs` (List NarrativeDBs) | NarrativesDB / Narratives (Sections) | This request retrieves a list of all repositories that is in the NarrativesDB module of the Content Library based on the user making the call and the permissionsLevel body param. · body |
| POST | `/api/v2/narratives/sections/copy` | `copySectionToNarativeRepository` (Copy Section to Narative Repository) | NarrativesDB / Narratives (Sections) | This request copies a section to another repository in the NarrativesDB module. · body |
| POST | `/api/v2/narratives/users/all` | `getAllNarrativeDBUsers` (Get All NarrativeDB Users) | NarrativesDB / Users | This request retrieves all users that have been added to repositories in the NarrativesDB module. · body |
| POST | `/api/v2/narratives/{narrativeRepositoryId}/users` | `getNarrativeDBUsersByRepository` (Get NarrativeDB Users by Repository) | NarrativesDB / Users | This request retrieves users for a specific repository in the NarrativesDB module. · body |
| PUT | `/api/v2/narratives/{narrativeRepositoryId}/users` | `updateNarrativeDBUsersByRepository` (Update NarrativeDB Users by Repository) | NarrativesDB / Users | This request adds users to a specific repository in the NarrativesDB module. · body |
| GET | `/api/v2/narratives/{narrativeRepositoryId}/getNarrativesRepository` | `getNarrativeDB` (Get NarrativeDB) | NarrativesDB | This request retrieves a specific repository and its metadata from the NarrativesDB module. |
| PUT | `/api/v2/narratives/{narrativeRepositoryId}/updateNarrativesRepository` | `updateNarrativeDB` (Update NarrativeDB) | NarrativesDB | This request updates a specific repository and its metadata from the NarrativesDB module. · body |
| DELETE | `/api/v2/narratives/{narrativeRepositoryId}/deleteNarrativesRepository` | `deleteNarrativeDB` (Delete NarrativeDB) | NarrativesDB | This request deletes a specific repository from the NarrativesDB module. |
| GET | `/api/v1/template/list` | `listWriteups` (List Writeups) | WriteupsDB / Writeups | This request retrieves all WriteupsDB entries for a tenant. |
| GET | `/api/v1/template/{writeupId}` | `getWriteup` (Get Writeup) | WriteupsDB / Writeups | This request retrieves a defined writeup. |
| POST | `/api/v1/template/create` | `createWriteups` (Create Writeups) | WriteupsDB / Writeups | This request adds a new writeup to a specific repository. · body |
| PUT | `/api/v1/template/{writeupId}` | `updateWriteups` (Update Writeups) | WriteupsDB / Writeups | This request updates an existing writeup for a tenant. · body |
| DELETE | `/api/v1/template/{writeupId}` | `deleteWriteups` (Delete Writeups) | WriteupsDB / Writeups | This request will delete a writeup from WriteupsDB by providing the instance url and writeup ID. |
| PUT | `/api/v1/copy/{writeupId}` | `addWriteupToReport` (Add Writeup to Report) | WriteupsDB / Writeups | Deprecated: See v2 endpoint Bulk Add Writeups to Report for similar functionality. · body |
| POST | `/api/v2/writeups/bulk/addToReport` | `bulkAddWriteupsToReport` (Bulk Add Writeups to Report) | WriteupsDB / Writeups | This request adds a writeup in the WriteupsDB module to an existing report. · body |
| POST | `/api/v2/repositories/{repositoryId}/getWriteups` | `getWriteupsFromRepository` (Get Writeups from Repository) | WriteupsDB / Writeups | This request retrieves all writeups from a specific repository in the WriteupsDB module. · body |
| POST | `/api/v2/repositories/{repositoryId}/addWriteups` | `addWriteupsToRepository` (Add Writeups to Repository) | WriteupsDB / Writeups | This request moves a writeup in the WriteupsDB module to different repository. · body |
| POST | `/api/v2/repositories/copyFlawToWriteupsRepository` | `copyFindingToWriteupsRepository` (Copy Finding to Writeups Repository) | WriteupsDB / Writeups | Deprecated: Since this endpoint's payload requires the finding object, it proves the same functionality as POST Create Writeups which should be used instead. · body |
| POST | `/api/v2/writeups/import/{source}` | `importWriteupsToRepository` (Import Writeups to Repository) | WriteupsDB / Writeups | This request imports a csv of writeups to the WriteupsDB module. · body |
| POST | `/api/v2/repositories/{repositoryId}/removeWriteup` | `removeWriteupsFromRepository` (Remove Writeups from Repository) | WriteupsDB / Writeups | This request removes a writeup from a specific repository in the WriteupsDB module. · body |
| POST | `/api/v2/writeups/bulk/copy` | `bulkCopyWriteups` (Bulk Copy Writeups) | WriteupsDB / Writeups | This request copies writeups from a repository in the WriteupsDB module. · body |
| POST | `/api/v2/writeups/bulk/move` | `bulkMoveWriteups` (Bulk Move Writeups) | WriteupsDB / Writeups | This request moves a writeup to another repository in the WriteupsDB module. · body |
| POST | `/api/v2/writeups/bulk/tags` | `bulkAddTagsToWriteups` (Bulk Add Tags to Writeups) | WriteupsDB / Writeups | This request adds tags to a writeup in the WriteupsDB module. · body |
| POST | `/api/v2/writeups/bulk/delete` | `bulkDeleteWriteups` (Bulk Delete Writeups) | WriteupsDB / Writeups | This request bulk deletes a list of writeups, removing them from any repositories, in the WriteupsDB module. · body |
| POST | `/api/v2/repositories/getAllWriteupsRepositories` | `listAllWriteupRepositories` (List All Writeup Repositories) | WriteupsDB / Repositories | This request retrieves a list of repositories in the WriteupsDB module. · body |
| GET | `/api/v2/repositories/listUserCanEdit` | `getWriteupsRepositoryUsersCanEdit` (Get Writeups Repository Users Can Edit) | WriteupsDB / Repositories | If the user has the RBAC permission ACCESS_WRITEUPS_REPOSITORIES, this request retrieves a list of repositories in the WriteupsDB module that the user is assigned an EDITOR on. |
| POST | `/api/v2/repositories/{repositoryId}` | `getWriteupRepository` (Get Writeup Repository) | WriteupsDB / Repositories | This request retrieves a specific repository and associated metadata in the WriteupsDB module. · body |
| POST | `/api/v2/repositories/add` | `createWriteupRepository` (Create Writeup Repository) | WriteupsDB / Repositories | This request adds a new repository in the WriteupsDB module. · body |
| POST | `/api/v2/repositories/{repositoryId}/update` | `updateWriteupRepository` (Update Writeup Repository) | WriteupsDB / Repositories | This request updates a specific repository and associated metadata in the WriteupsDB module. · body |
| POST | `/api/v2/repositories/delete` | `deleteWriteupRepository` (Delete Writeup Repository) | WriteupsDB / Repositories | This request deletes a repository in the WriteupsDB module. · body |
| GET | `/api/v2/repositories/{repositoryId}/users` | `getWriteupsRepositoryUsers` (Get Writeups Repository Users) | WriteupsDB / Users | This request retrieves all users from a specific repository in the WriteupsDB module. |
| POST | `/api/v2/repositories/{repositoryId}/users` | `addWriteupsRepositoryUsers` (Add Writeups Repository Users) | WriteupsDB / Users | This request adds users to a specific repository in the WriteupsDB module by adding a new user entry for each user in the list sent to the endpoint. · body |
| PUT | `/api/v2/repositories/{repositoryId}/users` | `updateWriteupsRepositoryUsers` (Update Writeups Repository Users) | WriteupsDB / Users | This request replaces the current list of users with a new one for a specific repository in the WriteupsDB module. · body |
| POST | `/api/v2/repositories/users` | `getAllWriteupsRepositoryUsers` (Get All Writeups Repository Users) | WriteupsDB / Users | This request retrieves a list of users in the WriteupsDB module with the MANAGE_WRITEUPS_REPOSITORIES RBAC permission and returns the list filter by and user that has the filterText in the first name, · body |

## Clients

This Clients module in the PlexTrac solution allows the ability to separate data as clients. A client could be a project, a business unit, a region, or a program... any grouping that requires data to be siloed from other findings, reports, and assets.

This collection contains the following requests related to clients:

retrieve a list of all clients authorized to view

get object/information about a client

create a client

update a client

delete a client

add a client logo

delete a client logo

COMING SOON:

get analytics on a client

obtain findings status of a client

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| GET | `/api/v1/tenant/{tenantId}/client/{clientId}/users` | `listClientUsersV1` (List Client Users v1) | Client Users | This request retrieves a list of all users for a specific client. |
| GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/users` | `listClientUsersV2` (List Client Users v2) | Client Users | This request retrieves a list of all users for a specific client. |
| GET | `/api/v1/tenant/{tenantId}/client/{clientId}/users/available` | `availableTenantUsers` (Available Tenant Users) | Client Users |  |
| POST | `/api/v1/tenant/{tenantId}/client/{clientId}/user/assign` | `assignUserToClientV1` (Assign User to Client v1) | Client Users | DEPRECATED - See Assign Users to Client v2 · body |
| POST | `/api/v2/tenant/{tenantId}/client/{clientId}/user/assign` | `assignUserToClientV2` (Assign User to Client v2) | Client Users | This endpoint allows you to assign users to a client within a specific tenant. · body |
| POST | `/api/v2/tenant/{tenantId}/client/{clientId}/bulk/users/assign` | `bulkAssignUsersToClient` (Bulk Assign Users to Client) | Client Users | Known Bug: This endpoint will not add or update a users classification level, even if Classification Tiers are enabled in your instance. · body |
| POST | `/api/v1/tenant/{tenantId}/client/{clientId}/user/remove` | `removeUserFromClient` (Remove User from Client) | Client Users | Revoke a user's authorization from a client · body |
| GET | `/api/v1/tenant/{tenantId}/client/list` | `listTenantClients` (List Tenant Clients) | - | List all clients of a given tenant |
| GET | `/api/v1/client/list` | `listClients` (List Clients) | - | This request retrieves all clients for a tenant that you are authorized to view. |
| POST | `/api/v2/clients` | `clientsListClients` (List Clients) | - | This request retrieves a list of all clients within a tenant. The body contains information on how to filter and sort the data to return. · body |
| GET | `/api/v1/client/{clientId}` | `getClient` (Get Client) | - | This request retrieves information on a client for a tenant that you are authorized to view. |
| POST | `/api/v1/client/create` | `createClient` (Create Client) | - | This request creates a new client within a tenant. · body |
| PUT | `/api/v1/client/{clientId}` | `updateClient` (Update Client) | - | This request updates an existing client within a tenant. · body |
| DELETE | `/api/v1/client/{clientId}` | `deleteClient` (Delete Client) | - | This request removes a client from a tenant. |
| POST | `/api/v1/client/{clientId}/logo` | `addClientLogo` (Add Client Logo) | - | This request creates a logo for a client. The file must be JPEG or PNG. · body |
| DELETE | `/api/v1/client/{clientId}/logo` | `deleteClientLogo` (Delete Client Logo) | - | This request removes a logo for a client. |
| POST | `/api/v2/client/{clientId}/findings` | `listClientFindings` (List Client Findings) | - | This request retrieves all findings for a specific client. The specific finding info returned is a truncated version of the full finding info. Sorting and filters can be added to the request body. · body |
| POST | `/api/v2/clients/{clientId}/assets` | `clientsListClientAssets` (List Client Assets) | - | This request retrieves assets associated with a specific client. · body |

## Files

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/api/v1/file-manager/artifacts` | `getArtifacts` (Get artifacts) | Artifacts | Return a list of filtered artifact files. · body |
| GET | `/api/v1/file-manager/artifacts/{artifactId}` | `downloadAnArtifact` (Download an artifact) | Artifacts |  |
| POST | `/api/v1/file-manager/upload` | `uploadAnArtifactFile` (Upload an artifact (file)) | Artifacts | Uploads a file to the tenant. These files live in a single location and are related to clients and reports through the relations attribute. Each file has a list of components or categorys it belongs t · body |
| DELETE | `/api/v1/file-manager/artifacts/{artifactId}` | `deleteAnArtifact` (Delete an artifact) | Artifacts | This request deletes an artifact from the tenant. |
| GET | `/api/v1/uploads/9bee9f28-7e25-4b4f-8b64-b520fc3c0b7c.png` | `getUploadByName` (Get Upload by Name) | - | This endpoint returns an inline image that was pasted in a rich text CKE field in the platform. |
| POST | `/api/v1/uploads` | `uploadImageToTenant` (Upload Image to Tenant) | - | body |

## Findings

This collection contains calls to manage Findings. It contains a folder Findings from Tools for endpoints related to third-party tools that are integrated with PlexTrac.

This collection has the following requests related to findings:

get findings based on parameters

list all findings for a tenant

list all findings for a specific report

get a specific finding

create a finding

update a finding for a report

delete a finding from a report

get status of a specific finding for a report

update status of a specific finding

get list of findings for s specific client

import list of findings for a specific client

Coming Soon:

copy a finding

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/api/v1/client/{clientId}/report/{reportId}/import/{source}` | `addFindingsFromFileImportsV1` (Add Findings from File Imports V1) | Findings From Tools V1 | DEPRECATED: Please use Findings from Tools - Streaming Upload · body |
| POST | `/api/v2/client/{clientId}/report/{reportId}/importAsync/{source}` | `addFindingsFromFileImportsV2` (Add Findings from File Imports V2) | Findings From Tools V2 | DEPRECATED: Please use Findings from Tools - Streaming Upload · body |
| POST | `/api/v2/presigned-url ` | `requestPresignedURL` (Request Presigned URL) | Findings from Tools - Streaming Upload | body |
| POST | `/api/v2/client/{clientId}/report/{reportId}/preuploaded-import/{source}` | `addFindingsAsyncFromPreuploadedFileImports` (Add Findings Async from Preuploaded File Imports) | Findings from Tools - Streaming Upload | body |
| GET | `/api/v2/my-imports` | `getImportStatus` (Get Import Status) | Findings from Tools - Streaming Upload | Import Status events have a lifetime of 1 hr. Once expired there are removed and will no longer be returned on this endpoint's response. |
| GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/scanoutput` | `evidenceGetScannerOutput` (Get Scanner Output) | Evidence |  |
| POST | `/api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence` | `bulkGetEvidence` (Bulk Get Evidence) | Evidence | Deprecated: Please use GET Get Scanner Output · body |
| PUT | `/api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/{assetId}/evidence/{evidenceId}` | `updateEvidence` (Update Evidence) | Evidence | This request updates evidence for a specific asset and finding. · body |
| PUT | `/api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence` | `bulkUpsertEvidence` (Bulk Upsert Evidence) | Evidence | This request inserts evidence information in bulk to an affected asset on a finding. This can either update existing evidence or create new evidence. · body |
| GET | `/api/v1/client/{clientId}/report/{reportId}/flaws` | `listReportFindings` (List Report Findings) | - | This request retrieves a list of findings for a specific report. |
| POST | `/api/v2/clients/{clientId}/reports/{reportId}/findings` | `getFindingsByReport` (Get Findings by Report) | - | Breaking Change Notification: · body |
| GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` | `getFinding` (Get Finding) | - | This request retrieves a specific finding from a report. |
| POST | `/api/v1/client/{clientId}/report/{reportId}/flaw/create` | `createFinding` (Create Finding) | - | This request creates a finding for a specific report. · body |
| PUT | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` | `updateFinding` (Update Finding) | - | This request updates a specific finding for a specific report. · body |
| PUT | `/api/v2/clients/{clientId}/reports/{reportId}/findings` | `bulkUpdateFindings` (Bulk Update Findings) | - | Bulk actions for updating findings. You can add tags, change the created at data or set the draft/published status with tthis endpoint. · body |
| PUT | `/api/v2/client/{clientId}/findings` | `bulkUpdateFindingsAssignUpdateStatus` (Bulk Update Findings - Assign / Update Status) | - | Bulk actions for updating findings. You can update the status, sub-status, and assinged user with this endpoint. · body |
| DELETE | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` | `deleteFinding` (Delete Finding) | - | This request deletes a specific finding from a specific report. |
| POST | `/api/v1/client/{clientId}/report/{reportId}/flaws/delete` | `bulkDeleteFindings` (Bulk Delete Findings) | - | This request enables a bulk deletion of findings from a report. · body |
| GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/status` | `getFindingStatusList` (Get Finding Status List) | - | This request retrieves the status of a specific finding from a report. |
| POST | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/status/update` | `createStatusUpdate` (Create Status Update) | - | This request updates the status of a specific finding from a report. · body |

## Integrations

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| GET | `/api/v2/tenant/{tenantId}/integrations/{product}` | `getIntegration` (Get Integration) | TenableIO |  |
| POST | `/api/v2/tenant/{tenantId}/integrations/{product}` | `saveIntegration` (Save Integration) | TenableIO | body |
| DELETE | `/api/v2/tenant/{tenantId}/integrations/{product}` | `deleteIntegration` (Delete Integration) | TenableIO |  |
| GET | `/api/v2/integrations/tenable-io/tags` | `tenableioGetTags` (TenableIO Get Tags) | TenableIO |  |
| GET | `/api/v2/integrations/tenable-io/tags/sync` | `tenableioSyncTags` (TenableIO Sync Tags) | TenableIO |  |
| GET | `/api/v1/jira/projects` | `listJiraProjects` (List Jira Projects) | Jira / Legacy Integration | This request retrieves a list of Jira projects that are used to associate a finding ticket to**.** |
| POST | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/createAndLinkJiraTicket` | `createAndLinkJiraTicketToFinding` (Create and Link Jira Ticket to Finding) | Jira / Legacy Integration | DEPRECATED: Will be removed in 2.14 · body |
| POST | `/api/v2/client/{clientId}/report/{reportId}/findings/createJiraTickets` | `bulkCreateAndLinkJiraTicketsToFindings` (Bulk Create and Link Jira Tickets to Findings) | Jira / Legacy Integration | DEPRECATED: Will be removed in 2.14 · body |
| POST | `/api/v2/jira/connect` | `createJiraConnection` (Create Jira Connection) | Jira | syncFrequency must one of following string value: · body |
| PUT | `/api/v2/jira/connect/{integrationId}` | `updateJiraConnection` (Update Jira Connection) | Jira | syncFrequency must one of following string value: · body |
| DELETE | `/api/v2/jira/connect/{integrationId}` | `deleteJiraConnection` (Delete Jira Connection) | Jira |  |
| POST | `/api/v2/jira/projects/{integrationId}` | `setJiraProjects` (Set Jira Projects) | Jira | mappingType must be one of following string value: · body |
| GET | `/api/v2/jira/integration/projects/{integrationId}` | `getJiraProjects` (Get Jira Projects) | Jira |  |
| GET | `/api/v2/jira/integration/{integrationId}/projects/{jiraProjectId}/issues/{jiraIssueTypeId}/mappings` | `getIssueMappingTypes` (Get Issue Mapping Types) | Jira |  |
| POST | `/api/v2/jira/integration/{integrationId}/projects/{jiraProjectId}/issues/{jiraIssueTypeId}/mappings/reset` | `resetIssueMappingTypes` (Reset Issue Mapping Types) | Jira |  |
| PUT | `/api/v2/jira/integration/{integrationId}/issues/bulk/mappings` | `bulkUpdateIssueTypeMappings` (Bulk Update Issue Type Mappings) | Jira | body |
| POST | `/api/v2/jira/integration/{integrationId}/issues/create` | `createJiraTicketFromFindings` (Create Jira Ticket From Findings) | Jira | body |
| DELETE | `/api/v2/jira/integration/unlink/client/{clientId}/report/{reportId}/finding/{findingId}` | `unlinkJiraTicketFromFindings` (Unlink Jira Ticket From Findings) | Jira |  |
| GET | `/api/v2/integrations/configurations` | `getConfigurations` (Get Configurations) | - |  |
| POST | `/api/v2/integrations/configurations` | `createConfigurations` (Create Configurations) | - | Creates a config for an integration. · body |
| GET | `/api/v2/integrations/configurations/{configId}` | `getConfiguration` (Get Configuration) | - | Creates a config for an integration. |
| PUT | `/api/v2/integrations/configurations/{configId}` | `updateConfiguration` (Update Configuration) | - | Creates a config for an integration. · body |
| DELETE | `/api/v2/integrations/configurations/{configId}` | `deleteConfiguration` (Delete Configuration) | - | Creates a config for an integration. |

## Mailer

Email Configuration Routes

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| GET | `/api/v2/tenants/{tenantId}/mailer/templates` | `getMailerTemplates` (Get Mailer Templates) | - | Get Mailer Templates |
| GET | `/api/v2/tenants/{tenantId}/mailer/templates/FORGOTTEN_PASSWORD` | `getEmailTemplate` (Get Email Template) | - | Get Email Template |
| PUT | `/api/v2/tenants/{tenantId}/mailer/templates/FORGOTTEN_PASSWORD` | `upsertEmailTemplate` (Upsert Email Template) | - | Upsert Email Template · body |

## Parser Actions

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/api/v1/tenant/{tenantId}/integrationconfig/parserConfig` | `enableDisableParserPluginActions` (Enable/Disable Parser Plugin Actions) | - | enable or disable global mapping of scanner findings to writeups · body |
| GET | `/api/v1/tenant/{tenantId}/actions` | `getTenantParsers` (Get Tenant Parsers) | - | This request retrieves a list of available parsers. |
| GET | `/api/v1/tenant/{tenantId}/actions/{parserName}` | `getTenantParserActions` (Get Tenant Parser Actions) | - | This request retrieves a list of parser actions for a tenant per identified parser source**.** |
| GET | `/api/v1/tenant/{tenantId}/actions/{parserName}/action/{actionId}` | `getTenantParserAction` (Get Tenant Parser Action) | - |  |
| POST | `/api/v1/tenant/{tenantId}/actions/{parserName}/action` | `createTenantParserAction` (Create Tenant Parser Action) | - | This request creates a parser action for a tenant. · body |
| PUT | `/api/v1/tenant/{tenantId}/actions/{parserName}/action/{actionId}` | `updateParserAction` (Update Parser Action) | - | This request updates a specific parser and specific action for a tenant. · body |
| PUT | `/api/v1/tenant/{tenantId}/actions/{parserName}/bulk` | `bulkUpdateTenantParserActions` (Bulk Update Tenant Parser Actions) | - | This request bulk updates a specific parser and specific action for a tenant. · body |
| POST | `/api/v1/tenant/{tenantId}/actions/upload/{source}` | `importParserPlugins` (Import Parser Plugins) | - | Used to import parser actions into a parser from a scan file. Scan files are imported directly to the parser and not into a report. · body |

## QA Workflow

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|

## Reports

The Reports module in PlexTrac streamlines the penetration test reporting process while improving the quality and value of security reports.

This collection contains a folder for Search & Replace functionality and the following requests related to reports:

list all reports for a client

list all reports for all clients

get a specific report

create a report for a client

update a report for a client

delete a report

get an exhibt from a report

upload a file to a report

export a report to .PTRAC

import findings to a report

Search & Replace folder:

retrieve a count of the number of times a value exists in a report

find and replace a value in a report

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/api/v1/search-replace/occurrences` | `searchReplaceInReportOccurrences` (Search & Replace in Report (Occurrences)) | Search & Replace | This request retrieves a count of the number of occurrences that exist in a report for a given query. This will not result in any changes of data but only return a numerical value. · body |
| POST | `/api/v1/search-replace` | `searchReplaceInReportReplace` (Search & Replace in Report (Replace)) | Search & Replace | This request finds and replaces a value in a report, such a report title, finding title, or field key. · body |
| GET | `/api/v1/client/{clientId}/reports` | `listClientReports` (List Client Reports) | - | This request retrieves a list of reports for a specific client. The information retrieved is limited and intended to provide an overview of the number of reports for a client. |
| POST | `/api/v2/reports` | `getReportList` (Get Report List) | - | This request retrieves a list of reports for a tenant. · body |
| GET | `/api/v1/client/{clientId}/report/{reportId}` | `getReport` (Get Report) | - | This request retrieves a specific report for a client and provides robust information about the report. |
| POST | `/api/v1/client/{clientId}/report/create` | `createReport` (Create Report) | - | This request creates a report for a client. · body |
| PUT | `/api/v1/client/{clientId}/report/{reportId}` | `updateReport` (Update Report) | - | This request updates a report. This does not update/relate to the findings on a report. · body |
| DELETE | `/api/v1/client/{clientId}/report/{reportId}` | `deleteReport` (Delete Report) | - | This request removes a report for a client. |
| POST | `/api/v2/reports/bulk/delete` | `bulkDeleteReports` (Bulk Delete Reports) | - | body |
| GET | `/api/v1/client/{clientId}/report/{reportId}/{exhibitId}` | `getExhibit` (Get Exhibit) | - | This request retrieves an exhibit filename from a specific report. |
| POST | `/api/v2/reports/bulk/tags` | `bulkAddTagsToReport` (Bulk Add Tags to Report) | - | body |
| POST | `/api/v2/reports/bulk/reviewers` | `bulkAssignReviewersToReport` (Bulk Assign Reviewers to Report) | - | The reviewer email must match an existing PT user email. · body |
| POST | `/api/v2/reports/bulk/status` | `bulkAdjustStatusOfReport` (Bulk Adjust Status of Report) | - | The reviewer email must match an existing PT user email. · body |
| GET | `/api/v1/client/{clientId}/report/{reportId}/export/ptrac` | `exportReportToPtrac` (Export Report to Ptrac) | - | This request exports a report in ptrac format for further manipulation and future importing back into PlexTrac. |
| GET | `/api/v1/client/{clientId}/report/{reportId}/export/doc` | `exportReportToWord` (Export Report to Word) | - | This requests exports a PlexTrac report to Word (.docx). |
| GET | `/api/v1/client/{clientId}/report/{reportId}/export/pdf` | `exportReportToPDF` (Export Report to PDF) | - | This requests exports a PlexTrac report to a PDF. |
| POST | `/api/v1/client/{clientId}/report/import` | `importPtracReport` (Import Ptrac Report) | - | body |

## Runbooks

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureOperatorListV2) | Runbooks v2 / Engagements / Engagement Procedures / Operators | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureOperatorsUpdateV2) | Runbooks v2 / Engagements / Engagement Procedures / Operators | Assign a user as an operator to a procedure in a RunbookV2 engagement. · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureAssetListV2) | Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureAssetsAddV2) | Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets | Add an existing asset to a procedure in a RunbookV2 engagement. · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureAssetCreateV2) | Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets | Create a new asset and add it to a procedure in a RunbookV2 engagement. · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureAssetDeleteV2) | Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureAssetUpdateV2) | Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureLogsV2) | Runbooks v2 / Engagements / Engagement Procedures / Procedure Logs | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureLogCreateV2) | Runbooks v2 / Engagements / Engagement Procedures / Procedure Logs | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureLogUpdateV2) | Runbooks v2 / Engagements / Engagement Procedures / Procedure Logs | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureLogDeleteV2) | Runbooks v2 / Engagements / Engagement Procedures / Procedure Logs | team can be one of "RED", "BLUE" · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureAttachmentListV2) | Runbooks v2 / Engagements / Engagement Procedures / Attachments | team can be one of "RED", "BLUE" · body |
| POST | `/api/v2/runbooks/engagement-procedures/{engagementProcedureId}/attachments/upload` | `uploadAttachmentToEngagementProcedure` (Upload Attachment to Engagement Procedure) | Runbooks v2 / Engagements / Engagement Procedures / Attachments | REST endpoint to upload attachments to a RunbooksV2 Engagment Procedure · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureAttachmentsUpdateV2) | Runbooks v2 / Engagements / Engagement Procedures / Attachments | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureAttachmentDeleteV2) | Runbooks v2 / Engagements / Engagement Procedures / Attachments | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureIdsV2) | Runbooks v2 / Engagements / Engagement Procedures | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureListV2) | Runbooks v2 / Engagements / Engagement Procedures | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureDetailV2) | Runbooks v2 / Engagements / Engagement Procedures | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureUpdateV2) | Runbooks v2 / Engagements / Engagement Procedures | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementProcedureDeleteV2) | Runbooks v2 / Engagements / Engagement Procedures | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementListV2) | Runbooks v2 / Engagements | Returns a list of RunbookV2 Engagements · body |
| POST | `/graphql` | `graphql` (RunbookEngagementDetailV2) | Runbooks v2 / Engagements | Returns the data for an In Progess Engagement · body |
| POST | `/graphql` | `graphql` (RunbookEngagementCreateV2) | Runbooks v2 / Engagements | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementUpdateV2) | Runbooks v2 / Engagements | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementDeleteV2) | Runbooks v2 / Engagements | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookEngagementFinishV2) | Runbooks v2 / Engagements | Submits a RunbookV2 Engagament and returns the ID of the created Report. · body |
| POST | `/graphql` | `graphql` (RunbookTestPlanListV2) | Runbooks v2 / Test Plans | Returns a list of RunbookV2 Test Plans · body |
| POST | `/graphql` | `graphql` (RunbookTestPlanDetailV2) | Runbooks v2 / Test Plans | Returns the data for a RunbooksV2 Test Plan and all Procedures it contains · body |
| POST | `/graphql` | `graphql` (RunbookTestPlanCreateV2) | Runbooks v2 / Test Plans | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookTestPlanUpdateV2) | Runbooks v2 / Test Plans | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookTestPlanDeleteV2) | Runbooks v2 / Test Plans | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookRepositoryAvailableUserListV2) | Runbooks v2 / RunbooksDB / Repositories / Users | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookRepositoryUsersV2) | Runbooks v2 / RunbooksDB / Repositories / Users | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookRepositoryUsersAddV2) | Runbooks v2 / RunbooksDB / Repositories / Users | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookRepositoryUserUpdateV2) | Runbooks v2 / RunbooksDB / Repositories / Users | Can update the permission of a user in the RunbookDB Repository. · body |
| POST | `/graphql` | `graphql` (RunbookRepositoryUserRemoveV2) | Runbooks v2 / RunbooksDB / Repositories / Users | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookRepositoryListV2) | Runbooks v2 / RunbooksDB / Repositories | Returns a list of all Repositories in the RunbooksDB · body |
| POST | `/graphql` | `graphql` (RunbookRepositoryDetailV2) | Runbooks v2 / RunbooksDB / Repositories | Returns the data for a RunbooksV2 Repository and a list of Procedures it contains · body |
| POST | `/graphql` | `graphql` (RunbookRepositoryCreateV2) | Runbooks v2 / RunbooksDB / Repositories | Create a RunbookDB Repository. · body |
| POST | `/graphql` | `graphql` (RunbookRepositoryUpdateV2) | Runbooks v2 / RunbooksDB / Repositories | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookRepositoryDeleteV2) | Runbooks v2 / RunbooksDB / Repositories | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookMethodologyListV2) | Runbooks v2 / RunbooksDB / Methodologies | Returns a list of Methodologies in the RunbooksDB · body |
| POST | `/graphql` | `graphql` (RunbookMethodologyDetailV2) | Runbooks v2 / RunbooksDB / Methodologies | Returns the data for a RunbooksV2 Methodology · body |
| POST | `/graphql` | `graphql` (RunbookMethodologyCreateV2) | Runbooks v2 / RunbooksDB / Methodologies | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookMethodologyUpdateV2) | Runbooks v2 / RunbooksDB / Methodologies | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookMethodologyDeleteV2) | Runbooks v2 / RunbooksDB / Methodologies | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookTacticListV2) | Runbooks v2 / RunbooksDB / Tactics | Returns a list of Tactics in the RunbooksDB · body |
| POST | `/graphql` | `graphql` (RunbookTacticDetailV2) | Runbooks v2 / RunbooksDB / Tactics | Returns the data for a RunbooksV2 Tactic · body |
| POST | `/graphql` | `graphql` (RunbookTacticCreateV2) | Runbooks v2 / RunbooksDB / Tactics | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookTacticUpdateV2) | Runbooks v2 / RunbooksDB / Tactics | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookTacticDeleteV2) | Runbooks v2 / RunbooksDB / Tactics | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookTechniqueListV2) | Runbooks v2 / RunbooksDB / Techniques | StartFragment · body |
| POST | `/graphql` | `graphql` (RunbookTechniqueDetailV2) | Runbooks v2 / RunbooksDB / Techniques | Returns the data for a RunbooksV2 Technique · body |
| POST | `/graphql` | `graphql` (RunbookTechniqueCreateV2) | Runbooks v2 / RunbooksDB / Techniques | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookTechniqueUpdateV2) | Runbooks v2 / RunbooksDB / Techniques | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookTechniqueDeleteV2) | Runbooks v2 / RunbooksDB / Techniques | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookProcedureListV2) | Runbooks v2 / RunbooksDB / Procedures | Returns a list of Procedures in the RunbooksDB · body |
| POST | `/graphql` | `graphql` (RunbookProcedureDetailV2) | Runbooks v2 / RunbooksDB / Procedures | Returns the data for a RunbooksV2 Procedure · body |
| POST | `/graphql` | `graphql` (RunbookProcedureCreateV2) | Runbooks v2 / RunbooksDB / Procedures | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookProcedureUpdateV2) | Runbooks v2 / RunbooksDB / Procedures | GraphQL operation; see graphql-operations.md · body |
| POST | `/graphql` | `graphql` (RunbookProcedureDeleteV2) | Runbooks v2 / RunbooksDB / Procedures | GraphQL operation; see graphql-operations.md · body |
| GET | `/api/v1/export/runbook/{runbookId}` | `exportRunbook` (Export Runbook) | - |  |
| POST | `/api/v1/import/runbook` | `importRunbook` (Import Runbook) | - |  |

## Scheduler

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/api/v2/engagement-schedule-artifacts` | `createEngagementScheduleEventArtifact` (Create Engagement Schedule Event Artifact) | Artifacts | Upload a file artifact to an existing Engagement Schedule Event. · body |
| GET | `/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/engagement-schedule-artifacts` | `getEngagementScheduleEventArtifacts` (Get Engagement Schedule Event Artifacts) | Artifacts | Get information about an existing file artifact on an Engagement Schedule Event. |
| PATCH | `/api/v2/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}` | `updateEngagementScheduleEventArtifact` (Update Engagement Schedule Event Artifact) | Artifacts | Updates a file artifact on an Engagement Schedule Event. · body |
| DELETE | `/api/v2/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}` | `deleteEngagementScheduleEventArtifact` (Delete Engagement Schedule Event Artifact) | Artifacts | Deletes a file artifact and removes its association with an Engagement Schedule Event. |
| GET | `/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}` | `downloadEngagementScheduleEventArtifact` (Download Engagement Schedule Event Artifact) | Artifacts |  |
| POST | `/api/v2/engagement-schedule-events/search` | `findManyEngagementScheduleEvents` (Find Many Engagement Schedule Events) | - | Get paginated multiple Engagement Schedule Events based on a filter. · body |
| GET | `/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}` | `getEngagementScheduleEventByID` (Get Engagement Schedule Event by ID) | - | Get an existing Engagement Schedule Event object. |
| POST | `/api/v2/engagement-schedule-events` | `createEngagementScheduleEvent` (Create Engagement Schedule Event) | - | Used to create a new Engagement Schedule Event. · body |
| POST | `/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/approve` | `approveEngagementScheduleEvent` (Approve Engagement Schedule Event) | - | Endpoint used in the process to create a new Engagement, or update an existing Engagement. · body |
| PATCH | `/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}` | `updateEngagementScheduleEvent` (Update Engagement Schedule Event) | - | Update any information on the scheduleEvent object. To update the assignedOperators or report, use POST Approve Engagement Schedule Event. · body |

## Substatus

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| GET | `/api/v3/substatus` | `listSubstatus` (List Substatus) | - |  |
| POST | `/api/v3/substatus` | `createSubstatus` (Create Substatus) | - | body |
| PATCH | `/api/v3/substatus/{substatusCuid}` | `updateSubstatus` (Update Substatus) | - | body |
| DELETE | `/api/v3/substatus/{substatusCuid}` | `deleteSubstatus` (Delete Substatus) | - |  |

## Templates

Please see our public docs for more information about how different Templates work together when exporting a report.

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| GET | `/api/v1/tenant/{tenantId}/report-templates` | `listReportTemplates` (List Report Templates) | Report Templates | This request lists all report templates for a tenant. |
| GET | `/api/v1/tenant/{tenantId}/report-template/{reportTemplateId}` | `getReportTemplate` (Get Report Template) | Report Templates | This request retrieves a specific report template within a tenant. |
| PUT | `/api/v1/tenant/{tenantId}/report-template` | `createReportTemplate` (Create Report Template) | Report Templates | This request creates a report template within a tenant. · body |
| PUT | `/api/v1/tenant/{tenantId}/report-template/{reportTemplateId}` | `updateReportTemplate` (Update Report Template) | Report Templates | This request updates a report template within a tenant. · body |
| DELETE | `/api/v1/tenant/{tenantId}/report-template/{reportTemplateId}` | `deleteReportTemplate` (Delete Report Template) | Report Templates |  |
| GET | `/api/v1/field-templates` | `listFindingsTemplates` (List Findings Templates) | Findings Templates/Layouts | This request lists all findings templates for a tenant. |
| GET | `/api/v1/field-template/{findingTemplateId}` | `getFindingsTemplate` (Get Findings Template) | Findings Templates/Layouts | This request retrieves a findings template |
| PUT | `/api/v1/tenant/{tenantId}/field-template` | `createFindingTemplate` (Create Finding Template) | Findings Templates/Layouts | This request creates a findings template within a tenant. · body |
| PUT | `/api/v1/tenant/{tenantId}/field-template/{findingTemplateId}` | `updateFindingTemplate` (Update Finding Template) | Findings Templates/Layouts | Update a finding template in your tenancy · body |
| DELETE | `/api/v1/tenant/{tenantId}/field-template/{findingTemplateId}` | `deleteFindingTemplate` (Delete Finding Template) | Findings Templates/Layouts |  |
| GET | `/api/v2/tenant/{tenantId}/export-templates` | `listExportTemplates` (List Export Templates) | Export Templates | Returns a list of all Export Templates in the tenant. |
| GET | `/api/v1/tenant/{tenantId}/export-template/{exportTemplateId}` | `getExportTemplate` (Get Export Template) | Export Templates | Returns the file binary of the .docx file of the Export Template. |
| POST | `/api/v1/tenant/{tenantId}/template/import` | `importExportTemplate` (Import Export Template) | Export Templates | Imports a file with Jinja code into the platform as an export template. You can add files for either a Word (.docx) or PDF (.j2) template. Files must be uploaded from you file system and have one of t · body |
| DELETE | `/api/v1/tenant/{tenantId}/template/{exportTemplateId}` | `deleteExportTemplate` (Delete Export Template) | Export Templates |  |

## Tenant

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| PUT | `/api/v2/tenants/{tenantId}/settings` | `updateSettings` (Update settings) | Settings | body |
| GET | `/api/v1/tenant/{tenantId}` | `getTenant` (Get Tenant) | - | This request obtains information about a tenant, such as ID, settings, point of contact information, etc. |
| PUT | `/api/v1/tenant/{tenantId}` | `updateTenant` (Update Tenant) | - | Update the details of your tenant, including name, address, and point of contact |
| GET | `/api/v1/tenant/{tenantId}/notificationsettings` | `getNotificationSettings` (Get Notification Settings) | - | This request retrieves the number of days to wait before reminding users to provide status updates on assigned findings. |
| PUT | `/api/v1/tenant/{tenantId}/notificationsettings` | `updateNotificationSettings` (Update Notification Settings) | - | Update the number of days to wait before reminding users to provide status updates on findings assigned to them |
| GET | `/api/v1/tenant/{tenantId}/analytics` | `tenantAnalytics` (Tenant Analytics) | - | This request retrieves analytics for a tenant, providing a total count of findings by risk and status. |
| POST | `/api/v1/tenant/{tenantId}/logo` | `addTenantLogo` (Add Tenant Logo) | - | Add a logo for your tenancy · body |
| POST | `/api/v1/tenant/{tenantId}/logo/dark` | `addTenantLogoDark` (Add Tenant Logo Dark) | - | Add a logo for your tenancy · body |
| DELETE | `/api/v1/tenant/{tenantId}/logo` | `deleteTenantLogo` (Delete Tenant Logo) | - | Remove the logo from your tenancy. This action will result in the PlexTrac logo being displayed. |
| DELETE | `/api/v1/tenant/{tenantId}/logo/dark` | `deleteTenantLogoDark` (Delete Tenant Logo Dark) | - | Remove the logo from your tenancy. This action will result in the PlexTrac logo being displayed. |
| DELETE | `/api/v1/tenant/{tenantId}/icon` | `deleteTenantIcon` (Delete Tenant Icon) | - |  |
| DELETE | `/api/v1/tenant/{tenantId}/icon/dark` | `deleteTenantIconDark` (Delete Tenant Icon Dark) | - |  |
| GET | `/api/v1/` | `rootRequest` (Root Request) | - | Root request. You can determine that the instance is up and running if this request returns the following JSON |

## Users

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| GET | `/api/v1/user/whoami` | `getAuthenticatedUserV1` (Get Authenticated User v1) | - | This request retrieves information about the user executing the endpoint, such as name, admin status, role, tenant ID, user ID, etc. |
| GET | `/api/v2/whoami` | `getAuthenticatedUserV2` (Get Authenticated User v2) | - | This request retrieves user info about the currently authenticated user. |
| GET | `/api/v1/tenant/{tenantId}/user/list` | `listTenantUsers` (List Tenant Users) | - | This request retrieves a list of all users in a tenant. |
| GET | `/api/v2/tenants/{tenantId}/users` | `getTenantsUsers` (Get Tenants Users) | - | This request retrieves a paginated list of all users in a tenant. |
| POST | `/api/v1/tenant/{tenantId}/user/create` | `createUserDEPRECATED` (Create User (DEPRECATED)) | - | Create a new user in your tenant · body |
| POST | `/api/v1/tenant/{tenantId}/user/create/bulk` | `bulkCreateUser` (Bulk Create User) | - | Create new users in your tenant. · body |
| PUT | `/api/v1/user/update` | `updateUser` (Update User) | - | This request updates information about the user executing the endpoint. · body |
| DELETE | `/api/v2/user/delete` | `deleteUser` (Delete User) | - | This request deletes the user associated with the email sent in the payload. · body |
| PUT | `/api/v1/user/changepass` | `changePassword` (Change Password) | - | This request changes the password for the user making the request. You cannot change another users password. · body |
| POST | `/api/v1/user/forgotpass` | `forgotPassword` (Forgot Password) | - | This request sends a password recovery email to an existing user based on the email address provided in the query. · body |
| PUT | `/api/v1/tenant/{tenantId}/user/resetpass` | `resetUserPassword` (Reset User Password) | - | Send an email for a user to reset their password. · body |
| PUT | `/api/v1/user/mfa/token` | `setMFAToken` (Set MFA Token) | - | This request sets the multi-factor authentication token of the current authenticated user. |
| PUT | `/api/v1/user/mfa/token/disable` | `disableUserMFAToken` (Disable User MFA Token) | - | This request disables the multi-factor authentication token of the current authenticated user. |
| PUT | `/api/v1/tenant/{tenantId}/user/mfa/disable` | `disableOtherUserMFAToken` (Disable Other User MFA Token) | - | Disable MFA for an authorized user in your tenant · body |
| POST | `/api/v1/tenant/{tenantId}/user/toggledisabled` | `enableDisableUser` (Enable/Disable User) | - | Toggles the User Disabled switch shown in the Admin Dashboard > Users. This enables or disables a user from authenticating to the platform. · body |
| GET | `/api/v1/user/notifications` | `getUserNotifications` (Get User Notifications) | - | This request retrieves notifications for the current authenticated user. |
| PUT | `/api/v1/user/notifications` | `setUserNotificationsRead` (Set User Notifications Read) | - | Mark a notification as read by the user. · body |
| POST | `/api/v2/user/findings` | `getUserFindings` (Get User Findings) | - | This request retrieves a list of findings assigned to the user making the API call. · body |

## Graph QL Queries

There are no REST endpoints for the functions described below.

Note: For all GraphQL requests the Plextrac backend is looking for the auth header with only the token value and nothing else.

ex. The header "Authorization": "" works

The header "Authorization": "Bearer " does not work

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/graphql` | `graphql` (clientAsset) | - | GraphQL operation; see graphql-operations.md · body |

## Graph QL Mutations

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| POST | `/graphql` | `graphql` (FindingUpdate) | - | Update individual properties on a finding. · body |
| POST | `/graphql` | `graphql` (NarrativeUpdate) | - | You can create a new report narrative by passing in a new report narrative object with a new unique CUID value in the id property. · body |

## Webhooks

This folder outlines the webhooks that PlexTrac can send to external services. Unlike traditional API calls where you initiate the request, webhooks are server-initiated notifications that PlexTrac sends to a URL you provide when specific events occur. Each request within this folder represents a distinct webhook event type.

For security reasons, these webhook events contain only minimal information—typically just the affected object's ID and the event trigger itself. Therefore, after receiving any event, the first thing you'll generally want to do is retrieve the full object details from the PlexTrac application using our public API.

For each event, you'll find a sample JSON payload. This is the exact data structure our system will send to your designated listener URL. You can find more

| Method | Path | Operation | Folder | Notes |
|---|---|---|---|---|
| WEBHOOK | `WFAOnReportFindingCreationEdit` | `WFAOnReportFindingCreationEdit` (WFA: On Report Finding Creation/Edit) | Workflow Automations | This webhook event is triggered whenever a report finding is created or edited. This event should fire for any method of finding creation or editting, including findings pulled into a report from the  · body |
| WEBHOOK | `WFAOnReportCreationEdit` | `WFAOnReportCreationEdit` (WFA: On Report Creation/Edit) | Workflow Automations | This webhook event is triggered whenever a report is created or edited. This event should fire for any method of report creation or editting, including manual creation, submission of an Assessment/Run · body |
| WEBHOOK | `OnReportPublished` | `OnReportPublished` (On Report Published) | - | The ReportPublished webhook event is triggered whenever a report's status changes from any non-published state to Published. When this event fires, PlexTrac sends a POST request containing the event p · body |
| WEBHOOK | `OnReportFindingPublished` | `OnReportFindingPublished` (On Report Finding Published) | - | The FindingPublished webhook event triggers whenever a finding's status is moved to Published within PlexTrac. When this event fires, PlexTrac sends a POST request containing the event payload to your · body |
| WEBHOOK | `OnAssessmentSubmission` | `OnAssessmentSubmission` (On Assessment Submission) | - | The AssessmentSubmitted webhook event is triggered whenever an assessment is submitted to become a report. This process automatically generates a new report, where each assessment question is converte · body |
| WEBHOOK | `OnSchedulerEngagementSubmission` | `OnSchedulerEngagementSubmission` (On Scheduler Engagement Submission) | - | The SchedulerEngagementSubmitted webhook event triggers whenever a scheduled engagement is created within PlexTrac. This event typically signifies that an engagement has been finalized or confirmed vi · body |
