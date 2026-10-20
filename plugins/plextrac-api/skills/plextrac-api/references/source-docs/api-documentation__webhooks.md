# Webhooks

Webhooks are a real-time, event-driven communication method that allows PlexTrac to send data automatically when a specific event occurs. Using HTTP POST requests, webhooks enable immediate data transfer without constant polling, making them efficient and lightweight.&#x20;

By providing a unique URL for event notifications, webhooks facilitate automation and real-time updates between applications while ensuring security through authentication methods and encryption.&#x20;

> **info:**
Users who prefer a straightforward, visual approach to setting up webhooks should utilize the [documentation page](/plextrac-documentation/product-documentation-1/account-management/account-admin/integrations-and-webhooks/webhooks.md) focused on integrations and webhooks through the application interface. This documentation is ideal for non-technical users or administrators who may not be familiar with API calls and prefer guided, step-by-step instructions.&#x20;

## Prerequisites

1. Users should ensure the webhook feature is enabled in their PlexTrac account.
2. Users must confirm that the notification engine and notification service are running.

> **danger:**
PlexTrac's webhook requests have a 5-second timeout. If an endpoint takes over five seconds to respond, the request will be retried up to five times with exponential backoff, potentially leading to duplicate events. To prevent this, ensure the endpoint reacts promptly.

## Configuring Webhooks

The list below outlines the key operations of the webhook lifecycle, including retrieving available events, creating new webhooks, updating existing configurations, testing webhook functionality, deleting webhooks, and accessing logs.&#x20;

### **Getting Available Events**

To retrieve a list of available webhook events, users should send a GET request to:

```
text{{toplevel_domain}}/api/internal/webhookevents
```

### **Creating a Webhook**

Users can create a new webhook by sending a POST request to:

```
text{{toplevel_domain}}/api/internal/webhooks
```

The request should include a JSON body with the following parameters:

```
json{
  "clientCuids": [],
  "name": "Your Webhook Name",
  "url": "https://your-webhook-url.com",
  "sslVerification": true,
  "events": ["ReportPublished"],
  "enabled": true,
  "secret": null
}
```

#### Webhook Security: HMAC-256 Signature Verification

To ensure the authenticity and integrity of webhooks, PlexTrac includes an HMAC-256 signature in the `X-Authorization-HMAC-256` header of each webhook request. This signature is generated using the secret provided during the webhook's creation.

> **info:**
Using an HMAC-256 signature with PlexTrac webhooks is optional. If a secret is not provided, it will default to null, and no signature will be included. While not required, using a signature is highly recommended to enhance the security and authenticity of webhooks. [Click here](/plextrac-documentation/api-documentation/webhooks/verifying-sender-requests.md) for more information on verifying sender requests.

To verify the signature, follow these steps:

1. **Concatenate**: Combine the secret with the raw JSON payload of the webhook request.
2. **Hash**: Generate an HMAC-SHA256 hash of the concatenated string.
3. **Compare**: Compare the generated hash with the value in the `X-Authorization-HMAC-256` header. If they match, the webhook is authentic.

### **Retrieving Webhooks**

To get a list of existing webhooks, users can use this GET endpoint:

```
text{{toplevel_domain}}/api/internal/webhooks?page[size]=25&page[current]=1
```

### **Updating a Webhook**

To modify an existing webhook, users should send a PATCH request to:

```
text{{toplevel_domain}}/api/internal/webhooks/{webhookCuid}
```

### **Testing a Webhook**

To test the webhook configuration, users can use this POST endpoint:

```
text{{toplevel_domain}}/api/internal/webhooks/test
```

The request should include a JSON body like this:

```
json{
  "url": "https://your-test-webhook-url.com",
  "secret": "your_secret_key",
  "sslVerification": true
}
```

### **Deleting a Webhook**

To remove a webhook, users should send a DELETE request to:

```
text{{toplevel_domain}}/api/internal/webhooks/{webhookCuid}
```

### **Viewing Webhook Logs**

To access webhook logs, users can use this GET endpoint:

```
text{{toplevel_domain}}/api/internal/webhookslog?tenantCuid={tenantCuid}&limit=25&offset=0&webhookCuid={webhookCuid}
```

## Validation Rules

When creating or updating webhooks, users must ensure that their requests adhere to the following validation rules:

* clientCuids: array of strings
* name: string
* url: string
* secret: string or null
* sslVerification: boolean
* events: array of strings (must include at least one valid event)
* enabled: boolean

## Troubleshooting

* Users should monitor API logs for testWebhook events and their outcomes.
* After configuring a webhook, it is advisable to trigger an event (e.g., publishing a report) to verify its functionality.
* If users encounter a "Failed to call webhook" error, they should check their logs for more details.
* It is important to note that webhook requests must follow specific rules to prevent SSRF attacks. PlexTrac validates the IP address and protocol for security purposes.
