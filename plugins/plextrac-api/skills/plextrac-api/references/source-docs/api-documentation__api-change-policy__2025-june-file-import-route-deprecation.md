# 2025 June - File Import Route Deprecation

### 🧾 Summary

We are deprecating the existing `POST /api/v2/client/{clientId}/report/{reportId}/importAsync/{source}` endpoint (named [**Add Findings from File Imports V2**](https://api-docs.plextrac.com/#807bb99a-5f1d-4503-8ae1-23eac3c9f37b) in our docs) in favor of a new, more reliable, multi-step asynchronous import flow. This update improves backend performance and makes the platform more responsive during heavy import activity.

If you’ve built an integration or script that uses the `POST /api/v2/client/{clientId}/report/{reportId}/importAsync/{source}` endpoint, you will need to migrate to the new process before the removal date.

***

### 🗓 Deprecation Timeline

* Deprecation Date: June 23, 2025 (the replacement option will be available starting in v2.18)
* Removal Date: October 8, 2025 - v2.22

***

### 📋 Details

#### 📌 Existing Workflow

Current imports are handled via:

`POST /api/v2/client/{clientId}/report/{reportId}/importAsync/{source}`

* The upload is asynchronous, but the actual import runs on the main API thread pool.
* This can degrade performance and responsiveness when multiple imports occur at once or the platform is experiencing heavy user load.

#### 🔁 Replacement Workflow

The new import process separates file upload and import execution:

1. **Request Presigned URL**\
   `POST /api/v2/presigned-url`
2. **Upload File to MinIO**\
   Use the returned url from step 1 via a PUT request.
3. **Trigger Import**\
   `POST /api/v2/client/{clientId}/report/{reportId}/preuploaded-import/{source}`\
   Pass the returned `key` from step 1 along with the filename, any tag metadata, and parser action option.
4. **Check Import Status**\
   `GET /api/v2/my-imports`

The actual import now runs on a dedicated worker queue, decoupled from the API thread.

#### 💡 Why This Change?

This update brings several backend improvements:

* **True background imports**: Jobs are no longer tied to the API thread.
* **Better system responsiveness**: Main thread stays available for interactive user actions.
* **Improved visibility**: Import status is queryable via a structured `/api/v2/my-imports` endpoint.
* **More scalable architecture**: MinIO upload is streaming, so it supports large files without loading into memory.

***

### 🛠 Required Developer Changes

#### ✅ How to Know If You're Affected

You are affected if you call:

`POST /api/v2/client/{clientId}/report/{reportId}/importAsync/{source}`

…in any script, integration, or automation. This was previously the primary way to upload findings with our file parsers from scan tools like Nessus, Burp, Qualys, etc.

#### 🔄 What You Need to Do

Update your integration to follow the new multi-step flow.

Step-by-step example:

**1. Request a Presigned Upload URL**

```typescript
// Fetch presigned url from PlextracApi
const presignedUrlResponse = await axios.post(
    "https://plextrac.localhost/api/v2/presigned-url",
    { name: fileName },
    { headers: { "authorization": authToken, "content-type": "application/json" }}
);
```

**Response:**

```json
{
    "status": "success",
    "key": "cmaod32be000i0hovg1oz04b4/burp_sample_small.xml",
    "url": "https://plextrac.localhost/cloud/uploads/cmaod32be000i0hovg1oz04b4/burp_sample_small.xml?..."
}
```

**2. Upload File to MinIO**

```typescript
// Ready file data to be uploaded as a stream
const fileStream = fs.createReadStream(filePath);

// Upload file to Minio using presigned url
const minioUploadResponse = await axios.put(
    presignedUrlResponse.data.url,
    fileStream,
    {
        headers: { "Content-Type": "application/octet-stream" },
        onUploadProgress(progressEvent) {
            if (progressEvent?.total === undefined) return;
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            console.log(`Upload progress: ${percentCompleted}%`);
        }
    }
);
```

**Note**: `onUploadProgress` is supported in Axios and can be used to provide user feedback on large files. Different solutions can be found in different request libraries if needed.

**3. Initiate Import via Background Worker**

```typescript
// Initiate asynchronous import process
const asyncImportResponse = await axios.post(
    "https://plextrac.localhost/api/v2/client/{clientId}/report/{reportId}/preuploaded-import/{source}",
    {
         tags: JSON.stringify({ assets: [], findings: [] }),
         useParserActions: false,
         key: presignedUrlResponse.data.key,
         fileName: fileName,
    },
    {
        headers: {
            "authorization": authToken,
            "content-type": "application/json"
        }
    }
);
```

This request returns a status based on the success of queuing up the import job. You need to use the `/api/v2/my-imports` to determine the success of the import job. If you uploaded a malformed or invalid file for the source selected, this will still queue up the import job successfully.

* `source` corresponds to the file parser (e.g. nessus, burp, qualys), match existing usage from the V2 import
* `key` is the same object storage path returned in step 1
* `tags` and `useParserActions` match existing usage from the V2 import

**Response:**

```json
{
    "status": "success",
    "operationId": "1dbc57cb-dd90-403b-a3e1-f411a66bd922",
    "importJob": {
        "id": "1dbc57cb-dd90-403b-a3e1-f411a66bd922",
        "user_id": 933708862,
        "user_email": "test.email@plextrac.com",
        "tenant_id": 0,
        "client_id": 70891,
        "report_id": 543658528,
        "source": "burp",
        "file_location": "cmapk4wtz000j0hov3pqe5foy/burp_sample_small.xml",
        "original_filename": "burp_sample_small.xml",
        "file_type": "text/xml",
        "file_size": "123625",
        "parser_actions_enabled": false,
        "processed_bytes": "0",
        "processed_findings": 0,
        "processed_assets": 0,
        "processed_finding_assets": 0,
        "processed_evidence": 0,
        "asset_tags": [],
        "finding_tags": [],
        "created_at": "2025-05-15T16:02:00.232Z",
        "last_updated_at": "2025-05-15T16:02:00.232Z",
        "failure_notified_at": null,
        "status": "IN QUEUE",
        "error_status": null
    }
}
```

**4. (Optional) Monitor Import Status**

```typescript
const importStatus = await axios.get(
    "https://plextrac.localhost/api/v2/my-imports",
    {
        headers: {
            "authorization": authToken,
            "content-type": "application/json"
        }
    }
);
```

This endpoint shows the list of recent imports and their status. A specific import job can be found by matching on the `key` which is the `operationId` returned when the import was started.

**Response:**

```json
[
    {
        "key": "1dbc57cb-dd90-403b-a3e1-f411a66bd922",
        "name": "burp_sample_small.xml",
        "reportName": "Test Report",
        "clientName": "Test Client",
        "fileSize": "123625",
        "status": "PROCESSING",
        "progress": 0,
        "errorStatus": null,
        "source": "burp"
    }
]
```

The `status` will be `IMPORT COMPLETE` or `ERROR` depending on whether the import job completed successfully or not. If the job results in failure, the `errorStatus` will have some text labelling the error.
