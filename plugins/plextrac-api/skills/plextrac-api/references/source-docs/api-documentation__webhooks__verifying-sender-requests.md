# Verifying Sender Requests

When events trigger a webhook, PlexTrac sends a POST request with the event payload to the configured URL. If a secret is provided during webhook setup, PlexTrac generates an HMAC-SHA256 signature using that secret and includes it in the `x-authorization-hmac-256` header. Users can specify a secret when creating a webhook in the PlexTrac UI, enabling signature-based verification of incoming requests.

### Generating the Signature

PlexTrac generates the signature using the following JavaScript code in the application:

```java
const hmac = crypto.createHmac('SHA256', webhook.secret);
hmac.update(Buffer.from(JSON.stringify(payload)));
const signature = hmac.digest('hex');
```

### Verifying the Signature in Python

To verify the signature in Python, follow these steps:

1. Extract the `x-authorization-hmac-256` header from the incoming request.
2. Retrieve the webhook secret.
3. Convert the payload into a JSON string using `json.dumps()` with specific formatting to match JavaScript's `JSON.stringify()`.
4. Compute the HMAC-SHA256 hash and compare it with the received signature using the secret.

Python Implementation (FastAPI Example):

```python
import hmac
import hashlib
import json
from fastapi import Request

async def verify_webhook(request: Request, secret: str):
    # Extract the signature from the request headers
    hmac_header = request.headers.get("x-authorization-hmac-256")
    if not hmac_header:
        return False  # Missing signature header

    # Retrieve and format the JSON payload
    response_payload = await request.json()
    payload_str = json.dumps(response_payload, separators=(',', ':'))  # Match JSON.stringify()

    # Compute the HMAC-SHA256 hash
    hmac_obj = hmac.new(secret.encode(), payload_str.encode(), hashlib.sha256)
    sha256_hash = hmac_obj.hexdigest()
    
    # Compare the computed hash with the received signature
    return hmac_header == sha256_hash
```

### Debugging Tips

If the generated hash does not match the received signature:

* Ensure that the JSON formatting is the same as `JSON.stringify()` (use `separators=(',', ':')`).
* Log the raw request body before parsing JSON to confirm the received data is correct:

```python
raw_body = await request.body()
print(f"Raw Body: {raw_body.decode()}")
```

* Check for encoding mismatches when converting the JSON string.
* Confirm that both systems use the same secret for hashing.
