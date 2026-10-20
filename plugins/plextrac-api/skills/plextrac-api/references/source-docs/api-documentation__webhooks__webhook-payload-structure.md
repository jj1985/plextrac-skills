# Webhook Payload Structure

A webhook payload contains data about events in a source system. Typically formatted as JSON, this structured information is sent to a specified URL when a predefined event triggers the webhook. Understanding the payload structure is essential for processing and responding effectively to incoming webhook data.&#x20;

This page outlines the standard format of our webhook payloads and details the key components that facilitate data exchange between applications.

> **info:**
You can find more detailed examples on the payload structure of each webhook on our [Postman Collection](https://api-docs.plextrac.com/#7cb8e496-3fee-4b97-be42-be9ee050fd2a)

## Structure

The `WebhookPayload` type is defined as follows:

```
type WebhookPayload = {
    cuid: string;
    actorCuid: string;
    event: string;
    targetCuid: string | never;
    targetCuids: string[] | never;
    targetType: string;
    text: string;
    clientId?: number;
    reportId?: number;
    findingId?: number;
    assessmentId?: number;
}
```

## Security

To ensure the integrity and authenticity of webhook payloads, PlexTrac includes a `X-Authorization-HMAC-256` header in the webhook request. This header contains an HMAC-SHA256 signature generated using a secret key configured when the webhook was created.&#x20;

Users can verify the payload's authenticity by calculating the HMAC-SHA256 signature on their end and comparing it to the value in the `X-Authorization-HMAC-256` header. For detailed instructions on how to verify the signature, users should refer to the main [Webhooks documentation](https://docs.plextrac.com/plextrac-documentation/api-documentation/webhooks#webhook-security-hmac-256-signature-verification) page.

## Field Definitions

* **cuid**: A unique identifier for the webhook request.
* **actorCuid**: A string representing the unique identifier of the actor or user who triggered the event.
* **event**: A string indicating the type of event that triggered the webhook.
* **targetCuid**: A string representing the unique identifier of a single entity associated with the event. This field is mutually exclusive with targetCuids.
* **targetCuids**: An array of strings representing the unique identifiers of multiple entities associated with the event. This field is mutually exclusive with targetCuid.
* **targetType:** A string indicating the type of entity associated with the event.
* **text**: A string field containing additional information or description related to the webhook event.

> **info:**
The fields `targetCuid` and `targetCuids` are mutually exclusive, meaning a payload will include either but never both.

## Conditional Object Identifiers

While the `WebhookPayload` type contains standard metadata, most event payloads include additional conditional fields to help you uniquely identify and retrieve the specific objects involved in the event.

These identifiers are essential for making subsequent API calls to fetch more data about the affected resource. Because our webhooks cover a range of objects, the specific IDs included in a payload depend entirely on the event type. These identifiers are provided in addition to the `cuid` since most API routes only accept these IDs as opposed to the objects `cuid`.

Possible Conditional Fields:

* **clientId**: `number` — The unique identifier for the Client associated with the event.
* **reportId**: `number` — The unique identifier for the specific Report associated with the event.
* **findingId**: `number` — The unique identifier for the specific Finding (flaw) associated with the event.
* **assessmentId**: `number` — The unique identifier for the Assessment associated with the event.

> **info:**
Endpoint Specificity: These fields are not present in every payload. Each webhook endpoint returns a unique combination of these identifiers based on its context. To see exactly which IDs are returned for a specific event, please refer to the individual endpoint examples in our [Postman Collection](https://api-docs.plextrac.com/#7cb8e496-3fee-4b97-be42-be9ee050fd2a).
