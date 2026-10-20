# PlexTrac skills

A plugin marketplace for AI coding agents that work with the **PlexTrac** penetration-testing and reporting platform API.
It ships one plugin, `plextrac-api`, built from the official PlexTrac API Postman collection and documentation (captured 2026-10-20).

| What you get | Where |
|---|---|
| OpenAPI 3.1 spec: 237 paths, 293 REST operations, the `/graphql` endpoint and 6 outbound webhook payloads | [`openapi/plextrac.openapi.yaml`](openapi/plextrac.openapi.yaml) (also bundled in the skill) |
| Agent skill: entry-point table, auth/pagination mechanics, workflow, conventions | [`plugins/plextrac-api/skills/plextrac-api/SKILL.md`](plugins/plextrac-api/skills/plextrac-api/SKILL.md) |
| Quick reference, object structures, gotchas with the full sunset/deprecation log | `.../references/quickref.md`, `objects.md`, `gotchas.md` |
| Generated catalog of all 363 documented requests and 62 GraphQL operations | `.../references/endpoint-catalog.md`, `graphql-operations.md` |
| Documentation snapshot (17 pages) and the raw Postman collection | `.../references/source-docs/` |
| Dependency-free Python client (MFA, token refresh, pagination, export, streaming scanner import) and webhook verifier | `.../scripts/plextrac_api.py`, `.../scripts/verify_webhook.py` |

## Install

### GitHub Copilot CLI

```bash
copilot plugin marketplace add jj1985/plextrac-skills
copilot plugin install plextrac-api@plextrac
```

Or install the plugin directly from the repository subdirectory:

```bash
copilot plugin install jj1985/plextrac-skills:plugins/plextrac-api
```

To enable it declaratively for a repository, add it to `.github/copilot/settings.json`:

```json
{
  "extraKnownMarketplaces": { "plextrac": { "source": "github", "repo": "jj1985/plextrac-skills" } },
  "enabledPlugins": { "plextrac-api@plextrac": true }
}
```

### Claude Code

```text
/plugin marketplace add jj1985/plextrac-skills
/plugin install plextrac-api@plextrac
```

### Any agent that reads `SKILL.md`

Copy `plugins/plextrac-api/skills/plextrac-api/` into your skills directory (for example `~/.copilot/skills/`, `~/.claude/skills/` or `.agents/skills/`).

## Repository layout

```text
plextrac-skills/
├── .github/plugin/marketplace.json        Copilot CLI marketplace manifest
├── .claude-plugin/marketplace.json        Claude Code mirror of the marketplace manifest
├── openapi/plextrac.openapi.yaml          OpenAPI 3.1 spec (canonical copy)
└── plugins/
    └── plextrac-api/
        ├── plugin.json                    Agent Plugins 1.0 manifest (Copilot CLI, Codex and other clients)
        ├── .claude-plugin/plugin.json     Claude Code manifest
        └── skills/
            └── plextrac-api/
                ├── SKILL.md
                ├── references/            quickref, objects, gotchas, catalogs, docs snapshot, OpenAPI copy
                └── scripts/               plextrac_api.py, verify_webhook.py
```

The plugin follows the [Agent Plugins 1.0](https://agent-plugins.org/) layout documented for Copilot CLI: manifest at the plugin root, skills discovered from `skills/<name>/SKILL.md`. Claude Code reads the `.claude-plugin/` mirrors.

## Using the scripts

```bash
export PLEXTRAC_URL=https://tenant.plextrac.com PLEXTRAC_USERNAME=svc@example.com PLEXTRAC_PASSWORD=...
python plugins/plextrac-api/skills/plextrac-api/scripts/plextrac_api.py whoami
python plugins/plextrac-api/skills/plextrac-api/scripts/plextrac_api.py findings 1254 500006 --out findings.json
python plugins/plextrac-api/skills/plextrac-api/scripts/plextrac_api.py import-scan 1254 500006 nessus ./scan.nessus --wait
```

Use a PlexTrac Service Account for automation (exempt from tenant-wide MFA enforcement). Tokens last 15 minutes; the client refreshes them automatically. Logins are rate-limited to 10 per minute per instance.

## Scope and caveats

- Sources: [PlexTrac API Postman collection](https://api-docs.plextrac.com/) and [PlexTrac API documentation](https://docs.plextrac.com/plextrac-documentation/api-documentation/overview). PlexTrac publishes no OpenAPI document; request and response schemas here are inferred from the collection's example payloads and are representative rather than exhaustive.
- GraphQL operations (Runbooks v2) cannot be expressed as OpenAPI paths; they are catalogued with their query text in `graphql-operations.md`.
- Webhook configuration routes live under `/api/internal/` and are documented from the docs pages only.
- Nothing here has been run against a live PlexTrac instance. Issues and corrections are welcome.

## License

MIT. PlexTrac, Inc. owns the underlying product and its documentation; this repository is an independent, derived reference and is not affiliated with PlexTrac.
