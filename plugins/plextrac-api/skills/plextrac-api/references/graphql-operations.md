# PlexTrac GraphQL operations

All go to `POST {instanceUrl}/graphql` with `Authorization: Bearer <JWT>` and a JSON body `{"query": "...", "variables": {...}}`.
Extracted from the official Postman collection on 2026-10-20 (63 operations). Response examples are trimmed.

## Contents

- Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Operators: `RunbookEngagementProcedureOperatorListV2`, `RunbookEngagementProcedureOperatorsUpdateV2`
- Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets: `RunbookEngagementProcedureAssetListV2`, `RunbookEngagementProcedureAssetsAddV2`, `RunbookEngagementProcedureAssetCreateV2`, `RunbookEngagementProcedureAssetDeleteV2`, `RunbookEngagementProcedureAssetUpdateV2`
- Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Procedure Logs: `RunbookEngagementProcedureLogsV2`, `RunbookEngagementProcedureLogCreateV2`, `RunbookEngagementProcedureLogUpdateV2`, `RunbookEngagementProcedureLogDeleteV2`
- Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Attachments: `RunbookEngagementProcedureAttachmentListV2`, `RunbookEngagementProcedureAttachmentsUpdateV2`, `RunbookEngagementProcedureAttachmentDeleteV2`
- Runbooks / Runbooks v2 / Engagements / Engagement Procedures: `RunbookEngagementProcedureIdsV2`, `RunbookEngagementProcedureListV2`, `RunbookEngagementProcedureDetailV2`, `RunbookEngagementProcedureUpdateV2`, `RunbookEngagementProcedureDeleteV2`
- Runbooks / Runbooks v2 / Engagements: `RunbookEngagementListV2`, `RunbookEngagementDetailV2`, `RunbookEngagementCreateV2`, `RunbookEngagementUpdateV2`, `RunbookEngagementDeleteV2`, `RunbookEngagementFinishV2`
- Runbooks / Runbooks v2 / Test Plans: `RunbookTestPlanListV2`, `RunbookTestPlanDetailV2`, `RunbookTestPlanCreateV2`, `RunbookTestPlanUpdateV2`, `RunbookTestPlanDeleteV2`
- Runbooks / Runbooks v2 / RunbooksDB / Repositories / Users: `RunbookRepositoryAvailableUserListV2`, `RunbookRepositoryUsersV2`, `RunbookRepositoryUsersAddV2`, `RunbookRepositoryUserUpdateV2`, `RunbookRepositoryUserRemoveV2`
- Runbooks / Runbooks v2 / RunbooksDB / Repositories: `RunbookRepositoryListV2`, `RunbookRepositoryDetailV2`, `RunbookRepositoryCreateV2`, `RunbookRepositoryUpdateV2`, `RunbookRepositoryDeleteV2`
- Runbooks / Runbooks v2 / RunbooksDB / Methodologies: `RunbookMethodologyListV2`, `RunbookMethodologyDetailV2`, `RunbookMethodologyCreateV2`, `RunbookMethodologyUpdateV2`, `RunbookMethodologyDeleteV2`
- Runbooks / Runbooks v2 / RunbooksDB / Tactics: `RunbookTacticListV2`, `RunbookTacticDetailV2`, `RunbookTacticCreateV2`, `RunbookTacticUpdateV2`, `RunbookTacticDeleteV2`
- Runbooks / Runbooks v2 / RunbooksDB / Techniques: `RunbookTechniqueListV2`, `RunbookTechniqueDetailV2`, `RunbookTechniqueCreateV2`, `RunbookTechniqueUpdateV2`, `RunbookTechniqueDeleteV2`
- Runbooks / Runbooks v2 / RunbooksDB / Procedures: `RunbookProcedureListV2`, `RunbookProcedureDetailV2`, `RunbookProcedureCreateV2`, `RunbookProcedureUpdateV2`, `RunbookProcedureDeleteV2`
- Graph QL Queries: `clientAsset`
- Graph QL Mutations: `FindingUpdate`, `NarrativeUpdate`

### RunbookEngagementProcedureOperatorListV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Operators

```graphql
query RunbookEngagementProcedureOperatorListV2($procedureId: ID!) {
  runbookEngagementProcedureOperatorListV2(procedureId: $procedureId) {
    ...RunbookEngagementProcedureOperatorV2Data
    __typename
  }
}

fragment RunbookEngagementProcedureOperatorV2Data on RunbookEngagementProcedureOperatorV2 {
  id
  userId
  team
  createdAt
  user {
    id
    fullName
    __typename
  }
  __typename
}

variables: {
    "procedureId": "clc0syuip005a0zo3cv3p87ic"
}
```

Response 200 (RunbookEngagementProcedureOperatorListV2):
```json
{
    "data": {
        "runbookEngagementProcedureOperatorListV2": [
            {
                "id": "clc0t8kxo004h0zpcd2eu3bhb",
                "userId": "905",
                "team": "RED",
                "createdAt": "2022-12-23T17:52:23.295Z",
                "user": {
                    "id": "905",
                    "fullName": "Red Test",
                    "__typename": "RunbookRepositoryUserData"
                },
                "__typename": "RunbookEngagementProcedureOperatorV2"
            },
            {
                "id": "clc0t8kxo004i0zpc58n9cgrc",
                "userId": "1333",
                "team": "BLUE",
                "createdAt": "2022-12-23T17:52:23.295Z",
                "user": {
                    "id": "1333",
                    "fullName": "Blue Test",
                    "__typename": "RunbookRepositoryUserData"
                },
                "__typename": "RunbookEngagementProcedureOperatorV2"
            }
        ]
    }
}
```

### RunbookEngagementProcedureOperatorsUpdateV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Operators

Assign a user as an operator to a procedure in a RunbookV2 engagement.

```graphql
mutation RunbookEngagementProcedureOperatorsUpdateV2($procedureId: ID!, $operators: [RunbookEngagementProcedureOperatorInputV2!]!) {
  runbookEngagementProcedureOperatorsUpdateV2(
    procedureId: $procedureId
    operators: $operators
  ) {
    ...RunbookEngagementProcedureOperatorV2Data
    __typename
  }
}

fragment RunbookEngagementProcedureOperatorV2Data on RunbookEngagementProcedureOperatorV2 {
  id
  userId
  team
  createdAt
  user {
    id
    fullName
    __typename
  }
  __typename
}

variables: {
    "procedureId": "clc0syuip005a0zo3cv3p87ic",
    "operators": [
        {
            "userId": "905",
            "team": "RED"
        },
        {
            "userId": "1333",
            "team": "BLUE"
        }
    ]
}
```

Response 200 (RunbookEngagementProcedureOperatorsUpdateV2):
```json
{
    "data": {
        "runbookEngagementProcedureOperatorsUpdateV2": [
            {
                "id": "clc0t8kxo004h0zpcd2eu3bhb",
                "userId": "905",
                "team": "RED",
                "createdAt": "2022-12-23T17:52:23.295Z",
                "user": {
                    "id": "905",
                    "fullName": "Red Test",
                    "__typename": "RunbookRepositoryUserData"
                },
                "__typename": "RunbookEngagementProcedureOperatorV2"
            },
            {
                "id": "clc0t8kxo004i0zpc58n9cgrc",
                "userId": "1333",
                "team": "BLUE",
                "createdAt": "2022-12-23T17:52:23.295Z",
                "user": {
                    "id": "1333",
                    "fullName": "Blue Test",
                    "__typename": "RunbookRepositoryUserData"
                },
                "__typename": "RunbookEngagementProcedureOperatorV2"
            }
        ]
    }
}
```

### RunbookEngagementProcedureAssetListV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets

```graphql
query RunbookEngagementProcedureAssetListV2($procedureId: ID!) {
  runbookEngagementProcedureAssetListV2(procedureId: $procedureId) {
    ...RunbookEngagementProcedureAssetDataV2
    __typename
  }
}

fragment RunbookEngagementProcedureAssetDataV2 on RunbookEngagementProcedureAssetV2 {
  id
  includeInFinding
  outcomeBlue
  outcomeRed
  clientAsset {
    ...ClientAssetDataV2
    __typename
  }
  evidences {
    ...RunbookEngagementProcedureAssetEvidenceDataV2
    __typename
  }
  __typename
}

fragment ClientAssetDataV2 on ClientAssetV2 {
  id
  name
  parentAssetId
  parentAsset {
    id
    name
    __typename
  }
  type
  criticality
  knownIps
  tags
  __typename
}

fragment RunbookEngagementProcedureAssetEvidenceDataV2 on RunbookEngagementProcedureAssetEvidenceV2 {
  id
  title
  description
  __typename
}

variables: {
    "procedureId": "clc0syuip005a0zo3cv3p87ic"
}
```

Response 200 (RunbookEngagementProcedureAssetListV2):
```json
{
    "data": {
        "runbookEngagementProcedureAssetListV2": [
            {
                "id": "clc0tsb4j005f0zn55dd9f831",
                "includeInFinding": true,
                "outcomeBlue": "detectedAlerted",
                "outcomeRed": "partiallySuccessful",
                "clientAsset": {
                    "id": "8c5678c5-a52f-4d9a-b426-9bd7b89d7a23",
                    "name": "10.167.205.186",
                    "parentAssetId": null,
                    "parentAsset": null,
                    "type": null,
                    "criticality": null,
                    "knownIps": null,
                    "tags": [],
                    "__typename": "ClientAssetV2"
                },
                "evidences": [],
                "__typename": "RunbookEngagementProcedureAssetV2"
            }
        ]
    }
}
```

### RunbookEngagementProcedureAssetsAddV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets

Add an existing asset to a procedure in a RunbookV2 engagement.

```graphql
mutation RunbookEngagementProcedureAssetsAddV2($procedureId: ID!, $clientAssetIds: [ID!]!) {
  runbookEngagementProcedureAssetsAddV2(
    procedureId: $procedureId
    clientAssetIds: $clientAssetIds
  ) {
    ...RunbookEngagementProcedureAssetDataV2
    __typename
  }
}

fragment RunbookEngagementProcedureAssetDataV2 on RunbookEngagementProcedureAssetV2 {
  id
  includeInFinding
  outcomeBlue
  outcomeRed
  clientAsset {
    ...ClientAssetDataV2
    __typename
  }
  evidences {
    ...RunbookEngagementProcedureAssetEvidenceDataV2
    __typename
  }
  __typename
}

fragment ClientAssetDataV2 on ClientAssetV2 {
  id
  name
  parentAssetId
  parentAsset {
    id
    name
    __typename
  }
  type
  criticality
  knownIps
  tags
  __typename
}

fragment RunbookEngagementProcedureAssetEvidenceDataV2 on RunbookEngagementProcedureAssetEvidenceV2 {
  id
  title
  description
  __typename
}

variables: {
    "procedureId": "claif919700130ymz4i8ufw3u",
    "clientAssetIds": [
        "c824ece7-cdc9-4c9d-bc11-68ce7e25ad72"
    ]
}
```

Response 200 (RunbookEngagementProcedureAssetsAddV2):
```json
{
    "data": {
        "runbookEngagementProcedureAssetsAddV2": [
            {
                "id": "clbwk3kv0001b0yo54ghtf6j3",
                "includeInFinding": false,
                "outcomeBlue": null,
                "outcomeRed": null,
                "clientAsset": {
                    "id": "c824ece7-cdc9-4c9d-bc11-68ce7e25ad72",
                    "name": "Asset test",
                    "parentAssetId": "e37729c5-6e0e-4d34-bc02-3c7e8cb59948",
                    "parentAsset": {
                        "id": "e37729c5-6e0e-4d34-bc02-3c7e8cb59948",
                        "name": "Asset Name",
                        "__typename": "ClientAssetV2"
                    },
                    "type": "Server",
                    "criticality": "Critical",
                    "knownIps": [
                        "1.1.1.1"
                    ],
                    "tags": [
                        "asset_tag"
                    ],
                    "__typename": "ClientAssetV2"
                },
                "evidences": [],
                "__typename": "RunbookEngagementProcedureAssetV2"
            }
        ]
    }
}
```

Response 200 (ERR - Asset already exists on procedure):
```json
{
    "errors": [
        {
            "message": "duplicate key value violates unique constraint \"runbook_engagement_procedure_asset_engagement_procedure_id_clie\"",
            "locations": [
                {
                    "line": 2,
                    "column": 3
                }
            ],
            "path": [
                "runbookEngagementProcedureAssetsAddV2"
            ],
            "extensions": {
                "code": "INTERNAL_SERVER_ERROR",
                "exception": {
                    "length": 415,
                    "name": "error",
                    "severity": "ERROR",
                    "code": "23505",
                    "detail": "Key (engagement_procedure_id, client_asset_id)=(claif919700130ymz4i8ufw3u, c824ece7-cdc9-4c9d-bc11-68ce7e25ad72) already exists.",
                    "schema": "public",
                    "table": "runbook_engagement_procedure_asset",
                    "constraint": "runbook_engagement_procedure_asset_engagement_procedure_id_clie",
                    "file": "nbtinsert.c",
                    "line": "663",
                    "routine": "_bt_check_unique"
                }
            }
        }
    ],
    "data": null
}
```

### RunbookEngagementProcedureAssetCreateV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets

Create a new asset and add it to a procedure in a RunbookV2 engagement.

```graphql
mutation RunbookEngagementProcedureAssetCreateV2($procedureId: ID!, $clientAsset: ClientAssetCreateInputV2!, $evidences: [RunbookEngagementProcedureAssetEvidenceCreateInputV2!]) {
  runbookEngagementProcedureAssetCreateV2(
    procedureId: $procedureId
    clientAsset: $clientAsset
    evidences: $evidences
  ) {
    ...RunbookEngagementProcedureAssetDataV2
    __typename
  }
}

fragment RunbookEngagementProcedureAssetDataV2 on RunbookEngagementProcedureAssetV2 {
  id
  includeInFinding
  outcomeBlue
  outcomeRed
  clientAsset {
    ...ClientAssetDataV2
    __typename
  }
  evidences {
    ...RunbookEngagementProcedureAssetEvidenceDataV2
    __typename
  }
  __typename
}

fragment ClientAssetDataV2 on ClientAssetV2 {
  id
  name
  parentAssetId
  parentAsset {
    id
    name
    __typename
  }
  type
  criticality
  knownIps
  tags
  __typename
}

fragment RunbookEngagementProcedureAssetEvidenceDataV2 on RunbookEngagementProcedureAssetEvidenceV2 {
  id
  title
  description
  __typename
}

variables: {
    "procedureId": "claif919700130ymz4i8ufw3u",
    "clientAsset": {
        "name": "Test Asset",
        "parentAssetId": "00f5b383-954c-4b90-8db8-192f5342a54a",
        "type": "Workstation",
        "criticality": "High",
        "knownIps": [
            "52.52.52.52"
        ],
        "tags": [
            "asset_tag"
        ]
    },
    "evidences": [
        {
            "title": "Evidence Title",
            "description": "This is the description of my evidence."
        }
    ]
}
```

Response 200 (RunbookEngagementProcedureAssetCreateV2):
```json
{
    "data": {
        "runbookEngagementProcedureAssetCreateV2": {
            "id": "clbwjvcjz000s0ztbbel470x9",
            "includeInFinding": false,
            "outcomeBlue": null,
            "outcomeRed": null,
            "clientAsset": {
                "id": "77e29357-b872-4af2-96b1-de98619753a5",
                "name": "Test Asset",
                "parentAssetId": "00f5b383-954c-4b90-8db8-192f5342a54a",
                "parentAsset": {
                    "id": "00f5b383-954c-4b90-8db8-192f5342a54a",
                    "name": "192.168.240.30",
                    "__typename": "ClientAssetV2"
                },
                "type": "Workstation",
                "criticality": "High",
                "knownIps": [
                    "52.52.52.52"
                ],
                "tags": [
                    "asset_tag"
                ],
                "__typename": "ClientAssetV2"
            },
            "evidences": [
                {
                    "id": "clbwjvcl3000t0ztb8z1vaa4c",
                    "title": "Evidence Title",
                    "description": "This is the description of my evidence.",
                    "__typename": "RunbookEngagementProcedureAssetEvidenceV2"
                }
            ],
            "__typename": "RunbookEngagementProcedureAssetV2"
        }
    }
}
```

### RunbookEngagementProcedureAssetDeleteV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets

```graphql
mutation RunbookEngagementProcedureAssetDeleteV2($id: ID!, $procedureId: ID!) {
  runbookEngagementProcedureAssetDeleteV2(id: $id, procedureId: $procedureId)
}

variables: {
    "id": "clc0w6ami005g0zn57u3461wz",
    "procedureId": "clc0syuip005a0zo3cv3p87ic"
}
```

Response 200 (RunbookEngagementProcedureAssetDeleteV2):
```json
{
    "data": {
        "runbookEngagementProcedureAssetDeleteV2": true
    }
}
```

### RunbookEngagementProcedureAssetUpdateV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Targeted Assets

```graphql
mutation RunbookEngagementProcedureAssetUpdateV2($id: ID!, $procedureId: ID!, $clientAsset: ClientAssetUpdateInputV2, $evidences: RunbookEngagementProcedureAssetEvidencesInputV2, $input: RunbookEngagementProcedureAssetInputV2) {
  runbookEngagementProcedureAssetUpdateV2(
    id: $id
    procedureId: $procedureId
    clientAsset: $clientAsset
    evidences: $evidences
    input: $input
  ) {
    ...RunbookEngagementProcedureAssetDataV2
    __typename
  }
}

fragment RunbookEngagementProcedureAssetDataV2 on RunbookEngagementProcedureAssetV2 {
  id
  includeInFinding
  outcomeBlue
  outcomeRed
  clientAsset {
    ...ClientAssetDataV2
    __typename
  }
  evidences {
    ...RunbookEngagementProcedureAssetEvidenceDataV2
    __typename
  }
  __typename
}

fragment ClientAssetDataV2 on ClientAssetV2 {
  id
  name
  parentAssetId
  parentAsset {
    id
    name
    __typename
  }
  type
  criticality
  knownIps
  tags
  __typename
}

fragment RunbookEngagementProcedureAssetEvidenceDataV2 on RunbookEngagementProcedureAssetEvidenceV2 {
  id
  title
  description
  __typename
}

variables: {
    "id": "clc0w90zt005h0zn5hkzw0lgg",
    "procedureId": "clc0syuip005a0zo3cv3p87ic",
    "clientAsset": {
        "type": "Workstation",
        "criticality": "Medium"
    }
}
```

Response 200 (RunbookEngagementProcedureAssetUpdateV2):
```json
{
    "data": {
        "runbookEngagementProcedureAssetUpdateV2": {
            "id": "clc0w90zt005h0zn5hkzw0lgg",
            "includeInFinding": false,
            "outcomeBlue": null,
            "outcomeRed": null,
            "clientAsset": {
                "id": "948d5220-f147-4a6b-bf59-a5d44f9ed5c2",
                "name": "249.82.85.239",
                "parentAssetId": null,
                "parentAsset": null,
                "type": "Workstation",
                "criticality": "Medium",
                "knownIps": null,
                "tags": [],
                "__typename": "ClientAssetV2"
            },
            "evidences": [],
            "__typename": "RunbookEngagementProcedureAssetV2"
        }
    }
}
```

### RunbookEngagementProcedureLogsV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Procedure Logs

```graphql
query RunbookEngagementProcedureLogsV2($engagementProcedureId: ID!) {
  runbookEngagementProcedureLogsV2(engagementProcedureId: $engagementProcedureId) {
    ...RunbookEngagementProcedureLogDataV2
    __typename
  }
}

fragment RunbookEngagementProcedureLogDataV2 on RunbookEngagementProcedureLogV2 {
  id
  engagementProcedureId
  text
  startDate
  endDate
  team
  __typename
}

variables: {
    "engagementProcedureId": "clc0syuip005a0zo3cv3p87ic"
}
```

Response 200 (RunbookEngagementProcedureLogsV2):
```json
{
    "data": {
        "runbookEngagementProcedureLogsV2": [
            {
                "id": "clc0t6ktk005d0zn59i9x92gh",
                "engagementProcedureId": "clc0syuip005a0zo3cv3p87ic",
                "text": "<p>Red team procedure logs</p>",
                "startDate": "2022-12-23T17:49:50.000Z",
                "endDate": null,
                "team": "RED",
                "__typename": "RunbookEngagementProcedureLogV2"
            },
            {
                "id": "clc0t6nr7005e0zn5et2s3n0g",
                "engagementProcedureId": "clc0syuip005a0zo3cv3p87ic",
                "text": "<p>Blue team procedure logs</p>",
                "startDate": "2022-12-23T17:49:50.000Z",
                "endDate": null,
                "team": "BLUE",
                "__typename": "RunbookEngagementProcedureLogV2"
            }
        ]
    }
}
```

### RunbookEngagementProcedureLogCreateV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Procedure Logs

```graphql
mutation RunbookEngagementProcedureLogCreateV2($engagementProcedureId: ID!, $input: RunbookEngagementProcedureLogCreateInputV2!) {
  runbookEngagementProcedureLogCreateV2(
    engagementProcedureId: $engagementProcedureId
    input: $input
  ) {
    ...RunbookEngagementProcedureLogDataV2
    __typename
  }
}

fragment RunbookEngagementProcedureLogDataV2 on RunbookEngagementProcedureLogV2 {
  id
  engagementProcedureId
  text
  startDate
  endDate
  team
  __typename
}

variables: {
    "engagementProcedureId": "clc0syuip005a0zo3cv3p87ic",
    "input": {
        "text": "<p>new red team procedure log</p>",
        "startDate": "2022-12-23T12:16:33-07:00",
        "endDate": "2022-12-23T12:45:19-07:00",
        "team": "RED"
    }
}
```

Response 200 (RunbookEngagementProcedureLogCreateV2):
```json
{
    "data": {
        "runbookEngagementProcedureLogCreateV2": {
            "id": "clc0xc94y005h0zo3ei91g5n7",
            "engagementProcedureId": "clc0syuip005a0zo3cv3p87ic",
            "text": "<p>new red team procedure log</p>",
            "startDate": "2022-12-23T19:16:33.000Z",
            "endDate": "2022-12-23T19:45:19.000Z",
            "team": "RED",
            "__typename": "RunbookEngagementProcedureLogV2"
        }
    }
}
```

### RunbookEngagementProcedureLogUpdateV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Procedure Logs

```graphql
mutation RunbookEngagementProcedureLogUpdateV2($id: ID!, $input: RunbookEngagementProcedureLogUpdateInputV2!) {
  runbookEngagementProcedureLogUpdateV2(id: $id, input: $input) {
    ...RunbookEngagementProcedureLogDataV2
    __typename
  }
}

fragment RunbookEngagementProcedureLogDataV2 on RunbookEngagementProcedureLogV2 {
  id
  engagementProcedureId
  text
  startDate
  endDate
  team
  __typename
}

variables: {
    "id": "clc0xa56n005g0zo3g3xucdra",
    "input": {
        "text": "<p>updated red team procedure log</p>",
        "startDate": "2022-12-23T12:16:33-07:00",
        "endDate": "2022-12-23T12:45:19-07:00"
    }
}
```

Response 200 (RunbookEngagementProcedureLogUpdateV2):
```json
{
    "data": {
        "runbookEngagementProcedureLogUpdateV2": {
            "id": "clc0xa56n005g0zo3g3xucdra",
            "engagementProcedureId": "clc0syuip005a0zo3cv3p87ic",
            "text": "<p>updated red team procedure log</p>",
            "startDate": "2022-12-23T19:16:33.000Z",
            "endDate": "2022-12-23T19:45:19.000Z",
            "team": "RED",
            "__typename": "RunbookEngagementProcedureLogV2"
        }
    }
}
```

### RunbookEngagementProcedureLogDeleteV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Procedure Logs

team can be one of "RED", "BLUE"

```graphql
mutation RunbookEngagementProcedureLogDeleteV2($id: ID!) {
  runbookEngagementProcedureLogDeleteV2(id: $id) {
    ...RunbookEngagementProcedureLogDataV2
    __typename
  }
}

fragment RunbookEngagementProcedureLogDataV2 on RunbookEngagementProcedureLogV2 {
  id
  engagementProcedureId
  text
  startDate
  endDate
  team
  __typename
}

variables: {
    "id": "clc0xa56n005g0zo3g3xucdra"
}
```

Response 200 (RunbookEngagementProcedureLogDeleteV2):
```json
{
    "data": {
        "runbookEngagementProcedureLogDeleteV2": {
            "id": "clc0xa56n005g0zo3g3xucdra",
            "engagementProcedureId": "clc0syuip005a0zo3cv3p87ic",
            "text": "<p>updated red team procedure log</p>",
            "startDate": "2022-12-23T19:16:33.000Z",
            "endDate": "2022-12-23T19:45:19.000Z",
            "team": "RED",
            "__typename": "RunbookEngagementProcedureLogV2"
        }
    }
}
```

### RunbookEngagementProcedureAttachmentListV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Attachments

team can be one of "RED", "BLUE"

```graphql
query RunbookEngagementProcedureAttachmentListV2($procedureId: ID!, $team: Team!) {
  runbookEngagementProcedureAttachmentListV2(
    procedureId: $procedureId
    team: $team
  ) {
    ...RunbookEngagementProcedureAttachmentDataV2
    __typename
  }
}

fragment RunbookEngagementProcedureAttachmentDataV2 on RunbookEngagementProcedureAttachmentV2 {
  id
  team
  title
  description
  includeInFinding
  filename
  downloadUrl
  __typename
}

variables: {
    "procedureId": "clc0syuip005a0zo3cv3p87ic",
    "team": "RED"
}
```

Response 200 (RunbookEngagementProcedureAttachmentListV2):
```json
{
    "data": {
        "runbookEngagementProcedureAttachmentListV2": [
            {
                "id": "b8a5a717-f738-46c3-b9cf-8532cf81feb0",
                "team": "RED",
                "title": "duck.png",
                "description": "image caption",
                "includeInFinding": true,
                "filename": "duck.png",
                "downloadUrl": "/api/v2/runbooks/engagement-procedures/clc0syuip005a0zo3cv3p87ic/attachments/b8a5a717-f738-46c3-b9cf-8532cf81feb0",
                "__typename": "RunbookEngagementProcedureAttachmentV2"
            }
        ]
    }
}
```

### RunbookEngagementProcedureAttachmentsUpdateV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Attachments

```graphql
mutation RunbookEngagementProcedureAttachmentsUpdateV2($procedureId: ID!, $attachments: [RunbookEngagementProcedureAttachmentInputV2!]!) {
  runbookEngagementProcedureAttachmentsUpdateV2(
    procedureId: $procedureId
    input: $attachments
  ) {
    id
    title
    description
    includeInFinding
    __typename
  }
}

variables: {
    "procedureId": "clc0syuip005a0zo3cv3p87ic",
    "attachments": [
        {
            "id": "28df74b4-d560-4233-840f-6b074e5fe6d1",
            "title": "My Duck",
            "description": "updated caption"
        }
    ]
}
```

Response 200 (RunbookEngagementProcedureAttachmentsUpdateV2):
```json
{
    "data": {
        "runbookEngagementProcedureAttachmentsUpdateV2": [
            {
                "id": "28df74b4-d560-4233-840f-6b074e5fe6d1",
                "title": "My Duck",
                "description": "updated caption",
                "includeInFinding": false,
                "__typename": "RunbookEngagementProcedureAttachmentV2"
            }
        ]
    }
}
```

### RunbookEngagementProcedureAttachmentDeleteV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures / Attachments

```graphql
mutation RunbookEngagementProcedureAttachmentDeleteV2($procedureId: ID!, $id: ID!) {
  runbookEngagementProcedureAttachmentDeleteV2(procedureId: $procedureId, id: $id)
}

variables: {
    "id": "aa0c9a37-ede5-43e8-8e04-068b170344ef",
    "procedureId": "clc0syuip005a0zo3cv3p87ic"
}
```

Response 200 (RunbookEngagementProcedureAttachmentDeleteV2):
```json
{
    "data": {
        "runbookEngagementProcedureAttachmentDeleteV2": true
    }
}
```

### RunbookEngagementProcedureIdsV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures

```graphql
query RunbookEngagementProcedureIdsV2($engagementId: ID!) {
  runbookEngagementV2(id: $engagementId) {
    id
    title
    clientId
    procedureIds
    __typename
  }
}

variables: {
    "engagementId": "clc0syugl00570zo33lh6deiw"
}
```

Response 200 (RunbookEngagementProcedureIdsV2):
```json
{
    "data": {
        "runbookEngagementV2": {
            "id": "clc0syugl00570zo33lh6deiw",
            "title": "Purple Team Test Plan",
            "clientId": "1045",
            "procedureIds": [
                "clc0syuip005a0zo3cv3p87ic",
                "clc0syuip00590zo3ecjw3bl3",
                "clc0syuio00580zo330084s61"
            ],
            "__typename": "RunbookEngagementV2"
        }
    }
}
```

### RunbookEngagementProcedureListV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures

```graphql
query RunbookEngagementProcedureListV2($engagementId: ID!, $args: ListArgs!) {
  runbookEngagementProcedureListV2(engagementId: $engagementId, args: $args) {
    data {
      ...RunbookEngagementProcedureListDataV2
      __typename
    }
    meta {
      ...ListMetaData
      __typename
    }
    __typename
  }
}

fragment RunbookEngagementProcedureListDataV2 on RunbookEngagementProcedureV2 {
  id
  name
  shortName
  tenantId
  clientId
  engagementId
  procedureId
  description
  outcomeRed
  outcomeBlue
  status
  attackSource
  notesRed
  notesBlue
  findingSeverity
  runbookProcedure {
    id
    shortName
    __typename
  }
  __typename
}

fragment ListMetaData on ListMeta {
  pagination {
    limit
    offset
    total
    __typename
  }
  sort {
    by
    order
    __typename
  }
  filters {
    by
    value
    __typename
  }
  __typename
}

variables: {
    "engagementId": "clc0syugl00570zo33lh6deiw",
    "args": {
        "pagination": {
            "limit": 25,
            "offset": 0
        },
        "sort": [],
        "filters": [
            {
                "by": "searchTerm",
                "value": ""
            },
            {
                "by": "status",
                "value": []
            },
            {
                "by": "severity",
                "value": []
            }
        ]
    }
}
```

Response 200 (RunbookEngagementProcedureListV2):
```json
{
    "data": {
        "runbookEngagementProcedureListV2": {
            "data": [
                {
                    "id": "clc0syuip005a0zo3cv3p87ic",
                    "name": "File Extension Masquerading",
                    "shortName": "T1036.003",
                    "tenantId": 0,
                    "clientId": "1045",
                    "engagementId": "clc0syugl00570zo33lh6deiw",
                    "procedureId": "clacwm3r201x629mq2a1l1fae",
                    "description": "download and execute a file masquerading as images or Office files. Upon execution 3 calc instances and 3 vbs windows will be launched.\n\ne.g SOME_LEGIT_NAME.[doc,docx,xls,xlsx,pdf,rtf,png,jpg,etc.].[exe,vbs,js,ps1,etc] (Quartelyreport.docx.exe)\n\n\n**Supported Platforms:** windows\n\n**Inputs:**\n\n | Name | Description | Type | Default Value | \n | ---- | ----------- | ---- | ------------- | \n | exe_path | path to exe to use when creating masquerading files | Path | C:\\Windows\\System32\\calc.exe | \n | vbs_path | path of vbs to use when creating masquerading files | Path | PathToAtomicsFolder\\T1036.003\\src\\T1036.003_masquerading.vbs | \n | ps1_path | path of powershell script to use when creating masquerading files | Path | PathToAtomicsFolder\\T1036.003\\src\\T1036.003_masquerading.ps1 | ",
                    "outcomeRed": null,
                    "outcomeBlue": null,
                    "status": "NOT_STARTED",
                    "attackSource": null,
                    "notesRed": null,
                    "notesBlue": null,
                    "findingSeverity": null,
                    "runbookProcedure": {
                        "id": "clacwm3r201x629mq2a1l1fae",
                        "shortName": "T1036.003",
                        "__typename": "RunbookProcedureV2"
                    },
                    "__typename": "RunbookEngagementProcedureV2"
                },
                {
                    "id": "clc0syuip00590zo3ecjw3bl3",
                    "name": "Execute base64-encoded PowerShell from Windows Registry",
                    "shortName": "T1027",
                    "tenantId": 0,
                    "clientId": "1045",
                    "engagementId": "clc0syugl00570zo33lh6deiw",
                    "procedureId": "clacwm3ow01vc29mqeeab2jcq",
                    "description": "Stores base64-encoded PowerShell code in the Windows Registry and deobfuscates it for execution. This is used by numerous adversaries and malicious tools.\n\nUpon successful execution, powershell will execute encoded command and read/write from the registry.\n\n\n**Supported Platforms:** windows\n\n**Inputs:**\n\n | Name | Description | Type | Default Value | \n | ---- | ----------- | ---- | ------------- | \n | registry_key_storage | Windows Registry Key to store code | String | HKCU:Software\\Microsoft\\Windows\\CurrentVersion | \n | powershell_command | PowerShell command to encode | String | Write-Host \"Hey, Atomic!\" | \n | registry_entry_storage | Windows Registry entry to store code under key | String | Debug | ",
                    "outcomeRed": null,
                    "outcomeBlue": null,
                    "status": "NOT_STARTED",
                    "attackSource": null,
                    "notesRed": null,
                    "notesBlue": null,
                    "findingSeverity": null,
                    "runbookProcedure": {
                        "id": "clacwm3ow01vc29mqeeab2jcq",
                        "shortName": "T1027",
                        "__typename": "RunbookProcedureV2"
                    },
                    "__typename": "RunbookEngagementProcedureV2"
                },
                {
                    "id": "clc0syuio00580zo330084s61",
                    "name": "Dump LSASS.exe Memory using ProcDump",
                    "shortName": "T1003.001",
                    "tenantId": 0,
                    "clientId": "1045",
                    "engagementId": "clc0syugl00570zo33lh6deiw",
                    "procedureId": "clacwm35201d929mqfuncgxpm",
                    "description": "The memory of lsass.exe is often dumped for offline credential theft attacks. This can be achieved with Sysinternals\nProcDump.\n\nUpon successful execution, you should see the following file created c:\\windows\\temp\\lsass_dump.dmp.\n\nIf you see a message saying \"procdump.exe is not recognized as an internal or external command\", try using the  get-prereq_commands to download and install the ProcDump tool first.\n\n\n**Supported Platforms:** windows\n\n**Inputs:**\n\n | Name | Description | Type | Default Value | \n | ---- | ----------- | ---- | ------------- | \n | output_file | Path where resulting dump should be placed | Path | C:\\Windows\\Temp\\lsass_dump.dmp | \n | procdump_exe | Path of Procdump executable | Path | PathToAtomicsFolder\\T1003.001\\bin\\procdump.exe | ",
                    "outcomeRed": null,
                    "outcomeBlue": null,
                    "status": "NOT_STARTED",
                    "attackSource": null,
                    "notesRed": null,
                    "notesBlue": null,
                    "findingSeverity": null,
                    "runbookProcedure": {
                        "id": "clacwm35201d929mqfuncgxpm",
                        "shortName": "T1003.001",
                        "__typename": "RunbookProcedureV2"
                    },
                    "__typename": "RunbookEngagementProcedureV2"
                }
            ],
            "meta": {
                "pagination": {
                    "limit": 25,
                    "offset": 0,
                    "total": 3,
                    "__typename": "PaginationResult"
                },
                "sort": [],
                "filters": [
                    {
                        "by": "searchTerm",
                        "value": "",
                        "__typename": "FilterResult"
                    },
```

### RunbookEngagementProcedureDetailV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures

```graphql
query RunbookEngagementProcedureDetailV2($procedureId: ID!) {
  runbookEngagementProcedureV2(id: $procedureId) {
    ...RunbookEngagementProcedureDetailV2
    __typename
  }
}

fragment RunbookEngagementProcedureDetailV2 on RunbookEngagementProcedureV2 {
  id
  name
  shortName
  description
  status
  outcomeRed
  outcomeBlue
  notesRed
  notesBlue
  attackSource
  findingSeverity
  executionSteps {
    ...RunbookEngagementProcedureDetailExecutionStep
    __typename
  }
  runbookProcedure {
    ...RunbookEngagementProcedureDetailProcedureDataV2
    __typename
  }
  __typename
}

fragment RunbookEngagementProcedureDetailExecutionStep on RunbookEngagementProcedureExecutionStep {
  id
  description
  successCriteria
  isCompleted
  __typename
}

fragment RunbookEngagementProcedureDetailProcedureDataV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  repository {
    id
    name
    shortName
    __typename
  }
  techniques {
    ...RunbookEngagementProcedureDetailTechniqueDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  tactics {
    ...RunbookEngagementProcedureDetailTacticDataV2
    __typename
  }
  __typename
}

fragment RunbookEngagementProcedureDetailTechniqueDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  tactics {
    id
    name
    __typename
  }
  methodologies {
    id
    name
    __typename
  }
  __typename
}

fragment RunbookEngagementProcedureDetailTacticDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  methodologies {
    id
    name
    __typename
  }
  __typename
}

variables: {
    "procedureId": "clc0syuip005a0zo3cv3p87ic"
}
```

Response 200 (RunbookEngagementProcedureDetailV2):
```json
{
    "data": {
        "runbookEngagementProcedureV2": {
            "id": "clc0syuip005a0zo3cv3p87ic",
            "name": "File Extension Masquerading",
            "shortName": "T1036.003",
            "description": "download and execute a file masquerading as images or Office files. Upon execution 3 calc instances and 3 vbs windows...",
            "status": "IN_PROGRESS",
            "outcomeRed": "partiallySuccessful",
            "outcomeBlue": "detectedAlerted",
            "notesRed": "<p><strong>Red team notes</strong></p>",
            "notesBlue": "<p><strong>Blue team notes</strong></p>",
            "attackSource": "52.52.52.52",
            "findingSeverity": "Medium",
            "executionSteps": [
                {
                    "id": "clc0syuj7005c0zo3g5kffhfx",
                    "description": "copy #{exe_path} %temp%\\T1036.003_masquerading.docx.exe /Y\ncopy #{exe_path} %temp%\\T1036.003_masquerading.pdf.exe...",
                    "successCriteria": null,
                    "isCompleted": true,
                    "__typename": "RunbookEngagementProcedureExecutionStep"
                }
            ],
            "runbookProcedure": {
                "id": "clacwm3r201x629mq2a1l1fae",
                "name": "File Extension Masquerading",
                "shortName": "T1036.003",
                "description": "download and execute a file masquerading as images or Office files. Upon execution 3 calc instances and 3 vbs windows will...",
                "repository": {
                    "id": "clacwm17b000029mqcwg1etc9",
                    "name": "PlexTrac Curated",
                    "shortName": "PlexTrac",
                    "__typename": "RunbookRepositoryV2"
                },
                "techniques": [
                    {
                        "id": "clacwm6ku03ku29mqbfsldyom",
                        "name": "Rename System Utilities",
                        "shortName": "T1036.003",
                        "tactics": [
                            {
                                "id": "clacwm5oh02mf29mqf5andaw8",
                                "name": "Defense Evasion",
                                "__typename": "RunbookTacticV2"
                            }
                        ],
                        "methodologies": [
                            {
                                "id": "clacwm5nx02m229mqci14ckrd",
                                "name": "Mitre ATT&CK 11.3",
                                "__typename": "RunbookMethodologyV2"
                            }
                        ],
                        "__typename": "RunbookTechniqueV2"
                    }
                ],
                "tags": [],
                "tactics": [
                    {
                        "id": "clacwm193000829mq7bhlcnj1",
                        "name": "Defense Evasion",
                        "shortName": "TA0005",
                        "methodologies": [
                            {
                                "id": "clacwm17k000129mqhudqhx01",
                                "name": "Mitre ATT&CK 9.0",
                                "__typename": "RunbookMethodologyV2"
                            }
                        ],
                        "__typename": "RunbookTacticV2"
                    }
                ],
                "__typename": "RunbookProcedureV2"
            },
            "__typename": "RunbookEngagementProcedureV2"
        }
    }
}
```

### RunbookEngagementProcedureUpdateV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures

```graphql
mutation RunbookEngagementProcedureUpdateV2($id: ID!, $data: RunbookEngagementProcedureUpdateInputV2!, $executionSteps: RunbookEngagementProcedureExecutionStepsInputV2, $assets: [RunbookEngagementProcedureAssetUpdateInputV2!]!) {
  runbookEngagementProcedureUpdateV2(
    id: $id
    input: $data
    executionSteps: $executionSteps
  ) {
    id
    status
    outcomeRed
    outcomeBlue
    notesRed
    notesBlue
    attackSource
    findingSeverity
    executionSteps {
      ...RunbookEngagementProcedureDetailExecutionStep
      __typename
    }
    __typename
  }
  runbookEngagementProcedureAssetsUpdateV2(procedureId: $id, input: $assets) {
    id
    outcomeBlue
    outcomeRed
    __typename
  }
}

fragment RunbookEngagementProcedureDetailExecutionStep on RunbookEngagementProcedureExecutionStep {
  id
  description
  successCriteria
  isCompleted
  __typename
}

variables: {
    "id": "clc0syuip005a0zo3cv3p87ic",
    "data": {
        "status": "IN_PROGRESS",
        "attackSource": "52.52.52.52",
        "outcomeBlue": "detectedAlerted",
        "outcomeRed": "partiallySuccessful",
        "findingSeverity": "Medium",
        "notesBlue": "<p><strong>Blue team notes</strong></p>",
        "notesRed": "<p><strong>Red team notes</strong></p>"
    },
    "executionSteps": {
        "toUpdate": [
            {
                "id": "clc0syuj7005c0zo3g5kffhfx",
                "isCompleted": true
            }
        ]
    },
    "assets": []
}
```

Response 200 (RunbookEngagementProcedureUpdateV2):
```json
{
    "data": {
        "runbookEngagementProcedureUpdateV2": {
            "id": "clc0syuip005a0zo3cv3p87ic",
            "status": "IN_PROGRESS",
            "outcomeRed": "partiallySuccessful",
            "outcomeBlue": "detectedAlerted",
            "notesRed": "<p><strong>Red team notes</strong></p>",
            "notesBlue": "<p><strong>Blue team notes</strong></p>",
            "attackSource": "52.52.52.52",
            "findingSeverity": "Medium",
            "executionSteps": [
                {
                    "id": "clc0syuj7005c0zo3g5kffhfx",
                    "description": "copy #{exe_path} %temp%\\T1036.003_masquerading.docx.exe /Y\ncopy #{exe_path} %temp%\\T1036.003_masquerading.pdf.exe...",
                    "successCriteria": null,
                    "isCompleted": true,
                    "__typename": "RunbookEngagementProcedureExecutionStep"
                }
            ],
            "__typename": "RunbookEngagementProcedureV2"
        },
        "runbookEngagementProcedureAssetsUpdateV2": []
    }
}
```

### RunbookEngagementProcedureDeleteV2
Folder: Runbooks / Runbooks v2 / Engagements / Engagement Procedures

```graphql
mutation RunbookEngagementProcedureDeleteV2($id: ID!) {
  runbookEngagementProcedureDeleteV2(id: $id) {
    ...RunbookEngagementProcedureListDataV2
    __typename
  }
}

fragment RunbookEngagementProcedureListDataV2 on RunbookEngagementProcedureV2 {
  id
  name
  shortName
  tenantId
  clientId
  engagementId
  procedureId
  description
  outcomeRed
  outcomeBlue
  status
  attackSource
  notesRed
  notesBlue
  findingSeverity
  runbookProcedure {
    id
    shortName
    __typename
  }
  __typename
}

variables: {
    "id": "clc0syuip005a0zo3cv3p87ic"
}
```

Response 200 (RunbookEngagementProcedureDeleteV2):
```json
{
    "data": {
        "runbookEngagementProcedureDeleteV2": {
            "id": "clc0syuip005a0zo3cv3p87ic",
            "name": "File Extension Masquerading",
            "shortName": "T1036.003",
            "tenantId": 0,
            "clientId": "1045",
            "engagementId": "clc0syugl00570zo33lh6deiw",
            "procedureId": "clacwm3r201x629mq2a1l1fae",
            "description": "download and execute a file masquerading as images or Office files. Upon execution 3 calc instances and 3 vbs windows...",
            "outcomeRed": "partiallySuccessful",
            "outcomeBlue": "detectedAlerted",
            "status": "IN_PROGRESS",
            "attackSource": "52.52.52.52",
            "notesRed": "<p><strong>Red team notes</strong></p>",
            "notesBlue": "<p><strong>Blue team notes</strong></p>",
            "findingSeverity": "Medium",
            "runbookProcedure": {
                "id": "clacwm3r201x629mq2a1l1fae",
                "shortName": "T1036.003",
                "__typename": "RunbookProcedureV2"
            },
            "__typename": "RunbookEngagementProcedureV2"
        }
    }
}
```

### RunbookEngagementListV2
Folder: Runbooks / Runbooks v2 / Engagements

Returns a list of RunbookV2 Engagements

```graphql
query RunbookEngagementListV2($args: ListArgs!) {
    runbookEngagementListV2(args: $args) {
    data {
      ...RunbookEngagementListDataV2
      __typename
    }
    meta {
      ...ListMetaData
      __typename
    }
    __typename
  }
}

fragment RunbookEngagementListDataV2 on RunbookEngagementV2 {
  id
  title
  description
  status
  isCompleted
  updatedAt
  percentComplete
  reportId
  testPlan {
    id
    title
    __typename
  }
  client {
    id
    name
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment ListMetaData on ListMeta {
  pagination {
    limit
    offset
    total
    __typename
  }
  sort {
    by
    order
    __typename
  }
  filters {
    by
    value
    __typename
  }
  __typename
}

variables: {
    "args": {
        "pagination": {
            "limit": 25,
            "offset": 0
        },
        "sort": [],
        "filters": [
            {
                "by": "searchTerm",
                "value": ""
            },
            {
                "by": "status",
                "value": []
            },
            {
                "by": "clientIds",
                "value": []
            }
        ]
    }
}
```

Response 200 (runbookEngagementListV2):
```json
{
    "data": {
        "runbookEngagementListV2": {
            "data": [
                {
                    "id": "clbfcfaoy00jr0zpr4z7ihc0m",
                    "title": "Demo Runbook Test",
                    "description": "<p>demo</p>",
                    "status": "COMPLETED",
                    "isCompleted": true,
                    "updatedAt": "2022-12-08T17:22:13.078Z",
                    "percentComplete": 25,
                    "reportId": "500596",
                    "testPlan": null,
                    "client": {
                        "id": 1017,
                        "name": "Talan Test",
                        "__typename": "Client"
                    },
                    "tags": [],
                    "__typename": "RunbookEngagementV2"
                },
                {
                    "id": "claif918x000q0ymzcve08knk",
                    "title": "Purple Team Test Plan",
                    "description": null,
                    "status": "NOT_STARTED",
                    "isCompleted": false,
                    "updatedAt": "2022-11-15T16:21:16.308Z",
                    "percentComplete": 0,
                    "reportId": null,
                    "testPlan": {
                        "id": "clacwm5a402lo29mq9al0dmt6",
                        "title": "Purple Team Test Plan",
                        "__typename": "RunbookTestPlanV2"
                    },
                    "client": {
                        "id": 1065,
                        "name": "Green Testing",
                        "__typename": "Client"
                    },
                    "tags": [],
                    "__typename": "RunbookEngagementV2"
                }
            ],
            "meta": {
                "pagination": {
                    "limit": 25,
                    "offset": 0,
                    "total": 3,
                    "__typename": "PaginationResult"
                },
                "sort": [],
                "filters": [
                    {
                        "by": "searchTerm",
                        "value": "",
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "status",
                        "value": [],
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "clientIds",
                        "value": [],
                        "__typename": "FilterResult"
                    }
                ],
                "__typename": "ListMeta"
            },
            "__typename": "RunbookEngagementListV2"
        }
    }
}
```

### RunbookEngagementDetailV2
Folder: Runbooks / Runbooks v2 / Engagements

Returns the data for an In Progess Engagement

```graphql
query RunbookEngagementDetailV2($engagementId: ID!) {
  runbookEngagementV2(id: $engagementId) {
    ...RunbookEngagementDetailV2
    __typename
  }
}

fragment RunbookEngagementDetailV2 on RunbookEngagementV2 {
  id
  title
  description
  status
  isCompleted
  updatedAt
  percentComplete
  clientId
  testPlan {
    id
    title
    __typename
  }
  client {
    id
    name
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

variables: {
    "engagementId": "claif918x000q0ymzcve08knk"
}
```

Response 200 (RunbookEngagementDetailV2):
```json
{
    "data": {
        "runbookEngagementV2": {
            "id": "claif918x000q0ymzcve08knk",
            "title": "Purple Team Test Plan",
            "description": null,
            "status": "NOT_STARTED",
            "isCompleted": false,
            "updatedAt": "2022-11-15T16:21:16.308Z",
            "percentComplete": 0,
            "clientId": "1065",
            "testPlan": {
                "id": "clacwm5a402lo29mq9al0dmt6",
                "title": "Purple Team Test Plan",
                "__typename": "RunbookTestPlanV2"
            },
            "client": {
                "id": 1065,
                "name": "Green Testing",
                "__typename": "Client"
            },
            "tags": [],
            "__typename": "RunbookEngagementV2"
        }
    }
}
```

### RunbookEngagementCreateV2
Folder: Runbooks / Runbooks v2 / Engagements

```graphql
mutation RunbookEngagementCreateV2($data: RunbookEngagementCreateInputV2!, $procedureIds: [ID!], $tags: [String!]) {
  runbookEngagementCreateV2(
    input: $data
    procedureIds: $procedureIds
    tags: $tags
  ) {
    ...RunbookEngagementWizardFormV2
    __typename
  }
}

fragment RunbookEngagementWizardFormV2 on RunbookEngagementV2 {
  id
  title
  description
  updatedAt
  client {
    id
    name
    __typename
  }
  procedures {
    ...RunbookEngagementWizardFormProcedureV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookEngagementWizardFormProcedureV2 on RunbookEngagementProcedureV2 {
  id
  runbookProcedure {
    ...RunbookProcedureAssignmentListDataV2
    __typename
  }
  __typename
}

fragment RunbookProcedureAssignmentListDataV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  techniques {
    ...RunbookTechniqueAssignmentListDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookTechniqueAssignmentListDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  methodologies {
    id
    name
    shortName
    __typename
  }
  tactics {
    id
    name
    shortName
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

variables: {
    "data": {
        "title": "Purple Team Test Plan",
        "description": "<p>description</p>",
        "testPlanId": "clacwm5a402lo29mq9al0dmt6",
        "clientId": "1045"
    },
    "procedureIds": [
        "clacwm2sk013029mqgh8nap0q"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookEngagementCreateV2):
```json
{
    "data": {
        "runbookEngagementCreateV2": {
            "id": "clc6n8m6z008c0zn5dk8b9mij",
            "title": "Purple Team Test Plan",
            "description": "<p>description</p>",
            "updatedAt": "2022-12-27T19:51:04.324Z",
            "client": {
                "id": 1045,
                "name": "Green Testing",
                "__typename": "Client"
            },
            "procedures": [
                {
                    "id": "clc6n8m8u008d0zn5addaasge",
                    "runbookProcedure": {
                        "id": "clacwm2sk013029mqgh8nap0q",
                        "name": "DLL Search Order Hijacking - amsi.dll",
                        "shortName": "T1574.001",
                        "description": "Adversaries can take advantage of insecure library loading by PowerShell to load a vulnerable version of amsi.dll in order to bypass...",
                        "techniques": [
                            {
                                "id": "clacwm5xb02w629mqd0ju23rt",
                                "name": "DLL Search Order Hijacking",
                                "shortName": "T1574.001",
                                "description": "Adversaries may execute their own malicious payloads by hijacking the search order used to load DLLs. Windows systems use a common...",
                                "methodologies": [
                                    {
                                        "id": "clacwm5nx02m229mqci14ckrd",
                                        "name": "Mitre ATT&CK 11.3",
                                        "shortName": "Mitre-11.3",
                                        "__typename": "RunbookMethodologyV2"
                                    }
                                ],
                                "tactics": [
                                    {
                                        "id": "clacwm5ob02m929mq74gcc6ae",
                                        "name": "Persistence",
                                        "shortName": "TA0003",
                                        "__typename": "RunbookTacticV2"
                                    },
                                    {
                                        "id": "clacwm5od02mb29mqa5fz3l4q",
                                        "name": "Privilege Escalation",
                                        "shortName": "TA0004",
                                        "__typename": "RunbookTacticV2"
                                    }
                                ],
                                "tags": [],
                                "__typename": "RunbookTechniqueV2"
                            }
                        ],
                        "tags": [],
                        "__typename": "RunbookProcedureV2"
                    },
                    "__typename": "RunbookEngagementProcedureV2"
                }
            ],
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookEngagementV2"
        }
    }
}
```

### RunbookEngagementUpdateV2
Folder: Runbooks / Runbooks v2 / Engagements

```graphql
mutation RunbookEngagementUpdateV2($id: ID!, $data: RunbookEngagementUpdateInputV2!, $procedureIds: [ID!], $tags: [String!]) {
  runbookEngagementUpdateV2(
    id: $id
    input: $data
    procedureIds: $procedureIds
    tags: $tags
  ) {
    ...RunbookEngagementWizardFormV2
    __typename
  }
}

fragment RunbookEngagementWizardFormV2 on RunbookEngagementV2 {
  id
  title
  description
  updatedAt
  client {
    id
    name
    __typename
  }
  procedures {
    ...RunbookEngagementWizardFormProcedureV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookEngagementWizardFormProcedureV2 on RunbookEngagementProcedureV2 {
  id
  runbookProcedure {
    ...RunbookProcedureAssignmentListDataV2
    __typename
  }
  __typename
}

fragment RunbookProcedureAssignmentListDataV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  techniques {
    ...RunbookTechniqueAssignmentListDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookTechniqueAssignmentListDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  methodologies {
    id
    name
    shortName
    __typename
  }
  tactics {
    id
    name
    shortName
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

variables: {
    "id": "clc6n8m6z008c0zn5dk8b9mij",
    "data": {
        "title": "Purple Team Test Plan",
        "description": "<p>updated description</p>"
    },
    "procedureIds": [
        "clacwm2sk013029mqgh8nap0q"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookEngagementUpdateV2):
```json
{
    "data": {
        "runbookEngagementUpdateV2": {
            "id": "clc6n8m6z008c0zn5dk8b9mij",
            "title": "Purple Team Test Plan",
            "description": "<p>updated description</p>",
            "updatedAt": "2022-12-27T19:57:14.509Z",
            "client": {
                "id": 1045,
                "name": "Green Testing",
                "__typename": "Client"
            },
            "procedures": [
                {
                    "id": "clc6n8m8u008d0zn5addaasge",
                    "runbookProcedure": {
                        "id": "clacwm2sk013029mqgh8nap0q",
                        "name": "DLL Search Order Hijacking - amsi.dll",
                        "shortName": "T1574.001",
                        "description": "Adversaries can take advantage of insecure library loading by PowerShell to load a vulnerable version of amsi.dll in order...",
                        "techniques": [
                            {
                                "id": "clacwm5xb02w629mqd0ju23rt",
                                "name": "DLL Search Order Hijacking",
                                "shortName": "T1574.001",
                                "description": "Adversaries may execute their own malicious payloads by hijacking the search order used to load DLLs. Windows systems...",
                                "methodologies": [
                                    {
                                        "id": "clacwm5nx02m229mqci14ckrd",
                                        "name": "Mitre ATT&CK 11.3",
                                        "shortName": "Mitre-11.3",
                                        "__typename": "RunbookMethodologyV2"
                                    }
                                ],
                                "tactics": [
                                    {
                                        "id": "clacwm5ob02m929mq74gcc6ae",
                                        "name": "Persistence",
                                        "shortName": "TA0003",
                                        "__typename": "RunbookTacticV2"
                                    },
                                    {
                                        "id": "clacwm5od02mb29mqa5fz3l4q",
                                        "name": "Privilege Escalation",
                                        "shortName": "TA0004",
                                        "__typename": "RunbookTacticV2"
                                    }
                                ],
                                "tags": [],
                                "__typename": "RunbookTechniqueV2"
                            }
                        ],
                        "tags": [],
                        "__typename": "RunbookProcedureV2"
                    },
                    "__typename": "RunbookEngagementProcedureV2"
                }
            ],
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookEngagementV2"
        }
    }
}
```

Response 200 (ERR - Engagement to update is deleted):
```json
{
    "errors": [
        {
            "message": "Engagement clc6n62xu007u0zpcdcq099zk was deleted",
            "locations": [
                {
                    "line": 2,
                    "column": 3
                }
            ],
            "path": [
                "runbookEngagementUpdateV2"
            ],
            "extensions": {
                "code": "INTERNAL_SERVER_ERROR"
            }
        }
    ],
    "data": null
}
```

### RunbookEngagementDeleteV2
Folder: Runbooks / Runbooks v2 / Engagements

```graphql
mutation RunbookEngagementDeleteV2($id: ID!) {
  runbookEngagementDeleteV2(id: $id) {
    ...RunbookEngagementListDataV2
    __typename
  }
}

fragment RunbookEngagementListDataV2 on RunbookEngagementV2 {
  id
  title
  description
  status
  isCompleted
  updatedAt
  percentComplete
  reportId
  testPlan {
    id
    title
    __typename
  }
  client {
    id
    name
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

variables: {
    "id": "clc6n62xu007u0zpcdcq099zk"
}
```

Response 200 (RunbookEngagementDeleteV2):
```json
{
    "data": {
        "runbookEngagementDeleteV2": {
            "id": "clc6n62xu007u0zpcdcq099zk",
            "title": "Purple Team Test Plan",
            "description": "<p>description</p>",
            "status": "NOT_STARTED",
            "isCompleted": false,
            "updatedAt": "2022-12-27T19:49:06.065Z",
            "percentComplete": 0,
            "reportId": null,
            "testPlan": {
                "id": "clacwm5a402lo29mq9al0dmt6",
                "title": "Purple Team Test Plan",
                "__typename": "RunbookTestPlanV2"
            },
            "client": {
                "id": 1045,
                "name": "Green Testing",
                "__typename": "Client"
            },
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookEngagementV2"
        }
    }
}
```

### RunbookEngagementFinishV2
Folder: Runbooks / Runbooks v2 / Engagements

Submits a RunbookV2 Engagament and returns the ID of the created Report.

```graphql
mutation RunbookEngagementFinishV2($id: ID!) {
  runbookEngagementFinishV2(id: $id)
}

variables: {
    "id": "clc6nm94f00990zo38lj769d6"
}
```

Response 200 (RunbookEngagementFinishV2):
```json
{
    "data": {
        "runbookEngagementFinishV2": "500670"
    }
}
```

### RunbookTestPlanListV2
Folder: Runbooks / Runbooks v2 / Test Plans

Returns a list of RunbookV2 Test Plans

```graphql
query RunbookTestPlanListV2($args: ListArgs!) {
  runbookTestPlanListV2(args: $args) {
    data {
      ...RunbookTestPlanListDataV2
      __typename
    }
    meta {
      ...ListMetaData
      __typename
    }
    __typename
  }
}

fragment RunbookTestPlanListDataV2 on RunbookTestPlanV2 {
  id
  title
  description
  type
  isEditable
  updatedAt
  deletedAt
  procedureCount
  tactics {
    id
    name
    __typename
  }
  __typename
}

fragment ListMetaData on ListMeta {
  pagination {
    limit
    offset
    total
    __typename
  }
  sort {
    by
    order
    __typename
  }
  filters {
    by
    value
    __typename
  }
  __typename
}

variables: {
    "args": {
        "pagination": {
            "limit": 25,
            "offset": 0
        },
        "sort": [
            {
                "by": "updatedAt",
                "order": "DESC"
            },
            {
                "by": "title",
                "order": "DESC"
            },
            {
                "by": "procedureCount",
                "order": "DESC"
            }
        ],
        "filters": [
            {
                "by": "searchTerm",
                "value": ""
            },
            {
                "by": "tacticIds",
                "value": []
            }
        ]
    }
}
```

Response 200 (RunbookTestPlanListV2):
```json
{
    "data": {
        "runbookTestPlanListV2": {
            "data": [
                {
                    "id": "clb6yz0a3000p10jsfkloa44w",
                    "title": "Test",
                    "description": null,
                    "type": "custom",
                    "isEditable": true,
                    "updatedAt": "2022-12-20T17:30:44.797Z",
                    "deletedAt": null,
                    "procedureCount": 8,
                    "tactics": [
                        {
                            "id": "clacwm19c000e29mqf3xr071t",
                            "name": "Exfiltration",
                            "__typename": "RunbookTacticV2"
                        },
                        {
                            "id": "clacwm5oi02mh29mqg4s9bv1o",
                            "name": "Exfiltration",
                            "__typename": "RunbookTacticV2"
                        }
                    ],
                    "__typename": "RunbookTestPlanV2"
                },
                {
                    "id": "clacwm5a402lo29mq9al0dmt6",
                    "title": "Purple Team Test Plan",
                    "description": null,
                    "type": "curated",
                    "isEditable": false,
                    "updatedAt": "2022-11-11T19:40:44.477Z",
                    "deletedAt": null,
                    "procedureCount": 13,
                    "tactics": [
                        {
                            "id": "clacwm18a000429mqbucn41wg",
                            "name": "Command and Control",
                            "__typename": "RunbookTacticV2"
                        },
                        {
                            "id": "clacwm191000629mq0gce3lk0",
                            "name": "Credential Access",
                            "__typename": "RunbookTacticV2"
                        },
                        {
                            "id": "clacwm193000829mq7bhlcnj1",
                            "name": "Defense Evasion",
                            "__typename": "RunbookTacticV2"
                        }
                    ],
                    "__typename": "RunbookTestPlanV2"
                }
            ],
            "meta": {
                "pagination": {
                    "limit": 25,
                    "offset": 0,
                    "total": 2,
                    "__typename": "PaginationResult"
                },
                "sort": [
                    {
                        "by": "updatedAt",
                        "order": "DESC",
                        "__typename": "SortResult"
                    },
                    {
                        "by": "title",
                        "order": "DESC",
                        "__typename": "SortResult"
                    },
                    {
                        "by": "procedureCount",
                        "order": "DESC",
                        "__typename": "SortResult"
                    }
                ],
                "filters": [
                    {
                        "by": "searchTerm",
                        "value": "",
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "tacticIds",
                        "value": [],
                        "__typename": "FilterResult"
                    }
                ],
                "__typename": "ListMeta"
            },
            "__typename": "RunbookTestPlanListV2"
        }
    }
}
```

### RunbookTestPlanDetailV2
Folder: Runbooks / Runbooks v2 / Test Plans

Returns the data for a RunbooksV2 Test Plan and all Procedures it contains

```graphql
query RunbookTestPlanDetailV2($testPlanId: ID!) {
  runbookTestPlanV2(id: $testPlanId) {
    ...RunbookTestPlanDetailV2
    __typename
  }
}

fragment RunbookTestPlanDetailV2 on RunbookTestPlanV2 {
  id
  title
  description
  type
  procedures {
    id
    name
    description
    shortName
    isEditable
    repository {
      id
      name
      shortName
      __typename
    }
    tags {
      id
      tag
      __typename
    }
    techniques {
      ...RunbookDetailTechniqueDataV2
      __typename
    }
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookDetailTechniqueDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  methodologies {
    id
    name
    shortName
    __typename
  }
  tactics {
    id
    name
    shortName
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

variables: {
    "testPlanId": "clacwm5a402lo29mq9al0dmt6"
}
```

Response 200 (RunbookTestPlanDetailV2):
```json
{
    "data": {
        "runbookTestPlanV2": {
            "id": "clacwm5a402lo29mq9al0dmt6",
            "title": "Purple Team Test Plan",
            "description": null,
            "type": "curated",
            "procedures": [
                {
                    "id": "clacwm2sk013029mqgh8nap0q",
                    "name": "DLL Search Order Hijacking - amsi.dll",
                    "description": "Adversaries can take advantage of insecure library loading by PowerShell to load a vulnerable version of amsi.dll in order...",
                    "shortName": "T1574.001",
                    "isEditable": false,
                    "repository": {
                        "id": "clacwm17b000029mqcwg1etc9",
                        "name": "PlexTrac Curated",
                        "shortName": "PlexTrac",
                        "__typename": "RunbookRepositoryV2"
                    },
                    "tags": [],
                    "techniques": [
                        {
                            "id": "clacwm5xb02w629mqd0ju23rt",
                            "name": "DLL Search Order Hijacking",
                            "shortName": "T1574.001",
                            "description": "Adversaries may execute their own malicious payloads by hijacking the search order used to load DLLs. Windows...",
                            "methodologies": [
                                {
                                    "id": "clacwm5nx02m229mqci14ckrd",
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "tactics": [
                                {
                                    "id": "clacwm5ob02m929mq74gcc6ae",
                                    "name": "Persistence",
                                    "shortName": "TA0003",
                                    "__typename": "RunbookTacticV2"
                                }
                            ],
                            "tags": [],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "__typename": "RunbookProcedureV2"
                },
                {
                    "id": "clacwm3s601y029mqcrqq70vp",
                    "name": "Rundll32 setupapi.dll Execution",
                    "description": "Test execution of a command using rundll32.exe with setupapi.dll. Upon execution, a windows saying \"installation failed...",
                    "shortName": "T1218.011",
                    "isEditable": false,
                    "repository": {
                        "id": "clacwm17b000029mqcwg1etc9",
                        "name": "PlexTrac Curated",
                        "shortName": "PlexTrac",
                        "__typename": "RunbookRepositoryV2"
                    },
                    "tags": [],
                    "techniques": [
                        {
                            "id": "clacwm5pg02nq29mq9yt1azdv",
                            "name": "Rundll32",
                            "shortName": "T1218.011",
                            "description": "Adversaries may abuse rundll32.exe to proxy execution of malicious code. Using rundll32.exe, vice executing...",
                            "methodologies": [
                                {
                                    "id": "clacwm5nx02m229mqci14ckrd",
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "tactics": [
                                {
                                    "id": "clacwm5oh02mf29mqf5andaw8",
                                    "name": "Defense Evasion",
                                    "shortName": "TA0005",
                                    "__typename": "RunbookTacticV2"
                                }
                            ],
                            "tags": [],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "__typename": "RunbookProcedureV2"
                }
            ],
            "tags": [],
            "__typename": "RunbookTestPlanV2"
        }
    }
}
```

### RunbookTestPlanCreateV2
Folder: Runbooks / Runbooks v2 / Test Plans

```graphql
mutation RunbookTestPlanCreateV2($data: RunbookTestPlanInputV2!, $procedureIds: [ID!], $tags: [String!]) {
  runbookTestPlanCreateV2(input: $data, procedureIds: $procedureIds, tags: $tags) {
    ...RunbookTestPlanWizardFormV2
    ...RunbookTestPlanListDataV2
    __typename
  }
}

fragment RunbookTestPlanWizardFormV2 on RunbookTestPlanV2 {
  id
  title
  description
  procedures {
    ...RunbookProcedureAssignmentListDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookProcedureAssignmentListDataV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  techniques {
    ...RunbookTechniqueAssignmentListDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookTechniqueAssignmentListDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  methodologies {
    id
    name
    shortName
    __typename
  }
  tactics {
    id
    name
    shortName
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookTestPlanListDataV2 on RunbookTestPlanV2 {
  id
  title
  description
  type
  isEditable
  updatedAt
  deletedAt
  procedureCount
  tactics {
    id
    name
    __typename
  }
  __typename
}

variables: {
    "data": {
        "title": "Test Test Plan",
        "description": "<p>description</p>"
    },
    "procedureIds": [
        "clacwmagf06jt29mqhl9o3rr0"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookTestPlanCreateV2):
```json
{
    "data": {
        "runbookTestPlanCreateV2": {
            "id": "clc6mi7x700960zo3h1ejf0gd",
            "title": "Test Test Plan",
            "description": "<p>description</p>",
            "procedures": [
                {
                    "id": "clacwmagf06jt29mqhl9o3rr0",
                    "name": "MAZE FTP Upload",
                    "shortName": "T1048.003",
                    "description": "This test simulates MAZE's ransomware's ability to exfiltrate data via FTP.\nUpon successful execution, all 7z files within the %windir%\\temp...",
                    "techniques": [
                        {
                            "id": "clacwm6v603w929mqhphn2ppz",
                            "name": "Exfiltration Over Unencrypted Non-C2 Protocol",
                            "shortName": "T1048.003",
                            "description": "Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control...",
                            "methodologies": [
                                {
                                    "id": "clacwm5nx02m229mqci14ckrd",
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "tactics": [
                                {
                                    "id": "clacwm5oi02mh29mqg4s9bv1o",
                                    "name": "Exfiltration",
                                    "shortName": "TA0010",
                                    "__typename": "RunbookTacticV2"
                                }
                            ],
                            "tags": [],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "tags": [],
                    "__typename": "RunbookProcedureV2"
                }
            ],
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookTestPlanV2",
            "type": "custom",
            "isEditable": true,
            "updatedAt": "2022-12-27T19:30:32.822Z",
            "deletedAt": null,
            "procedureCount": 1,
            "tactics": [
                {
                    "id": "clacwm5o202m329mq67o51mj9",
                    "name": "Credential Access",
                    "__typename": "RunbookTacticV2"
                },
                {
                    "id": "clacwm5oi02mh29mqg4s9bv1o",
                    "name": "Exfiltration",
                    "__typename": "RunbookTacticV2"
                }
            ]
        }
    }
}
```

### RunbookTestPlanUpdateV2
Folder: Runbooks / Runbooks v2 / Test Plans

```graphql
mutation RunbookTestPlanUpdateV2($id: ID!, $data: RunbookTestPlanInputV2!, $procedureIds: [ID!], $tags: [String!]) {
  runbookTestPlanUpdateV2(
    id: $id
    input: $data
    procedureIds: $procedureIds
    tags: $tags
  ) {
    ...RunbookTestPlanWizardFormV2
    ...RunbookTestPlanListDataV2
    __typename
  }
}

fragment RunbookTestPlanWizardFormV2 on RunbookTestPlanV2 {
  id
  title
  description
  procedures {
    ...RunbookProcedureAssignmentListDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookProcedureAssignmentListDataV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  techniques {
    ...RunbookTechniqueAssignmentListDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookTechniqueAssignmentListDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  methodologies {
    id
    name
    shortName
    __typename
  }
  tactics {
    id
    name
    shortName
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookTestPlanListDataV2 on RunbookTestPlanV2 {
  id
  title
  description
  type
  isEditable
  updatedAt
  deletedAt
  procedureCount
  tactics {
    id
    name
    __typename
  }
  __typename
}

variables: {
    "id": "clc6m782y00910zo3g0eu9800",
    "data": {
        "title": "Test Test Plan",
        "description": "<p>updated description</p>"
    },
    "procedureIds": [
        "clacwmagf06jt29mqhl9o3rr0"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookTestPlanUpdateV2):
```json
{
    "data": {
        "runbookTestPlanUpdateV2": {
            "id": "clc6m782y00910zo3g0eu9800",
            "title": "Test Test Plan",
            "description": "<p>updated description</p>",
            "procedures": [
                {
                    "id": "clacwmagf06jt29mqhl9o3rr0",
                    "name": "MAZE FTP Upload",
                    "shortName": "T1048.003",
                    "description": "This test simulates MAZE's ransomware's ability to exfiltrate data via FTP.\nUpon successful execution, all 7z files within the %windir%\\temp directory...",
                    "techniques": [
                        {
                            "id": "clacwm6v603w929mqhphn2ppz",
                            "name": "Exfiltration Over Unencrypted Non-C2 Protocol",
                            "shortName": "T1048.003",
                            "description": "Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control...",
                            "methodologies": [
                                {
                                    "id": "clacwm5nx02m229mqci14ckrd",
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "tactics": [
                                {
                                    "id": "clacwm5oi02mh29mqg4s9bv1o",
                                    "name": "Exfiltration",
                                    "shortName": "TA0010",
                                    "__typename": "RunbookTacticV2"
                                }
                            ],
                            "tags": [],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "tags": [],
                    "__typename": "RunbookProcedureV2"
                }
            ],
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookTestPlanV2",
            "type": "custom",
            "isEditable": true,
            "updatedAt": "2022-12-27T19:25:14.365Z",
            "deletedAt": null,
            "procedureCount": 1,
            "tactics": [
                {
                    "id": "clacwm5o202m329mq67o51mj9",
                    "name": "Credential Access",
                    "__typename": "RunbookTacticV2"
                },
                {
                    "id": "clacwm5oi02mh29mqg4s9bv1o",
                    "name": "Exfiltration",
                    "__typename": "RunbookTacticV2"
                }
            ]
        }
    }
}
```

### RunbookTestPlanDeleteV2
Folder: Runbooks / Runbooks v2 / Test Plans

```graphql
mutation RunbookTestPlanDeleteV2($id: ID!) {
  runbookTestPlanDeleteV2(id: $id) {
    ...RunbookTestPlanListDataV2
    __typename
  }
}

fragment RunbookTestPlanListDataV2 on RunbookTestPlanV2 {
  id
  title
  description
  type
  isEditable
  updatedAt
  deletedAt
  procedureCount
  tactics {
    id
    name
    __typename
  }
  __typename
}

variables: {
    "id": "clc6mi7x700960zo3h1ejf0gd"
}
```

Response 200 (RunbookTestPlanDeleteV2):
```json
{
    "data": {
        "runbookTestPlanDeleteV2": {
            "id": "clc6mi7x700960zo3h1ejf0gd",
            "title": "Test Test Plan",
            "description": "<p>description</p>",
            "type": "custom",
            "isEditable": true,
            "updatedAt": "2022-12-27T19:30:32.822Z",
            "deletedAt": "2022-12-27T19:41:43.241Z",
            "procedureCount": 1,
            "tactics": [
                {
                    "id": "clacwm5o202m329mq67o51mj9",
                    "name": "Credential Access",
                    "__typename": "RunbookTacticV2"
                },
                {
                    "id": "clacwm5oi02mh29mqg4s9bv1o",
                    "name": "Exfiltration",
                    "__typename": "RunbookTacticV2"
                }
            ],
            "__typename": "RunbookTestPlanV2"
        }
    }
}
```

### RunbookRepositoryAvailableUserListV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Repositories / Users

```graphql
query RunbookRepositoryAvailableUserListV2($args: ListArgs!) {
  runbookRepositoryAvailableUserListV2(args: $args) {
    data {
      ...RunbookRepositoryAvailableUserData
      __typename
    }
    meta {
      pagination {
        total
        __typename
      }
      __typename
    }
    __typename
  }
}

fragment RunbookRepositoryAvailableUserData on RunbookRepositoryUserData {
  id
  user_id
  fullName
  email
  __typename
}

variables: {
    "args": {
        "pagination": {
            "limit": 100,
            "offset": 0
        },
        "filters": [
            {
                "by": "permissionsIn",
                "value": [
                    "CONTENT_LIBRARY.RUNBOOKSDB.ACCESS_RUNBOOKS_REPOSITORIES"
                ]
            },
            {
                "by": "permissionsNotIn",
                "value": [
                    "CONTENT_LIBRARY.RUNBOOKSDB.MANAGE_RUNBOOKS_REPOSITORIES"
                ]
            }
        ]
    }
}
```

Response 200 (RunbookRepositoryAvailableUserListV2):
```json
{
    "data": {
        "runbookRepositoryAvailableUserListV2": {
            "data": [
                {
                    "id": "219516932",
                    "user_id": 219516932,
                    "fullName": "Test Runbooks",
                    "email": "test@plextrac.com",
                    "__typename": "RunbookRepositoryUserData"
                }
            ],
            "meta": {
                "pagination": {
                    "total": 1,
                    "__typename": "PaginationResult"
                },
                "__typename": "ListMeta"
            },
            "__typename": "RunbookRepositoryAvailableUserListV2"
        }
    }
}
```

### RunbookRepositoryUsersV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Repositories / Users

```graphql
query RunbookRepositoryUsersV2($repositoryId: ID!) {
  runbookRepositoryUsersV2(id: $repositoryId) {
    ...RunbookRepositoryUserV2
    __typename
  }
}

fragment RunbookRepositoryUserV2 on RunbookRepositoryUserV2 {
  id
  role
  repositoryId
  userId
  userData {
    id
    user_id
    fullName
    email
    __typename
  }
  __typename
}

variables: {
    "repositoryId": "clc0rr6v500540zo31c5i4cz2"
}
```

Response 200 (RunbookRepositoryUsersV2):
```json
{
    "data": {
        "runbookRepositoryUsersV2": [
            {
                "id": "clc0s5mvi00560zo34ge538lz",
                "role": "editor",
                "repositoryId": "clc0rr6v500540zo31c5i4cz2",
                "userId": "219516932",
                "userData": {
                    "id": "219516932",
                    "user_id": 219516932,
                    "fullName": "Test Runbooks",
                    "email": "test@plextrac.com",
                    "__typename": "RunbookRepositoryUserData"
                },
                "__typename": "RunbookRepositoryUserV2"
            }
        ]
    }
}
```

Response 200 (No Assigned Users):
```json
{
    "data": {
        "runbookRepositoryUsersV2": []
    }
}
```

### RunbookRepositoryUsersAddV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Repositories / Users

```graphql
mutation RunbookRepositoryUsersAddV2($repositoryId: ID!, $users: [RunbookRepositoryUserCreateInputV2!]!) {
  runbookRepositoryUsersAddV2(repositoryId: $repositoryId, users: $users) {
    ...RunbookRepositoryUserV2
    __typename
  }
}

fragment RunbookRepositoryUserV2 on RunbookRepositoryUserV2 {
  id
  role
  repositoryId
  userId
  userData {
    id
    user_id
    fullName
    email
    __typename
  }
  __typename
}

variables: {
    "repositoryId": "clc0rr6v500540zo31c5i4cz2",
    "users": [
        {
            "userId": "219516932",
            "role": "editor"
        }
    ]
}
```

Response 200 (RunbookRepositoryUsersAddV2):
```json
{
    "data": {
        "runbookRepositoryUsersAddV2": [
            {
                "id": "clc0s5mvi00560zo34ge538lz",
                "role": "editor",
                "repositoryId": "clc0rr6v500540zo31c5i4cz2",
                "userId": "219516932",
                "userData": {
                    "id": "219516932",
                    "user_id": 219516932,
                    "fullName": "Test Runbooks",
                    "email": "test@plextrac.com",
                    "__typename": "RunbookRepositoryUserData"
                },
                "__typename": "RunbookRepositoryUserV2"
            }
        ]
    }
}
```

Response 200 (ERR - User already added to repository):
```json
{
    "errors": [
        {
            "message": "duplicate key value violates unique constraint \"runbook_repository_to_user_repository_id_user_id_key\"",
            "locations": [
                {
                    "line": 2,
                    "column": 3
                }
            ],
            "path": [
                "runbookRepositoryUsersAddV2"
            ],
            "extensions": {
                "code": "INTERNAL_SERVER_ERROR",
                "exception": {
                    "length": 340,
                    "name": "error",
                    "severity": "ERROR",
                    "code": "23505",
                    "detail": "Key (repository_id, user_id)=(clc0rr6v500540zo31c5i4cz2, 219516932) already exists.",
                    "schema": "public",
                    "table": "runbook_repository_to_user",
                    "constraint": "runbook_repository_to_user_repository_id_user_id_key",
                    "file": "nbtinsert.c",
                    "line": "663",
                    "routine": "_bt_check_unique"
                }
            }
        }
    ],
    "data": null
}
```

### RunbookRepositoryUserUpdateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Repositories / Users

Can update the permission of a user in the RunbookDB Repository.

role can be one of ["viewer", "editor"]

```graphql
mutation RunbookRepositoryUserUpdateV2($repositoryId: ID!, $userId: ID!, $data: RunbookRepositoryUserUpdateInputV2!) {
  runbookRepositoryUserUpdateV2(
    repositoryId: $repositoryId
    userId: $userId
    input: $data
  ) {
    ...RunbookRepositoryUserV2
    __typename
  }
}

fragment RunbookRepositoryUserV2 on RunbookRepositoryUserV2 {
  id
  role
  repositoryId
  userId
  userData {
    id
    user_id
    fullName
    email
    __typename
  }
  __typename
}

variables: {
    "repositoryId": "clc6lx98y008z0zo39qwu9sq5",
    "userId": "219516932",
    "data": {
        "role": "editor"
    }
}
```

Response 200 (RunbookRepositoryUserUpdateV2):
```json
{
    "data": {
        "runbookRepositoryUserUpdateV2": {
            "id": "clc6lxv1r00900zo37wqyd1n4",
            "role": "editor",
            "repositoryId": "clc6lx98y008z0zo39qwu9sq5",
            "userId": "219516932",
            "userData": {
                "id": "219516932",
                "user_id": 219516932,
                "fullName": "Test Runbooks",
                "email": "test@plextrac.com",
                "__typename": "RunbookRepositoryUserData"
            },
            "__typename": "RunbookRepositoryUserV2"
        }
    }
}
```

### RunbookRepositoryUserRemoveV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Repositories / Users

```graphql
mutation RunbookRepositoryUserRemoveV2($repositoryId: ID!, $userId: ID!) {
  runbookRepositoryUserRemoveV2(repositoryId: $repositoryId, userId: $userId) {
    ...RunbookRepositoryUserV2
    __typename
  }
}

fragment RunbookRepositoryUserV2 on RunbookRepositoryUserV2 {
  id
  role
  repositoryId
  userId
  userData {
    id
    user_id
    fullName
    email
    __typename
  }
  __typename
}

variables: {
    "repositoryId": "clc0rr6v500540zo31c5i4cz2",
    "userId": "219516932"
}
```

Response 200 (RunbookRepositoryUserRemoveV2):
```json
{
    "data": {
        "runbookRepositoryUserRemoveV2": {
            "id": "clc6lqsdf008x0zo31w9za127",
            "role": "editor",
            "repositoryId": "clc0rr6v500540zo31c5i4cz2",
            "userId": "219516932",
            "userData": {
                "id": "219516932",
                "user_id": 219516932,
                "fullName": "Test Runbooks",
                "email": "test@plextrac.com",
                "__typename": "RunbookRepositoryUserData"
            },
            "__typename": "RunbookRepositoryUserV2"
        }
    }
}
```

### RunbookRepositoryListV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Repositories

Returns a list of all Repositories in the RunbooksDB

```graphql
query RunbookRepositoryListV2($args: ListArgs!) {
  runbookRepositoryListV2(args: $args) {
    data {
      ...RunbookRepositoryListDataV2
      __typename
    }
    meta {
      ...ListMetaData
      __typename
    }
    __typename
  }
}

fragment RunbookRepositoryListDataV2 on RunbookRepositoryV2 {
  id
  name
  shortName
  description
  type
  procedures {
    id
    __typename
  }
  isEditable
  updatedAt
  userCount
  __typename
}

fragment ListMetaData on ListMeta {
  pagination {
    limit
    offset
    total
    __typename
  }
  sort {
    by
    order
    __typename
  }
  filters {
    by
    value
    __typename
  }
  __typename
}

variables: {
    "args": {
        "pagination": {
            "limit": 999,
            "offset": 0
        }
    }
}
```

Response 200 (RunbookRepositoryListV2):
```json
{
    "data": {
        "runbookRepositoryListV2": {
            "data": [
                {
                    "id": "clacwm17b000029mqcwg1etc9",
                    "name": "PlexTrac Curated",
                    "shortName": "PlexTrac",
                    "description": "Community produced procedures on MITRE/CTI",
                    "type": "curated",
                    "procedures": [
                        {
                            "id": "clacwm2r1011l29mq73kdg8ja",
                            "__typename": "RunbookProcedureV2"
                        },
                        {
                            "id": "clacwm2qi011c29mqctyf2mrm",
                            "__typename": "RunbookProcedureV2"
                        },
                        {
                            "id": "clacwm2qt011f29mqbtgodc2r",
                            "__typename": "RunbookProcedureV2"
                        },
                        {
                            "id": "clacwm2t5013i29mqdot2g3zq",
                            "__typename": "RunbookProcedureV2"
                        },
                        {
                            "id": "clacwm2pz011029mqfcpvfrdr",
                            "__typename": "RunbookProcedureV2"
                        }
                    ],
                    "isEditable": false,
                    "updatedAt": "2022-11-11T19:40:51.431Z",
                    "userCount": 0,
                    "__typename": "RunbookRepositoryV2"
                }
            ],
            "meta": {
                "pagination": {
                    "limit": 999,
                    "offset": 0,
                    "total": 1,
                    "__typename": "PaginationResult"
                },
                "sort": null,
                "filters": null,
                "__typename": "ListMeta"
            },
            "__typename": "RunbookRepositoryListV2"
        }
    }
}
```

### RunbookRepositoryDetailV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Repositories

Returns the data for a RunbooksV2 Repository and a list of Procedures it contains

```graphql
query RunbookRepositoryDetailV2($repositoryId: ID!, $procedureListArgs: ListArgs!) {
  runbookRepositoryV2(id: $repositoryId) {
    ...RunbookRepositoryDetailV2
    __typename
  }
  runbookProcedureListV2(args: $procedureListArgs) {
    data {
      ...RunbookProcedureDataGridV2
      __typename
    }
    meta {
      ...ListMetaData
      __typename
    }
    __typename
  }
}

fragment RunbookRepositoryDetailV2 on RunbookRepositoryV2 {
  id
  name
  shortName
  description
  type
  isEditable
  updatedAt
  __typename
}

fragment RunbookProcedureDataGridV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  isEditable
  updatedAt
  deletedAt
  repository {
    id
    name
    shortName
    type
    __typename
  }
  techniques {
    id
    name
    shortName
    methodologies {
      name
      shortName
      __typename
    }
    __typename
  }
  __typename
}

fragment ListMetaData on ListMeta {
  pagination {
    limit
    offset
    total
    __typename
  }
  sort {
    by
    order
    __typename
  }
  filters {
    by
    value
    __typename
  }
  __typename
}

variables: {
    "repositoryId": "clacwm17b000029mqcwg1etc9",
    "procedureListArgs": {
        "pagination": {
            "limit": 25,
            "offset": 0
        },
        "sort": [
            {
                "by": "shortName",
                "order": "DESC"
            },
            {
                "by": "name",
                "order": "DESC"
            }
        ],
        "filters": [
            {
                "by": "repositoryId",
                "value": "clacwm17b000029mqcwg1etc9"
            },
            {
                "by": "tacticIds",
                "value": []
            },
            {
                "by": "methodologyIds",
                "value": []
            },
            {
                "by": "searchTerm",
                "value": ""
            }
        ]
    }
}
```

Response 200 (RunbookRepositoryDetailV2):
```json
{
    "data": {
        "runbookRepositoryV2": {
            "id": "clacwm17b000029mqcwg1etc9",
            "name": "PlexTrac Curated",
            "shortName": "PlexTrac",
            "description": "Community produced procedures on MITRE/CTI",
            "type": "curated",
            "isEditable": false,
            "updatedAt": "2022-11-11T19:40:51.431Z",
            "__typename": "RunbookRepositoryV2"
        },
        "runbookProcedureListV2": {
            "data": [
                {
                    "id": "clacwm7pe04hn29mqbu96b4n7",
                    "name": "Plist Modification",
                    "shortName": "T1647",
                    "description": "Modify MacOS plist file in one of two directories\n\n\n**Supported Platforms:** macos\n\n",
                    "isEditable": false,
                    "updatedAt": "2022-11-11T19:40:47.618Z",
                    "deletedAt": null,
                    "repository": {
                        "id": "clacwm17b000029mqcwg1etc9",
                        "name": "PlexTrac Curated",
                        "shortName": "PlexTrac",
                        "type": "curated",
                        "__typename": "RunbookRepositoryV2"
                    },
                    "techniques": [
                        {
                            "id": "clacwm6bg03ag29mq06ho26ob",
                            "name": "Plist File Modification",
                            "shortName": "T1647",
                            "methodologies": [
                                {
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "__typename": "RunbookProcedureV2"
                },
                {
                    "id": "clacwm7fy048w29mqbrfx4mi1",
                    "name": "WinPwn - Reflectively load Mimik@tz into memory",
                    "shortName": "T1620",
                    "description": "Reflectively load Mimik@tz into memory technique via function of WinPwn\n\n**Supported Platforms:** windows\n\n",
                    "isEditable": false,
                    "updatedAt": "2022-11-11T19:40:47.279Z",
                    "deletedAt": null,
                    "repository": {
                        "id": "clacwm17b000029mqcwg1etc9",
                        "name": "PlexTrac Curated",
                        "shortName": "PlexTrac",
                        "type": "curated",
                        "__typename": "RunbookRepositoryV2"
                    },
                    "techniques": [
                        {
                            "id": "clacwm627031029mq3yggfznc",
                            "name": "Reflective Code Loading",
                            "shortName": "T1620",
                            "methodologies": [
                                {
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "__typename": "RunbookProcedureV2"
                }
            ],
            "meta": {
                "pagination": {
                    "limit": 25,
                    "offset": 0,
                    "total": 1163,
                    "__typename": "PaginationResult"
                },
                "sort": [
                    {
                        "by": "shortName",
                        "order": "DESC",
                        "__typename": "SortResult"
                    },
                    {
                        "by": "name",
                        "order": "DESC",
                        "__typename": "SortResult"
                    }
                ],
                "filters": [
                    {
                        "by": "repositoryId",
                        "value": "clacwm17b000029mqcwg1etc9",
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "tacticIds",
                        "value": [],
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "methodologyIds",
                        "value": [],
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "searchTerm",
                        "value": "",
                        "__typename": "FilterResult"
                    }
                ],
                "__typename": "ListMeta"
            },
            "__typename": "RunbookProcedureListV2"
        }
    }
}
```

### RunbookRepositoryCreateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Repositories

Create a RunbookDB Repository.

Must have a unique shortName (Repository ID Prefix in platform)

type can be one of ["private", "managed", "open"]

```graphql
mutation RunbookRepositoryCreateV2($data: RunbookRepositoryInputV2!) {
  runbookRepositoryCreateV2(input: $data) {
    id
    name
    shortName
    description
    type
    isEditable
    __typename
  }
}

variables: {
    "data": {
        "name": "Test RB Repo",
        "shortName": "test",
        "description": "description",
        "type": "managed"
    }
}
```

Response 200 (RunbookRepositoryCreateV2):
```json
{
    "data": {
        "runbookRepositoryCreateV2": {
            "id": "clc0rr6v500540zo31c5i4cz2",
            "name": "Test RB Repo",
            "shortName": "test",
            "description": "description",
            "type": "managed",
            "isEditable": true,
            "__typename": "RunbookRepositoryV2"
        }
    }
}
```

Response 200 (ERR - Duplicate Short Name Key):
```json
{
    "errors": [
        {
            "message": "duplicate key value violates unique constraint \"runbook_repository_short_name_key\"",
            "locations": [
                {
                    "line": 2,
                    "column": 3
                }
            ],
            "path": [
                "runbookRepositoryCreateV2"
            ],
            "extensions": {
                "code": "INTERNAL_SERVER_ERROR",
                "exception": {
                    "length": 250,
                    "name": "error",
                    "severity": "ERROR",
                    "code": "23505",
                    "detail": "Key (short_name)=(test) already exists.",
                    "schema": "public",
                    "table": "runbook_repository",
                    "constraint": "runbook_repository_short_name_key",
                    "file": "nbtinsert.c",
                    "line": "663",
                    "routine": "_bt_check_unique"
                }
            }
        }
    ],
    "data": null
}
```

### RunbookRepositoryUpdateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Repositories

```graphql
mutation RunbookRepositoryUpdateV2($data: RunbookRepositoryInputV2!, $repositoryId: ID!) {
  runbookRepositoryUpdateV2(input: $data, id: $repositoryId) {
    ...RunbookRepositoryUpdateDataV2
    __typename
  }
}

fragment RunbookRepositoryUpdateDataV2 on RunbookRepositoryV2 {
  id
  name
  shortName
  description
  type
  isEditable
  updatedAt
  __typename
}

variables: {
    "repositoryId": "clc0rr6v500540zo31c5i4cz2",
    "data": {
        "name": "Test RB Repo",
        "shortName": "test",
        "description": "updated description",
        "type": "managed"
    }
}
```

Response 200 (RunbookRepositoryUpdateV2):
```json
{
    "data": {
        "runbookRepositoryUpdateV2": {
            "id": "clc0rr6v500540zo31c5i4cz2",
            "name": "Test RB Repo",
            "shortName": "test",
            "description": "updated description",
            "type": "managed",
            "isEditable": true,
            "updatedAt": "2022-12-27T19:11:20.562Z",
            "__typename": "RunbookRepositoryV2"
        }
    }
}
```

### RunbookRepositoryDeleteV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Repositories

```graphql
mutation RunbookRepositoryDeleteV2($id: ID!) {
  runbookRepositoryDeleteV2(id: $id) {
    id
    deletedAt
    __typename
  }
}

variables: {
    "id": "clc6lvdcw008y0zo3b0yd9nu1"
}
```

Response 200 (RunbookRepositoryDeleteV2):
```json
{
    "data": {
        "runbookRepositoryDeleteV2": {
            "id": "clc6lvdcw008y0zo3b0yd9nu1",
            "deletedAt": "2022-12-27T19:13:02.518Z",
            "__typename": "RunbookRepositoryV2"
        }
    }
}
```

### RunbookMethodologyListV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Methodologies

Returns a list of Methodologies in the RunbooksDB

```graphql
query RunbookMethodologyListV2($args: ListArgs!) {
  runbookMethodologyListV2(args: $args) {
    data {
      ...RunbookMethodologyListDataV2
      __typename
    }
    meta {
      ...ListMetaData
      __typename
    }
    __typename
  }
}

fragment RunbookMethodologyListDataV2 on RunbookMethodologyV2 {
  id
  name
  shortName
  isEditable
  __typename
}

fragment ListMetaData on ListMeta {
  pagination {
    limit
    offset
    total
    __typename
  }
  sort {
    by
    order
    __typename
  }
  filters {
    by
    value
    __typename
  }
  __typename
}

variables: {
    "args": {
        "pagination": {
            "limit": 25,
            "offset": 0
        },
        "sort": [
            {
                "by": "shortName",
                "order": "DESC"
            },
            {
                "by": "name",
                "order": "DESC"
            }
        ],
        "filters": [
            {
                "by": "searchTerm",
                "value": ""
            }
        ]
    }
}
```

Response 200 (RunbookMethodologyListV2):
```json
{
    "data": {
        "runbookMethodologyListV2": {
            "data": [
                {
                    "id": "clacwm5nx02m229mqci14ckrd",
                    "name": "Mitre ATT&CK 11.3",
                    "shortName": "Mitre-11.3",
                    "isEditable": false,
                    "__typename": "RunbookMethodologyV2"
                },
                {
                    "id": "clacwm17k000129mqhudqhx01",
                    "name": "Mitre ATT&CK 9.0",
                    "shortName": "Mitre-9.0",
                    "isEditable": false,
                    "__typename": "RunbookMethodologyV2"
                }
            ],
            "meta": {
                "pagination": {
                    "limit": 25,
                    "offset": 0,
                    "total": 2,
                    "__typename": "PaginationResult"
                },
                "sort": [
                    {
                        "by": "shortName",
                        "order": "DESC",
                        "__typename": "SortResult"
                    },
                    {
                        "by": "name",
                        "order": "DESC",
                        "__typename": "SortResult"
                    }
                ],
                "filters": [
                    {
                        "by": "searchTerm",
                        "value": "",
                        "__typename": "FilterResult"
                    }
                ],
                "__typename": "ListMeta"
            },
            "__typename": "RunbookMethodologyListV2"
        }
    }
}
```

### RunbookMethodologyDetailV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Methodologies

Returns the data for a RunbooksV2 Methodology

```graphql
query RunbookMethodologyDetailV2($methodologyId: ID!) {
  runbookMethodologyV2(id: $methodologyId) {
    ...RunbookMethodologyFormDataV2
    __typename
  }
}

fragment RunbookMethodologyFormDataV2 on RunbookMethodologyV2 {
  id
  name
  shortName
  description
  isEditable
  tactics {
    ...RunbookMethodologyFormTacticDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookMethodologyFormTacticDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

variables: {
    "methodologyId": "clacwm5nx02m229mqci14ckrd"
}
```

Response 200 (RunbookMethodologyDetailV2):
```json
{
    "data": {
        "runbookMethodologyV2": {
            "id": "clacwm5nx02m229mqci14ckrd",
            "name": "Mitre ATT&CK 11.3",
            "shortName": "Mitre-11.3",
            "description": "Mitre ATT&CK framework (version: 11.3)",
            "isEditable": false,
            "tactics": [
                {
                    "id": "clacwm5ok02mj29mq0ywaavye",
                    "name": "Discovery",
                    "shortName": "TA0007",
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                },
                {
                    "id": "clacwm5o202m329mq67o51mj9",
                    "name": "Credential Access",
                    "shortName": "TA0006",
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                }
            ],
            "tags": [],
            "__typename": "RunbookMethodologyV2"
        }
    }
}
```

### RunbookMethodologyCreateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Methodologies

```graphql
mutation RunbookMethodologyCreateV2($data: RunbookMethodologyInputV2!, $tacticIds: [ID!], $tags: [String!]) {
  runbookMethodologyCreateV2(input: $data, tacticIds: $tacticIds, tags: $tags) {
    ...RunbookMethodologyFormDataV2
    __typename
  }
}

fragment RunbookMethodologyFormDataV2 on RunbookMethodologyV2 {
  id
  name
  shortName
  description
  isEditable
  tactics {
    ...RunbookMethodologyFormTacticDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookMethodologyFormTacticDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

variables: {
    "data": {
        "name": "Test title",
        "shortName": "mid",
        "description": "<p>description</p>"
    },
    "tacticIds": [
        "clacwm5o202m329mq67o51mj9",
        "clacwm5o602m529mqbfxnfv54",
        "clacwm5o802m729mqf9j76yj4"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookMethodologyCreateV2):
```json
{
    "data": {
        "runbookMethodologyCreateV2": {
            "id": "clc6i9mu6007r0zo362uvejpt",
            "name": "Test title",
            "shortName": "mid",
            "description": "<p>description</p>",
            "isEditable": true,
            "tactics": [
                {
                    "id": "clacwm5o202m329mq67o51mj9",
                    "name": "Credential Access",
                    "shortName": "TA0006",
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        },
                        {
                            "id": "clc6i7cp3007k0zn5g7txfhd8",
                            "name": "Test title",
                            "shortName": "mid",
                            "__typename": "RunbookMethodologyV2"
                        },
                        {
                            "id": "clc6i9mu6007r0zo362uvejpt",
                            "name": "Test title",
                            "shortName": "mid",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                },
                {
                    "id": "clacwm5o602m529mqbfxnfv54",
                    "name": "Execution",
                    "shortName": "TA0002",
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        },
                        {
                            "id": "clc6i7cp3007k0zn5g7txfhd8",
                            "name": "Test title",
                            "shortName": "mid",
                            "__typename": "RunbookMethodologyV2"
                        },
                        {
                            "id": "clc6i9mu6007r0zo362uvejpt",
                            "name": "Test title",
                            "shortName": "mid",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                },
                {
                    "id": "clacwm5o802m729mqf9j76yj4",
                    "name": "Impact",
                    "shortName": "TA0040",
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        },
                        {
                            "id": "clc6i7cp3007k0zn5g7txfhd8",
                            "name": "Test title",
                            "shortName": "mid",
                            "__typename": "RunbookMethodologyV2"
                        },
                        {
                            "id": "clc6i9mu6007r0zo362uvejpt",
                            "name": "Test title",
                            "shortName": "mid",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                }
            ],
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookMethodologyV2"
        }
    }
}
```

### RunbookMethodologyUpdateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Methodologies

```graphql
mutation RunbookMethodologyUpdateV2($id: ID!, $data: RunbookMethodologyInputV2!, $tacticIds: [ID!], $tags: [String!]) {
  runbookMethodologyUpdateV2(
    id: $id
    input: $data
    tacticIds: $tacticIds
    tags: $tags
  ) {
    ...RunbookMethodologyFormDataV2
    __typename
  }
}

fragment RunbookMethodologyFormDataV2 on RunbookMethodologyV2 {
  id
  name
  shortName
  description
  isEditable
  tactics {
    ...RunbookMethodologyFormTacticDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookMethodologyFormTacticDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

variables: {
    "id": "clc6i7cp3007k0zn5g7txfhd8",
    "data": {
        "name": "Test title",
        "shortName": "mid",
        "description": "<p>updated description</p>"
    },
    "tacticIds": [
        "clacwm5o202m329mq67o51mj9",
        "clacwm5o602m529mqbfxnfv54",
        "clacwm5o802m729mqf9j76yj4"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookMethodologyUpdateV2):
```json
{
    "data": {
        "runbookMethodologyUpdateV2": {
            "id": "clc6i7cp3007k0zn5g7txfhd8",
            "name": "Test title",
            "shortName": "mid",
            "description": "<p>updated description</p>",
            "isEditable": true,
            "tactics": [
                {
                    "id": "clacwm5o202m329mq67o51mj9",
                    "name": "Credential Access",
                    "shortName": "TA0006",
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        },
                        {
                            "id": "clc6i7cp3007k0zn5g7txfhd8",
                            "name": "Test title",
                            "shortName": "mid",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                },
                {
                    "id": "clacwm5o602m529mqbfxnfv54",
                    "name": "Execution",
                    "shortName": "TA0002",
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        },
                        {
                            "id": "clc6i7cp3007k0zn5g7txfhd8",
                            "name": "Test title",
                            "shortName": "mid",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                },
                {
                    "id": "clacwm5o802m729mqf9j76yj4",
                    "name": "Impact",
                    "shortName": "TA0040",
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        },
                        {
                            "id": "clc6i7cp3007k0zn5g7txfhd8",
                            "name": "Test title",
                            "shortName": "mid",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                }
            ],
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookMethodologyV2"
        }
    }
}
```

### RunbookMethodologyDeleteV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Methodologies

```graphql
mutation RunbookMethodologyDeleteV2($id: ID!) {
  runbookMethodologyDeleteV2(id: $id) {
    ...RunbookMethodologyListDataV2
    __typename
  }
}

fragment RunbookMethodologyListDataV2 on RunbookMethodologyV2 {
  id
  name
  shortName
  isEditable
  __typename
}

variables: {
    "id": "clc6ieu6g007w0zo37ac3a2no"
}
```

Response 200 (RunbookMethodologyDeleteV2):
```json
{
    "data": {
        "runbookMethodologyDeleteV2": {
            "id": "clc6ieu6g007w0zo37ac3a2no",
            "name": "Test title",
            "shortName": "mid",
            "isEditable": true,
            "__typename": "RunbookMethodologyV2"
        }
    }
}
```

### RunbookTacticListV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Tactics

Returns a list of Tactics in the RunbooksDB

```graphql
query RunbookTacticListV2($args: ListArgs!) {
  runbookTacticListV2(args: $args) {
    data {
      ...RunbookTacticListDataV2
      __typename
    }
    meta {
      ...ListMetaData
      __typename
    }
    __typename
  }
}

fragment RunbookTacticListDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  isEditable
  methodologies {
    id
    name
    __typename
  }
  __typename
}

fragment ListMetaData on ListMeta {
  pagination {
    limit
    offset
    total
    __typename
  }
  sort {
    by
    order
    __typename
  }
  filters {
    by
    value
    __typename
  }
  __typename
}

variables: {
    "args": {
        "pagination": {
            "limit": 25,
            "offset": 0
        },
        "sort": [
            {
                "by": "shortName",
                "order": "DESC"
            },
            {
                "by": "name",
                "order": "DESC"
            }
        ],
        "filters": [
            {
                "by": "methodologyIds",
                "value": []
            },
            {
                "by": "searchTerm",
                "value": ""
            }
        ]
    }
}
```

Response 200 (RunbookTacticListV2):
```json
{
    "data": {
        "runbookTacticListV2": {
            "data": [
                {
                    "id": "clacwm19q000q29mqat28hbjq",
                    "name": "Reconnaissance",
                    "shortName": "TA0043",
                    "isEditable": false,
                    "methodologies": [
                        {
                            "id": "clacwm17k000129mqhudqhx01",
                            "name": "Mitre ATT&CK 9.0",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                },
                {
                    "id": "clacwm5oo02mp29mq1s2t4gtq",
                    "name": "Reconnaissance",
                    "shortName": "TA0043",
                    "isEditable": false,
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                },
                {
                    "id": "clacwm19t000s29mq5px205fk",
                    "name": "Resource Development",
                    "shortName": "TA0042",
                    "isEditable": false,
                    "methodologies": [
                        {
                            "id": "clacwm17k000129mqhudqhx01",
                            "name": "Mitre ATT&CK 9.0",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                }
            ],
            "meta": {
                "pagination": {
                    "limit": 25,
                    "offset": 0,
                    "total": 28,
                    "__typename": "PaginationResult"
                },
                "sort": [
                    {
                        "by": "shortName",
                        "order": "DESC",
                        "__typename": "SortResult"
                    },
                    {
                        "by": "name",
                        "order": "DESC",
                        "__typename": "SortResult"
                    }
                ],
                "filters": [
                    {
                        "by": "methodologyIds",
                        "value": [],
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "searchTerm",
                        "value": "",
                        "__typename": "FilterResult"
                    }
                ],
                "__typename": "ListMeta"
            },
            "__typename": "RunbookTacticListV2"
        }
    }
}
```

### RunbookTacticDetailV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Tactics

Returns the data for a RunbooksV2 Tactic

```graphql
query RunbookTacticDetailV2($tacticId: ID!) {
  runbookTacticV2(id: $tacticId) {
    ...RunbookTacticFormDataV2
    __typename
  }
}

fragment RunbookTacticFormDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  description
  methodologies {
    ...RunbookTacticFormMethodologyDataV2
    __typename
  }
  techniques {
    ...RunbookProcedureFormTechniqueDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookTacticFormMethodologyDataV2 on RunbookMethodologyV2 {
  id
  name
  shortName
  __typename
}

fragment RunbookProcedureFormTechniqueDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  tactics {
    id
    name
    shortName
    __typename
  }
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

variables: {
    "tacticId": "clacwm5oo02mp29mq1s2t4gtq"
}
```

Response 200 (RunbookTacticDetailV2):
```json
{
    "data": {
        "runbookTacticV2": {
            "id": "clacwm5oo02mp29mq1s2t4gtq",
            "name": "Reconnaissance",
            "shortName": "TA0043",
            "description": "The adversary is trying to gather information they can use to plan future operations.\n\nReconnaissance consists of techniques...",
            "methodologies": [
                {
                    "id": "clacwm5nx02m229mqci14ckrd",
                    "name": "Mitre ATT&CK 11.3",
                    "shortName": "Mitre-11.3",
                    "__typename": "RunbookMethodologyV2"
                }
            ],
            "techniques": [
                {
                    "id": "clacwm5pv02oc29mq7bhj125y",
                    "name": "Gather Victim Host Information",
                    "shortName": "T1592",
                    "description": "Adversaries may gather information about the victim's hosts that can be used during targeting. Information about...",
                    "tactics": [
                        {
                            "id": "clacwm5oo02mp29mq1s2t4gtq",
                            "name": "Reconnaissance",
                            "shortName": "TA0043",
                            "__typename": "RunbookTacticV2"
                        }
                    ],
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTechniqueV2"
                },
                {
                    "id": "clacwm5pw02oe29mqdp1ma0o5",
                    "name": "Digital Certificates",
                    "shortName": "T1596.003",
                    "description": "Adversaries may search public digital certificate data for information about victims that can be used during...",
                    "tactics": [
                        {
                            "id": "clacwm5oo02mp29mq1s2t4gtq",
                            "name": "Reconnaissance",
                            "shortName": "TA0043",
                            "__typename": "RunbookTacticV2"
                        }
                    ],
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTechniqueV2"
                }
            ],
            "tags": [],
            "__typename": "RunbookTacticV2"
        }
    }
}
```

### RunbookTacticCreateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Tactics

```graphql
mutation RunbookTacticCreateV2($data: RunbookTacticInputV2!, $methodologyIds: [ID!], $techniqueIds: [ID!], $tags: [String!]) {
  runbookTacticCreateV2(
    input: $data
    methodologyIds: $methodologyIds
    techniqueIds: $techniqueIds
    tags: $tags
  ) {
    ...RunbookTacticFormDataV2
    __typename
  }
}

fragment RunbookTacticFormDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  description
  methodologies {
    ...RunbookTacticFormMethodologyDataV2
    __typename
  }
  techniques {
    ...RunbookProcedureFormTechniqueDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookTacticFormMethodologyDataV2 on RunbookMethodologyV2 {
  id
  name
  shortName
  __typename
}

fragment RunbookProcedureFormTechniqueDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  tactics {
    id
    name
    shortName
    __typename
  }
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

variables: {
    "data": {
        "name": "Test Tactic",
        "shortName": "tid",
        "description": "<p>desc</p>"
    },
    "methodologyIds": [
        "clacwm5nx02m229mqci14ckrd"
    ],
    "techniqueIds": [
        "clacwm5ot02mv29mqevmb44lh"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookTacticCreateV2):
```json
{
    "data": {
        "runbookTacticCreateV2": {
            "id": "clc6irvck00820zo32c4mgdkd",
            "name": "Test Tactic",
            "shortName": "tid",
            "description": "<p>desc</p>",
            "methodologies": [
                {
                    "id": "clacwm5nx02m229mqci14ckrd",
                    "name": "Mitre ATT&CK 11.3",
                    "shortName": "Mitre-11.3",
                    "__typename": "RunbookMethodologyV2"
                }
            ],
            "techniques": [
                {
                    "id": "clacwm5ot02mv29mqevmb44lh",
                    "name": "Extra Window Memory Injection",
                    "shortName": "T1055.011",
                    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly...",
                    "tactics": [
                        {
                            "id": "clacwm5od02mb29mqa5fz3l4q",
                            "name": "Privilege Escalation",
                            "shortName": "TA0004",
                            "__typename": "RunbookTacticV2"
                        },
                        {
                            "id": "clacwm5oh02mf29mqf5andaw8",
                            "name": "Defense Evasion",
                            "shortName": "TA0005",
                            "__typename": "RunbookTacticV2"
                        },
                        {
                            "id": "clc6irvck00820zo32c4mgdkd",
                            "name": "Test Tactic",
                            "shortName": "tid",
                            "__typename": "RunbookTacticV2"
                        }
                    ],
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTechniqueV2"
                }
            ],
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookTacticV2"
        }
    }
}
```

### RunbookTacticUpdateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Tactics

```graphql
mutation RunbookTacticUpdateV2($id: ID!, $data: RunbookTacticInputV2!, $methodologyIds: [ID!], $techniqueIds: [ID!], $tags: [String!]) {
  runbookTacticUpdateV2(
    id: $id
    input: $data
    methodologyIds: $methodologyIds
    techniqueIds: $techniqueIds
    tags: $tags
  ) {
    ...RunbookTacticFormDataV2
    __typename
  }
}

fragment RunbookTacticFormDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  description
  methodologies {
    ...RunbookTacticFormMethodologyDataV2
    __typename
  }
  techniques {
    ...RunbookProcedureFormTechniqueDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookTacticFormMethodologyDataV2 on RunbookMethodologyV2 {
  id
  name
  shortName
  __typename
}

fragment RunbookProcedureFormTechniqueDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  tactics {
    id
    name
    shortName
    __typename
  }
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

variables: {
    "id": "clc6irvck00820zo32c4mgdkd",
    "data": {
        "name": "Test Tactic",
        "shortName": "tid",
        "description": "<p>updated description</p>"
    },
    "methodologyIds": [
        "clacwm5nx02m229mqci14ckrd"
    ],
    "techniqueIds": [
        "clacwm5ot02mv29mqevmb44lh"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookTacticUpdateV2):
```json
{
    "data": {
        "runbookTacticUpdateV2": {
            "id": "clc6irvck00820zo32c4mgdkd",
            "name": "Test Tactic",
            "shortName": "tid",
            "description": "<p>updated description</p>",
            "methodologies": [
                {
                    "id": "clacwm5nx02m229mqci14ckrd",
                    "name": "Mitre ATT&CK 11.3",
                    "shortName": "Mitre-11.3",
                    "__typename": "RunbookMethodologyV2"
                }
            ],
            "techniques": [
                {
                    "id": "clacwm5ot02mv29mqevmb44lh",
                    "name": "Extra Window Memory Injection",
                    "shortName": "T1055.011",
                    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly...",
                    "tactics": [
                        {
                            "id": "clacwm5od02mb29mqa5fz3l4q",
                            "name": "Privilege Escalation",
                            "shortName": "TA0004",
                            "__typename": "RunbookTacticV2"
                        },
                        {
                            "id": "clacwm5oh02mf29mqf5andaw8",
                            "name": "Defense Evasion",
                            "shortName": "TA0005",
                            "__typename": "RunbookTacticV2"
                        },
                        {
                            "id": "clc6irvck00820zo32c4mgdkd",
                            "name": "Test Tactic",
                            "shortName": "tid",
                            "__typename": "RunbookTacticV2"
                        }
                    ],
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTechniqueV2"
                }
            ],
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookTacticV2"
        }
    }
}
```

### RunbookTacticDeleteV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Tactics

```graphql
mutation RunbookTacticDeleteV2($id: ID!) {
  runbookTacticDeleteV2(id: $id) {
    ...RunbookTacticListDataV2
    __typename
  }
}

fragment RunbookTacticListDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  isEditable
  methodologies {
    id
    name
    __typename
  }
  __typename
}

variables: {
    "id": "clc6irvck00820zo32c4mgdkd"
}
```

Response 200 (RunbookTacticDeleteV2):
```json
{
    "data": {
        "runbookTacticDeleteV2": {
            "id": "clc6irvck00820zo32c4mgdkd",
            "name": "Test Tactic",
            "shortName": "tid",
            "isEditable": true,
            "methodologies": [
                {
                    "id": "clacwm5nx02m229mqci14ckrd",
                    "name": "Mitre ATT&CK 11.3",
                    "__typename": "RunbookMethodologyV2"
                }
            ],
            "__typename": "RunbookTacticV2"
        }
    }
}
```

### RunbookTechniqueListV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Techniques

StartFragment

Returns a list of Techniques in the RunbooksDB

```graphql
query RunbookTechniqueListV2($args: ListArgs!) {
  runbookTechniqueListV2(args: $args) {
    data {
      ...RunbookTechniqueDataGridV2
      __typename
    }
    meta {
      ...ListMetaData
      __typename
    }
    __typename
  }
}

fragment RunbookTechniqueDataGridV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  isEditable
  updatedAt
  deletedAt
  tactics {
    id
    name
    __typename
  }
  __typename
}

fragment ListMetaData on ListMeta {
  pagination {
    limit
    offset
    total
    __typename
  }
  sort {
    by
    order
    __typename
  }
  filters {
    by
    value
    __typename
  }
  __typename
}

variables: {
    "args": {
        "pagination": {
            "limit": 25,
            "offset": 0
        },
        "sort": [
            {
                "by": "name",
                "order": "DESC"
            }
        ],
        "filters": [
            {
                "by": "methodologyIds",
                "value": []
            },
            {
                "by": "tacticIds",
                "value": []
            },
            {
                "by": "searchTerm",
                "value": ""
            }
        ]
    }
}
```

Response 200 (RunbookTechniqueListV2):
```json
{
    "data": {
        "runbookTechniqueListV2": {
            "data": [
                {
                    "id": "clacwm2mr010s29mqhxcn10dq",
                    "name": "XSL Script Processing",
                    "shortName": "T1220",
                    "description": "Adversaries may bypass application control and obscure execution of code by embedding scripts inside...",
                    "isEditable": false,
                    "updatedAt": "2022-11-11T19:40:39.177Z",
                    "deletedAt": null,
                    "tactics": [
                        {
                            "id": "clacwm193000829mq7bhlcnj1",
                            "name": "Defense Evasion",
                            "__typename": "RunbookTacticV2"
                        }
                    ],
                    "__typename": "RunbookTechniqueV2"
                }
            ],
            "meta": {
                "pagination": {
                    "limit": 25,
                    "offset": 0,
                    "total": 1282,
                    "__typename": "PaginationResult"
                },
                "sort": [
                    {
                        "by": "name",
                        "order": "DESC",
                        "__typename": "SortResult"
                    }
                ],
                "filters": [
                    {
                        "by": "methodologyIds",
                        "value": [],
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "tacticIds",
                        "value": [],
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "searchTerm",
                        "value": "",
                        "__typename": "FilterResult"
                    }
                ],
                "__typename": "ListMeta"
            },
            "__typename": "RunbookTechniqueListV2"
        }
    }
}
```

### RunbookTechniqueDetailV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Techniques

Returns the data for a RunbooksV2 Technique

```graphql
query RunbookTechniqueDetailV2($techniqueId: ID!) {
  runbookTechniqueV2(id: $techniqueId) {
    id
    name
    shortName
    description
    procedures {
      id
      name
      shortName
      techniques {
        ...RunbookProcedureDetailTechniqueV2
        __typename
      }
      __typename
    }
    tactics {
      ...RunbookTacticDetailV2
      __typename
    }
    tags {
      id
      tag
      __typename
    }
    __typename
  }
}

fragment RunbookProcedureDetailTechniqueV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  tactics {
    id
    name
    methodologies {
      id
      name
      __typename
    }
    __typename
  }
  __typename
}

fragment RunbookTacticDetailV2 on RunbookTacticV2 {
  ...RunbookTacticFormDataV2
  __typename
}

fragment RunbookTacticFormDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  description
  methodologies {
    ...RunbookTacticFormMethodologyDataV2
    __typename
  }
  techniques {
    ...RunbookProcedureFormTechniqueDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookTacticFormMethodologyDataV2 on RunbookMethodologyV2 {
  id
  name
  shortName
  __typename
}

fragment RunbookProcedureFormTechniqueDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  tactics {
    id
    name
    shortName
    __typename
  }
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

variables: {
    "techniqueId": "clacwm6s003t829mqffsr5amz"
}
```

Response 200 (RunbookTechniqueDetailV2):
```json
{
    "data": {
        "runbookTechniqueV2": {
            "id": "clacwm6s003t829mqffsr5amz",
            "name": "XSL Script Processing",
            "shortName": "T1220",
            "description": "Adversaries may bypass application control and obscure execution of code by embedding scripts inside...",
            "procedures": [
                {
                    "id": "clacwm3vl020x29mq9dd5gz4c",
                    "name": "MSXSL Bypass using local files",
                    "shortName": "T1220",
                    "techniques": [
                        {
                            "id": "clacwm6s003t829mqffsr5amz",
                            "name": "XSL Script Processing",
                            "shortName": "T1220",
                            "tactics": [
                                {
                                    "id": "clacwm5oh02mf29mqf5andaw8",
                                    "name": "Defense Evasion",
                                    "methodologies": [
                                        {
                                            "id": "clacwm5nx02m229mqci14ckrd",
                                            "name": "Mitre ATT&CK 11.3",
                                            "__typename": "RunbookMethodologyV2"
                                        }
                                    ],
                                    "__typename": "RunbookTacticV2"
                                }
                            ],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "__typename": "RunbookProcedureV2"
                }
            ],
            "tactics": [
                {
                    "id": "clacwm5oh02mf29mqf5andaw8",
                    "name": "Defense Evasion",
                    "shortName": "TA0005",
                    "description": "The adversary is trying to avoid being detected.\n\nDefense Evasion consists of techniques that adversaries...",
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "techniques": [
                        {
                            "id": "clacwm5r702po29mqga8ohsgg",
                            "name": "Rootkit",
                            "shortName": "T1014",
                            "description": "Adversaries may use rootkits to hide the presence of programs, files, network connections, services...",
                            "tactics": [
                                {
                                    "id": "clacwm5oh02mf29mqf5andaw8",
                                    "name": "Defense Evasion",
                                    "shortName": "TA0005",
                                    "__typename": "RunbookTacticV2"
                                }
                            ],
                            "methodologies": [
                                {
                                    "id": "clacwm5nx02m229mqci14ckrd",
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "__typename": "RunbookTechniqueV2"
                        },
                        {
                            "id": "clacwm5ot02mv29mqevmb44lh",
                            "name": "Extra Window Memory Injection",
                            "shortName": "T1055.011",
                            "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade...",
                            "tactics": [
                                {
                                    "id": "clacwm5od02mb29mqa5fz3l4q",
                                    "name": "Privilege Escalation",
                                    "shortName": "TA0004",
                                    "__typename": "RunbookTacticV2"
                                },
                                {
                                    "id": "clacwm5oh02mf29mqf5andaw8",
                                    "name": "Defense Evasion",
                                    "shortName": "TA0005",
                                    "__typename": "RunbookTacticV2"
                                }
                            ],
                            "methodologies": [
                                {
                                    "id": "clacwm5nx02m229mqci14ckrd",
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "tags": [],
                    "__typename": "RunbookTacticV2"
                }
            ],
            "tags": [],
            "__typename": "RunbookTechniqueV2"
        }
    }
}
```

### RunbookTechniqueCreateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Techniques

```graphql
mutation RunbookTechniqueCreateV2($data: RunbookTechniqueInputV2!, $tacticIds: [ID!], $procedureIds: [ID!], $tags: [String!]) {
  runbookTechniqueCreateV2(
    input: $data
    tacticIds: $tacticIds
    procedureIds: $procedureIds
    tags: $tags
  ) {
    ...RunbookTechniqueFormDataV2
    __typename
  }
}

fragment RunbookTechniqueFormDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  procedures {
    ...RunbookProcedureFormDataV2
    __typename
  }
  tactics {
    ...RunbookTacticListDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookProcedureFormDataV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  isEditable
  repositoryId
  tags {
    id
    tag
    __typename
  }
  executionSteps {
    id
    description
    successCriteria
    sortOrder
    __typename
  }
  techniques {
    ...RunbookProcedureFormTechniqueDataV2
    __typename
  }
  __typename
}

fragment RunbookProcedureFormTechniqueDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  tactics {
    id
    name
    shortName
    __typename
  }
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

fragment RunbookTacticListDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  isEditable
  methodologies {
    id
    name
    __typename
  }
  __typename
}

variables: {
    "data": {
        "name": "Test Technique",
        "shortName": "tecid",
        "description": "<p>desc</p>"
    },
    "procedureIds": [
        "clacwmagf06jt29mqhl9o3rr0"
    ],
    "tacticIds": [
        "clacwm5o202m329mq67o51mj9"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookTechniqueCreateV2):
```json
{
    "data": {
        "runbookTechniqueCreateV2": {
            "id": "clc6ksea6008i0zo34gbvajea",
            "name": "Test Technique",
            "shortName": "tecid",
            "description": "<p>desc</p>",
            "procedures": [
                {
                    "id": "clacwmagf06jt29mqhl9o3rr0",
                    "name": "MAZE FTP Upload",
                    "shortName": "T1048.003",
                    "description": "This test simulates MAZE's ransomware's ability to exfiltrate data via FTP.\nUpon successful execution, all 7z files within the %windir%\\temp directory...",
                    "isEditable": false,
                    "repositoryId": "clacwm17b000029mqcwg1etc9",
                    "tags": [],
                    "executionSteps": [
                        {
                            "id": "clacwmagg06ju29mq9em4cm7d",
                            "description": "$Dir_to_copy = \"$env:windir\\temp\"\n$ftp = \"ftp://#{ftp_server}/\"\n$web_client = New-Object System.Net.WebClient\n$web_client.Credentials...",
                            "successCriteria": null,
                            "sortOrder": 0,
                            "__typename": "RunbookProcedureStep"
                        }
                    ],
                    "techniques": [
                        {
                            "id": "clc6ksea6008i0zo34gbvajea",
                            "name": "Test Technique",
                            "shortName": "tecid",
                            "description": "<p>desc</p>",
                            "tactics": [
                                {
                                    "id": "clacwm5o202m329mq67o51mj9",
                                    "name": "Credential Access",
                                    "shortName": "TA0006",
                                    "__typename": "RunbookTacticV2"
                                }
                            ],
                            "methodologies": [
                                {
                                    "id": "clacwm5nx02m229mqci14ckrd",
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "__typename": "RunbookProcedureV2"
                }
            ],
            "tactics": [
                {
                    "id": "clacwm5o202m329mq67o51mj9",
                    "name": "Credential Access",
                    "shortName": "TA0006",
                    "isEditable": false,
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                }
            ],
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookTechniqueV2"
        }
    }
}
```

### RunbookTechniqueUpdateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Techniques

```graphql
mutation RunbookTechniqueUpdateV2($data: RunbookTechniqueInputV2!, $id: ID!, $tacticIds: [ID!], $procedureIds: [ID!], $tags: [String!]) {
  runbookTechniqueUpdateV2(
    input: $data
    id: $id
    tacticIds: $tacticIds
    procedureIds: $procedureIds
    tags: $tags
  ) {
    ...RunbookTechniqueFormDataV2
    __typename
  }
}

fragment RunbookTechniqueFormDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  procedures {
    ...RunbookProcedureFormDataV2
    __typename
  }
  tactics {
    ...RunbookTacticListDataV2
    __typename
  }
  tags {
    id
    tag
    __typename
  }
  __typename
}

fragment RunbookProcedureFormDataV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  isEditable
  repositoryId
  tags {
    id
    tag
    __typename
  }
  executionSteps {
    id
    description
    successCriteria
    sortOrder
    __typename
  }
  techniques {
    ...RunbookProcedureFormTechniqueDataV2
    __typename
  }
  __typename
}

fragment RunbookProcedureFormTechniqueDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  tactics {
    id
    name
    shortName
    __typename
  }
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

fragment RunbookTacticListDataV2 on RunbookTacticV2 {
  id
  name
  shortName
  isEditable
  methodologies {
    id
    name
    __typename
  }
  __typename
}

variables: {
    "id": "clc6ksea6008i0zo34gbvajea",
    "data": {
        "name": "Test Technique",
        "shortName": "tecid",
        "description": "<p>updated description</p>"
    },
    "procedureIds": [
        "clacwmagf06jt29mqhl9o3rr0"
    ],
    "tacticIds": [
        "clacwm5o202m329mq67o51mj9"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookTechniqueUpdateV2):
```json
{
    "data": {
        "runbookTechniqueUpdateV2": {
            "id": "clc6ksea6008i0zo34gbvajea",
            "name": "Test Technique",
            "shortName": "tecid",
            "description": "<p>updated description</p>",
            "procedures": [
                {
                    "id": "clacwmagf06jt29mqhl9o3rr0",
                    "name": "MAZE FTP Upload",
                    "shortName": "T1048.003",
                    "description": "This test simulates MAZE's ransomware's ability to exfiltrate data via FTP.\nUpon successful execution, all 7z files within the %windir%\\temp directory...",
                    "isEditable": false,
                    "repositoryId": "clacwm17b000029mqcwg1etc9",
                    "tags": [],
                    "executionSteps": [
                        {
                            "id": "clacwmagg06ju29mq9em4cm7d",
                            "description": "$Dir_to_copy = \"$env:windir\\temp\"\n$ftp = \"ftp://#{ftp_server}/\"\n$web_client = New-Object System.Net.WebClient\n$web_client.Credentials...",
                            "successCriteria": null,
                            "sortOrder": 0,
                            "__typename": "RunbookProcedureStep"
                        }
                    ],
                    "techniques": [
                        {
                            "id": "clc6ksea6008i0zo34gbvajea",
                            "name": "Test Technique",
                            "shortName": "tecid",
                            "description": "<p>updated description</p>",
                            "tactics": [
                                {
                                    "id": "clacwm5o202m329mq67o51mj9",
                                    "name": "Credential Access",
                                    "shortName": "TA0006",
                                    "__typename": "RunbookTacticV2"
                                }
                            ],
                            "methodologies": [
                                {
                                    "id": "clacwm5nx02m229mqci14ckrd",
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "__typename": "RunbookProcedureV2"
                }
            ],
            "tactics": [
                {
                    "id": "clacwm5o202m329mq67o51mj9",
                    "name": "Credential Access",
                    "shortName": "TA0006",
                    "isEditable": false,
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTacticV2"
                }
            ],
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "__typename": "RunbookTechniqueV2"
        }
    }
}
```

### RunbookTechniqueDeleteV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Techniques

```graphql
mutation RunbookTechniqueDeleteV2($id: ID!) {
  runbookTechniqueDeleteV2(id: $id) {
    ...RunbookTechniqueDataGridV2
    __typename
  }
}

fragment RunbookTechniqueDataGridV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  isEditable
  updatedAt
  deletedAt
  tactics {
    id
    name
    __typename
  }
  __typename
}

variables: {
    "id": "clc6ksea6008i0zo34gbvajea"
}
```

Response 200 (RunbookTechniqueDeleteV2):
```json
{
    "data": {
        "runbookTechniqueDeleteV2": {
            "id": "clc6ksea6008i0zo34gbvajea",
            "name": "Test Technique",
            "shortName": "tecid",
            "description": "<p>updated description</p>",
            "isEditable": true,
            "updatedAt": "2022-12-27T18:45:42.563Z",
            "deletedAt": "2022-12-27T18:46:24.557Z",
            "tactics": [
                {
                    "id": "clacwm5o202m329mq67o51mj9",
                    "name": "Credential Access",
                    "__typename": "RunbookTacticV2"
                }
            ],
            "__typename": "RunbookTechniqueV2"
        }
    }
}
```

### RunbookProcedureListV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Procedures

Returns a list of Procedures in the RunbooksDB

```graphql
query RunbookProcedureListV2($args: ListArgs!) {
  runbookProcedureListV2(args: $args) {
    data {
      ...RunbookProcedureDataGridV2
      __typename
    }
    meta {
      ...ListMetaData
      __typename
    }
    __typename
  }
}

fragment RunbookProcedureDataGridV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  isEditable
  updatedAt
  deletedAt
  repository {
    id
    name
    shortName
    type
    __typename
  }
  techniques {
    id
    name
    shortName
    methodologies {
      name
      shortName
      __typename
    }
    __typename
  }
  __typename
}

fragment ListMetaData on ListMeta {
  pagination {
    limit
    offset
    total
    __typename
  }
  sort {
    by
    order
    __typename
  }
  filters {
    by
    value
    __typename
  }
  __typename
}

variables: {
    "args": {
        "pagination": {
            "limit": 25,
            "offset": 0
        },
        "sort": [
            {
                "by": "shortName",
                "order": "DESC"
            },
            {
                "by": "name",
                "order": "DESC"
            }
        ],
        "filters": [
            {
                "by": "tacticIds",
                "value": []
            },
            {
                "by": "methodologyIds",
                "value": []
            },
            {
                "by": "searchTerm",
                "value": ""
            }
        ]
    }
}
```

Response 200 (RunbookProcedureListV2):
```json
{
    "data": {
        "runbookProcedureListV2": {
            "data": [
                {
                    "id": "clacwm7pe04hn29mqbu96b4n7",
                    "name": "Plist Modification",
                    "shortName": "T1647",
                    "description": "Modify MacOS plist file in one of two directories\n\n\n**Supported Platforms:** macos\n\n",
                    "isEditable": false,
                    "updatedAt": "2022-11-11T19:40:47.618Z",
                    "deletedAt": null,
                    "repository": {
                        "id": "clacwm17b000029mqcwg1etc9",
                        "name": "PlexTrac Curated",
                        "shortName": "PlexTrac",
                        "type": "curated",
                        "__typename": "RunbookRepositoryV2"
                    },
                    "techniques": [
                        {
                            "id": "clacwm6bg03ag29mq06ho26ob",
                            "name": "Plist File Modification",
                            "shortName": "T1647",
                            "methodologies": [
                                {
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "__typename": "RunbookProcedureV2"
                },
                {
                    "id": "clacwm7fy048w29mqbrfx4mi1",
                    "name": "WinPwn - Reflectively load Mimik@tz into memory",
                    "shortName": "T1620",
                    "description": "Reflectively load Mimik@tz into memory technique via function of WinPwn\n\n**Supported Platforms:** windows\n\n",
                    "isEditable": false,
                    "updatedAt": "2022-11-11T19:40:47.279Z",
                    "deletedAt": null,
                    "repository": {
                        "id": "clacwm17b000029mqcwg1etc9",
                        "name": "PlexTrac Curated",
                        "shortName": "PlexTrac",
                        "type": "curated",
                        "__typename": "RunbookRepositoryV2"
                    },
                    "techniques": [
                        {
                            "id": "clacwm627031029mq3yggfznc",
                            "name": "Reflective Code Loading",
                            "shortName": "T1620",
                            "methodologies": [
                                {
                                    "name": "Mitre ATT&CK 11.3",
                                    "shortName": "Mitre-11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "__typename": "RunbookTechniqueV2"
                        }
                    ],
                    "__typename": "RunbookProcedureV2"
                }
            ],
            "meta": {
                "pagination": {
                    "limit": 25,
                    "offset": 0,
                    "total": 1163,
                    "__typename": "PaginationResult"
                },
                "sort": [
                    {
                        "by": "shortName",
                        "order": "DESC",
                        "__typename": "SortResult"
                    },
                    {
                        "by": "name",
                        "order": "DESC",
                        "__typename": "SortResult"
                    }
                ],
                "filters": [
                    {
                        "by": "tacticIds",
                        "value": [],
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "methodologyIds",
                        "value": [],
                        "__typename": "FilterResult"
                    },
                    {
                        "by": "searchTerm",
                        "value": "",
                        "__typename": "FilterResult"
                    }
                ],
                "__typename": "ListMeta"
            },
            "__typename": "RunbookProcedureListV2"
        }
    }
}
```

### RunbookProcedureDetailV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Procedures

Returns the data for a RunbooksV2 Procedure

```graphql
query RunbookProcedureDetailV2($id: ID!) {
  runbookProcedureV2(id: $id) {
    id
    name
    description
    shortName
    isEditable
    repository {
      id
      name
      shortName
      __typename
    }
    tags {
      id
      tag
      __typename
    }
    executionSteps {
      id
      description
      successCriteria
      __typename
    }
    techniques {
      ...RunbookProcedureDetailTechniqueV2
      __typename
    }
    __typename
  }
}

fragment RunbookProcedureDetailTechniqueV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  tactics {
    id
    name
    methodologies {
      id
      name
      __typename
    }
    __typename
  }
  __typename
}

variables: {
    "id": "clacwm7pe04hn29mqbu96b4n7"
}
```

Response 200 (RunbookProcedureDetailV2):
```json
{
    "data": {
        "runbookProcedureV2": {
            "id": "clacwm7pe04hn29mqbu96b4n7",
            "name": "Plist Modification",
            "description": "Modify MacOS plist file in one of two directories\n\n\n**Supported Platforms:** macos\n\n",
            "shortName": "T1647",
            "isEditable": false,
            "repository": {
                "id": "clacwm17b000029mqcwg1etc9",
                "name": "PlexTrac Curated",
                "shortName": "PlexTrac",
                "__typename": "RunbookRepositoryV2"
            },
            "tags": [],
            "executionSteps": [
                {
                    "id": "clacwm7pe04ho29mqds8u98xg",
                    "description": "1. Modify a .plist in\n\n    /Library/Preferences\n\n    OR\n\n    ~/Library/Preferences\n\n2. Subsequently, follow the steps for adding and running via [Launch Agent](Persistence/Launch_Agent.md)\n",
                    "successCriteria": null,
                    "__typename": "RunbookProcedureStep"
                }
            ],
            "techniques": [
                {
                    "id": "clacwm6bg03ag29mq06ho26ob",
                    "name": "Plist File Modification",
                    "shortName": "T1647",
                    "tactics": [
                        {
                            "id": "clacwm5oh02mf29mqf5andaw8",
                            "name": "Defense Evasion",
                            "methodologies": [
                                {
                                    "id": "clacwm5nx02m229mqci14ckrd",
                                    "name": "Mitre ATT&CK 11.3",
                                    "__typename": "RunbookMethodologyV2"
                                }
                            ],
                            "__typename": "RunbookTacticV2"
                        }
                    ],
                    "__typename": "RunbookTechniqueV2"
                }
            ],
            "__typename": "RunbookProcedureV2"
        }
    }
}
```

### RunbookProcedureCreateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Procedures

```graphql
mutation RunbookProcedureCreateV2($data: RunbookProcedureInputV2!, $executionSteps: [RunbookProcedureExecutionStepInput!]!, $techniqueIds: [ID!], $tags: [String!]) {
  runbookProcedureCreateV2(
    input: $data
    executionSteps: $executionSteps
    techniqueIds: $techniqueIds
    tags: $tags
  ) {
    ...RunbookProcedureFormDataV2
    __typename
  }
}

fragment RunbookProcedureFormDataV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  isEditable
  repositoryId
  tags {
    id
    tag
    __typename
  }
  executionSteps {
    id
    description
    successCriteria
    sortOrder
    __typename
  }
  techniques {
    ...RunbookProcedureFormTechniqueDataV2
    __typename
  }
  __typename
}

fragment RunbookProcedureFormTechniqueDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  tactics {
    id
    name
    shortName
    __typename
  }
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

variables: {
    "data": {
        "name": "Test Procedure",
        "shortName": "pid",
        "repositoryId": "clc0rr6v500540zo31c5i4cz2",
        "description": "<p>desc</p>"
    },
    "executionSteps": [
        {
            "description": "<p>step 1</p>",
            "successCriteria": "<p>did the thing</p>"
        }
    ],
    "techniqueIds": [
        "clacwm5ot02mv29mqevmb44lh"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookProcedureCreateV2):
```json
{
    "data": {
        "runbookProcedureCreateV2": {
            "id": "clc6l9ob7007n0zpc5ugd1hh6",
            "name": "Test Procedure",
            "shortName": "pid",
            "description": "<p>desc</p>",
            "isEditable": true,
            "repositoryId": "clc0rr6v500540zo31c5i4cz2",
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "executionSteps": [
                {
                    "id": "clc6l9oc2007o0zpcaepj0005",
                    "description": "<p>step 1</p>",
                    "successCriteria": "<p>did the thing</p>",
                    "sortOrder": 0,
                    "__typename": "RunbookProcedureStep"
                }
            ],
            "techniques": [
                {
                    "id": "clacwm5ot02mv29mqevmb44lh",
                    "name": "Extra Window Memory Injection",
                    "shortName": "T1055.011",
                    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly...",
                    "tactics": [
                        {
                            "id": "clacwm5od02mb29mqa5fz3l4q",
                            "name": "Privilege Escalation",
                            "shortName": "TA0004",
                            "__typename": "RunbookTacticV2"
                        },
                        {
                            "id": "clacwm5oh02mf29mqf5andaw8",
                            "name": "Defense Evasion",
                            "shortName": "TA0005",
                            "__typename": "RunbookTacticV2"
                        }
                    ],
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTechniqueV2"
                }
            ],
            "__typename": "RunbookProcedureV2"
        }
    }
}
```

### RunbookProcedureUpdateV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Procedures

```graphql
mutation RunbookProcedureUpdateV2($id: ID!, $data: RunbookProcedureInputV2!, $executionSteps: [RunbookProcedureExecutionStepInput!]!, $techniqueIds: [ID!], $tags: [String!]) {
  runbookProcedureUpdateV2(
    id: $id
    input: $data
    executionSteps: $executionSteps
    techniqueIds: $techniqueIds
    tags: $tags
  ) {
    ...RunbookProcedureFormDataV2
    __typename
  }
}

fragment RunbookProcedureFormDataV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  isEditable
  repositoryId
  tags {
    id
    tag
    __typename
  }
  executionSteps {
    id
    description
    successCriteria
    sortOrder
    __typename
  }
  techniques {
    ...RunbookProcedureFormTechniqueDataV2
    __typename
  }
  __typename
}

fragment RunbookProcedureFormTechniqueDataV2 on RunbookTechniqueV2 {
  id
  name
  shortName
  description
  tactics {
    id
    name
    shortName
    __typename
  }
  methodologies {
    id
    name
    shortName
    __typename
  }
  __typename
}

variables: {
    "id": "clc6l9ob7007n0zpc5ugd1hh6",
    "data": {
        "name": "Test Procedure",
        "shortName": "pid",
        "repositoryId": "clc0rr6v500540zo31c5i4cz2",
        "description": "<p>updated description</p>"
    },
    "executionSteps": [
        {
            "description": "<p>step 1</p>",
            "successCriteria": "<p>did the thing</p>"
        }
    ],
    "techniqueIds": [
        "clacwm5ot02mv29mqevmb44lh"
    ],
    "tags": [
        "test_tag"
    ]
}
```

Response 200 (RunbookProcedureUpdateV2):
```json
{
    "data": {
        "runbookProcedureUpdateV2": {
            "id": "clc6l9ob7007n0zpc5ugd1hh6",
            "name": "Test Procedure",
            "shortName": "pid",
            "description": "<p>updated description</p>",
            "isEditable": true,
            "repositoryId": "clc0rr6v500540zo31c5i4cz2",
            "tags": [
                {
                    "id": "clc6i7cro007o0zn5flatf2al",
                    "tag": "test_tag",
                    "__typename": "RunbookTag"
                }
            ],
            "executionSteps": [
                {
                    "id": "clc6lcnod00830zn5h0s6gwuv",
                    "description": "<p>step 1</p>",
                    "successCriteria": "<p>did the thing</p>",
                    "sortOrder": 0,
                    "__typename": "RunbookProcedureStep"
                }
            ],
            "techniques": [
                {
                    "id": "clacwm5ot02mv29mqevmb44lh",
                    "name": "Extra Window Memory Injection",
                    "shortName": "T1055.011",
                    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate...",
                    "tactics": [
                        {
                            "id": "clacwm5od02mb29mqa5fz3l4q",
                            "name": "Privilege Escalation",
                            "shortName": "TA0004",
                            "__typename": "RunbookTacticV2"
                        },
                        {
                            "id": "clacwm5oh02mf29mqf5andaw8",
                            "name": "Defense Evasion",
                            "shortName": "TA0005",
                            "__typename": "RunbookTacticV2"
                        }
                    ],
                    "methodologies": [
                        {
                            "id": "clacwm5nx02m229mqci14ckrd",
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTechniqueV2"
                }
            ],
            "__typename": "RunbookProcedureV2"
        }
    }
}
```

### RunbookProcedureDeleteV2
Folder: Runbooks / Runbooks v2 / RunbooksDB / Procedures

```graphql
mutation RunbookProcedureDeleteV2($id: ID!) {
  runbookProcedureDeleteV2(id: $id) {
    ...RunbookProcedureDataGridV2
    __typename
  }
}

fragment RunbookProcedureDataGridV2 on RunbookProcedureV2 {
  id
  name
  shortName
  description
  isEditable
  updatedAt
  deletedAt
  repository {
    id
    name
    shortName
    type
    __typename
  }
  techniques {
    id
    name
    shortName
    methodologies {
      name
      shortName
      __typename
    }
    __typename
  }
  __typename
}

variables: {
    "id": "clc6l9ob7007n0zpc5ugd1hh6"
}
```

Response 200 (RunbookProcedureDeleteV2):
```json
{
    "data": {
        "runbookProcedureDeleteV2": {
            "id": "clc6l9ob7007n0zpc5ugd1hh6",
            "name": "Test Procedure",
            "shortName": "pid",
            "description": "<p>updated description</p>",
            "isEditable": false,
            "updatedAt": "2022-12-27T18:58:13.587Z",
            "deletedAt": "2022-12-27T18:58:37.307Z",
            "repository": {
                "id": "clc0rr6v500540zo31c5i4cz2",
                "name": "Test RB Repo",
                "shortName": "test",
                "type": "managed",
                "__typename": "RunbookRepositoryV2"
            },
            "techniques": [
                {
                    "id": "clacwm5ot02mv29mqevmb44lh",
                    "name": "Extra Window Memory Injection",
                    "shortName": "T1055.011",
                    "methodologies": [
                        {
                            "name": "Mitre ATT&CK 11.3",
                            "shortName": "Mitre-11.3",
                            "__typename": "RunbookMethodologyV2"
                        }
                    ],
                    "__typename": "RunbookTechniqueV2"
                }
            ],
            "__typename": "RunbookProcedureV2"
        }
    }
}
```

### clientAsset
Folder: Graph QL Queries

```graphql
query clientAsset ($clientId: ID!, $id: ID!) {
    clientAsset (clientId: $clientId, id: $id) {
        client {
            id
            name
        }
        created
        description
        findings {
            id
            instances {
                report_flaw_title
                report_id
                report_severity
                report_status
            }
            severity
            status
            title
        }
        id
        name
    }
}

variables: {
  "clientId": 0,
  "id": 0
}
```

### FindingUpdate
Folder: Graph QL Mutations

Update individual properties on a finding.

StartFragment

NOTE: The Custom Fields tab of a finding in the platform is considered a single property.

"data": {
    "fields": [
        {
            "key": "synopsis",
            "label": "Synopsis",
            "value": "The remote OS or service pack is no longer supported. test"
        },
        {
            "key": "evidence",
            "label": "Evidence",
            "value": ""
        }
    ]
}

This means to update to any custom field key, label, or value you will need to send the entire fields object in the data property.

EndFr

```graphql
mutation FindingUpdate($clientId: Int!, $data: FindingUpdateInput!, $findingId: Float!, $reportId: Int!) {
  findingUpdate(
    clientId: $clientId
    data: $data
    findingId: $findingId
    reportId: $reportId
  ) {
    ... on FindingUpdateSuccess {
      finding {
        ...FindingFragment
        __typename
      }
      __typename
    }
    __typename
  }
}

fragment FindingFragment on Finding {
  assignedTo
  closedAt
  createdAt
  code_samples {
    caption
    code
    id
    __typename
  }
  common_identifiers {
    CVE {
      name
      id
      year
      link
      __typename
    }
    CWE {
      name
      id
      link
      __typename
    }
    __typename
  }
  description
  exhibits {
    assets {
      asset
      id
      __typename
    }
    caption
    exhibitID
    index
    type
    __typename
  }
  fields {
    key
    label
    value
    __typename
  }
  flaw_id
  includeEvidence
  recommendations
  references
  scores
  selectedScore
  severity
  source
  status
  subStatus
  tags
  title
  visibility
  calculated_severity
  risk_score {
    CVSS3_1 {
      overall
      vector
      subScore {
        base
        temporal
        environmental
        __typename
      }
      __typename
    }
    CVSS3 {
      overall
      vector
      subScore {
        base
        temporal
        environmental
        __typename
      }
      __typename
    }
    CVSS2 {
      overall
      vector
      subScore {
        base
        temporal
        __typename
      }
      __typename
    }
    CWSS {
      overall
      vector
      subScore {
        base
        environmental
        attackSurface
        __typename
      }
      __typename
    }
    __typename
  }
  hackerOneData {
    bountyAmount
    programId
    programName
    remoteId
    __typename
  }
  snykData {
    issueType
    pkgName
    issueUrl
    identifiers {
      CVE
      CWE
      __typename
    }
    exploitMaturity
    patches
    nearestFixedInVersion
    isMaliciousPackage
    violatedPolicyPublicId
    introducedThrough
    fixInfo {
      isUpgradable
      isPinnable
      isPatchable
      isFixable
      isPartiallyFixable
      nearestFixedInVersion
      __typename
    }
    __typename
  }
  edgescanData {
    id
    portal_url
    details {
      html
      id
      orginal_detail_hash
      parameter_name
      parameter_type
      port
      protocol
      screenshot_urls {
        file
        id
        medium_thumb
        small_thumb
        __typename
      }
      src
      type
      __typename
    }
    __typename
  }
  __typename
}

variables: {
    "clientId": 1045,
    "reportId": 500790,
    "findingId": 108797,
    "data": {
        "severity": "Medium"
    }
}
```

### NarrativeUpdate
Folder: Graph QL Mutations

You can create a new report narrative by passing in a new report narrative object with a new unique CUID value in the id property.

```graphql
mutation NarrativeUpdate($clientId: Int!, $data: [NarrativeInput!]!, $reportId: Int!, $tenantId: Int!) {
  narrativeUpdate(
    clientId: $clientId
    data: $data
    reportId: $reportId
    tenantId: $tenantId
  ) {
    ...NarrativeFragment
    __typename
  }
}

fragment NarrativeFragment on Narrative {
  id
  label
  tags
  text
  titleCommentThreadId
  isFromNarrativesDB
  __typename
}

variables: {
  "clientId": 1045,
  "data": [
    {
      "id": "clw8551sr01cf0gjze5wf50qt",
      "label": "Test Narrative",
      "tags": [
        "test_tag"
      ],
      "text": "<p>updated narrative text</p>",
      "repository": null,
      "isFromNarrativesDB": false,
      "titleCommentThreadId": null
    }
  ],
  "reportId": 345951070,
  "tenantId": 0
}
```
