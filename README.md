# Data-Flow

Enterprise desktop automation platform for transferring spreadsheet records into web applications through browser automation.

## Product direction

- Windows desktop client: Python + Eel + HTML/CSS/JavaScript
- Browser automation: Playwright
- Cloud control plane: FastAPI + PostgreSQL
- Local persistence: SQLite
- Commercial model: multi-tenant accounts, subscriptions, device-bound licenses, and usage telemetry

## Status

Foundation initialization. Product workflows, licensing enforcement, and automation execution are under phased development.

## Security model

The desktop client must not contain database credentials or signing secrets. Subscription decisions are made by the remote API. Offline operation uses a bounded, signed license lease; revocation takes effect when the client next validates or its lease expires.

## Development

See `docs/` for architecture and setup guidance. The Windows desktop client is the initial delivery target; cloud services are a separate deployable component.
