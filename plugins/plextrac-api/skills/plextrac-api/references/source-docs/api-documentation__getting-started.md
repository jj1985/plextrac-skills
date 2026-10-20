# Getting Started

## Authentication Tokens

PlexTrac uses JWT tokens to manage authentication for all API endpoints. This token is sent as an authorization header to all endpoints and validates the user has permission to access the requested action.

Upon successful authentication, these tokens are granted to users in a PlexTrac instance and contain the user's permissions. This means the user will have the same permissions regardless of whether they interact with the PlexTrac platform or manually request an API.

### Expiration and Limits

After 15 minutes, JWT tokens expire, requiring users to refresh or re-authenticate for a new valid token.

Ten authentication requests are allowed per minute, regardless of the user or whether the attempt was successful. Any additional attempts will result in an error. This limit is enforced to prevent brute-force attacks against the platform. It may be reached naturally if multiple users attempt to sign in simultaneously or if an API script tries to be used concurrently.

### Authentication Providers

Each user in PlexTrac is assigned a single Authentication Provider that determines how they access the platform. While the system supports multiple providers, the logic for token generation remains consistent across all methods.

* PlexTrac (Default): Local authentication managed within the platform. Supports Multi-Factor Authentication (MFA).
* SSO Providers: Supports multiple enterprise options, including SAML and OAuth.
* PlexTrac Service Account: A specialized local account type used primarily for automation (see the [Service Accounts](https://docs.plextrac.com/plextrac-documentation/api-documentation/getting-started#service-accounts-mfa-override) section for details).

#### Global MFA Enforcement

PlexTrac includes a global instance setting to Require MFA for all users.

* Enforcement: When enabled, any user without MFA configured will be interrupted during the login process.
* Setup: The system will prompt the user to configure MFA immediately and will block access to the dashboard and API until the setup is complete.

### Generate Access Token

> **info:**
This method generates a JWT token ONLY when the user's authentication provider is set to PlexTrac and MFA is NOT enabled. For MFA, see the [Generate Access Token (MFA)](https://docs.plextrac.com/plextrac-documentation/api-documentation/getting-started#generate-access-token-mfa) section.\
\
![](https://4252973360-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LXA6EayCcg12qfDcfXd%2Fuploads%2F90bQMi8ZM2SHF8TToot8%2Fimage.png?alt=media\&token=157fdfd9-d334-4b78-bfa1-b8f74c107586)

[`POST Authentication`](https://api-docs.plextrac.com/#65d40d98-bfaf-4452-8ab0-3ffeeb280923) is the basic auth endpoint and returns the following after successfully verifying the given username and password for a user without MFA:

<div align="left"></div>

The value of the `token` field is the JWT token to be sent to all other endpoints in the Authorization header.

### Generate Access Token (MFA)

> **info:**
This method generates a JWT token ONLY when the user's Authentication Provider is set to PlexTrac, and the user DOES have MFA enabled.<br>

![](https://4252973360-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LXA6EayCcg12qfDcfXd%2Fuploads%2FoJyYs3yJT3S85gnrFOuE%2Fimage.png?alt=media\&token=c80227bb-c77c-417b-bd38-bea19a048ec1)

Users with MFA enabled must use two endpoints to generate a JWT token. First, call the [`POST Authentication`](https://api-docs.plextrac.com/#65d40d98-bfaf-4452-8ab0-3ffeeb280923) endpoint. The response will contain the `code` field if the user has MFA enabled. The value relates to the Authenticator set up by the user and the six-digit rotating code associated with their login.

<div align="left"></div>

Next, call the [POST Multi-Factor Authentication](https://api-docs.plextrac.com/#e7e0df57-0731-4658-9a83-30be15405177) endpoint with the code returned from the last request and the current six-digit code from your Authenticator in the payload.

```json
{
    "code": "<code value from previous request>",
    "token": "<6-digit authenticator code>"
}
```

This will return the following after successfully verifying the given MFA data for a user:

<div align="left"></div>

The value of the `token` field is the JWT token to be sent in the Authorization header to all other endpoints.

### Service Accounts (MFA Override)

A PlexTrac Service Account is technically a standard user capable of logging in via the UI, but it serves a specific architectural purpose: bypassing global MFA requirements.

In environments where the global "Require MFA" toggle is active, standard scripts and API integrations would typically fail because they cannot perform the interactive MFA setup or provide rotating codes without human intervention.

* The Exception: Users designated as a "Service Account" are exempt from the global MFA enforcement toggle.
* Use Case: This allows scripts and automated workflows to authenticate using standard credentials to receive a JWT token without being blocked by an MFA setup prompt.

### Authorization and RBAC

PlexTrac authentication is token-based and handled per user. When a user (or service account) sends credentials to the authentication endpoints, they receive a JWT token tied specifically to their user profile.

Every time this token is sent in an API request header, the system performs an authorization check:

1. Identity: Who is the user tied to this token?
2. Permissions: Does this specific user have the required Role-Based Access Control (RBAC) permissions to perform the requested task?

If the user’s assigned permissions do not cover the endpoint or action, the request will be denied, regardless of the token's validity.

### Sending the Authorization Header with Requests

Once generated, the JWT token is sent as an Authorization Header with all other endpoints. Using the requests module in Python, an example call would be the following:

<div align="left"></div>

To make a request using cURL from the command line, consider the following syntax:

<div align="left"></div>

### Refreshing Access Token

Tokens can be refreshed with the [PUT Refresh Token](https://api-docs.plextrac.com/#c4bbbfa1-1c6e-4552-8cca-bd5634907b7e) endpoint before the session expires, creating a new session that lasts another 15 minutes. The alternative approach is using the same authentication methods that generated the session in the first place. The advantage of refreshing a token vs. generating a new session is tied to how a user is authenticated into the latest session.

Refreshing a token uses an existing token but must be done before the session expires while the original token is still valid.

Generating a new session token requires your username/password and, if MFA is set up for the user, an MFA code.

The advantage of refreshing is that the user does not need the username/password and MFA code to extend the session. However, refreshing is necessary for users with MFA setup; otherwise, a new MFA code must be entered to generate a new session.

## Sending a JSON Payload

Some endpoints require a JSON payload. When sending a request in Postman, it automatically detects when the raw JSON body option is selected and adds the header `Content-Type: application/json` to the request. This adds the payload to the HTTP request `json` field.&#x20;

Confirm that the payload is being sent in the request's json field when sending requests via other means. Without the `Content-Type: application/json` header, the payload might be stored in the `data` or `form` field and cause the request to fail since the `json` field where the expected data is `null`.

<div align="left"></div>

#### **cURL**

Add the `Content-Type: application/json` header to tell the request the `--data-raw` data is a JSON and should be stored in the request's `json` field.

<div align="left"></div>

#### **Python**

With the Python requests module, add the JSON payload to the `json` parameter when making a request, and the requests module will automatically send the `Content-Type: application/json` header with the request.

<div align="left"></div>
