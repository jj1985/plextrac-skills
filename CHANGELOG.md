# Changelog

## 1.0.0 - 2026-10-20

- Initial release of the `plextrac-api` plugin, built from the official PlexTrac Postman collection (api-docs.plextrac.com, 363 requests) and the docs.plextrac.com API documentation.
- OpenAPI 3.1 spec: 237 paths, 293 REST operations, the `/graphql` endpoint, and 6 outbound webhook payloads (OpenAPI `webhooks`).
- Skill references: quick reference (auth, IDs, pagination, CRUD, streaming scanner import, export), object structures, gotchas with the full sunset/deprecation log, generated endpoint catalog, generated GraphQL operation catalog, and the documentation snapshot.
- Dependency-free Python client (`plextrac_api.py`) with MFA, automatic token refresh, pagination, report export and the presigned-URL import flow; `verify_webhook.py` for HMAC-SHA256 webhook verification.
