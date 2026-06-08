# Modifications & Applications: Substrate Changelog

This page tracks all Substrate-specific additions, modifications, and architectural overrides applied to the standard Chezmoi workflow.

## [v1.2.0] - Project Nexus (Current)
### Added
- **Fleet Telemetry:** Implemented `cz-drift-exporter` to surface configuration drift metrics to Prometheus.
- **Sovereign Health Dashboard:** Deployed managed Grafana dashboard (`sovereign-health.json`) for fleet-wide observability.
- **Resilient Templates:** Standardized the use of `get ... | default` for all secret injections to prevent bootstrapping deadlocks.

## [v1.1.0] - Project Aegis & Synapse
### Added
- **FIDO2 Hardware Lock:** Binded Age encryption to AFD FIDO hardware (ID 072f:b307).
- **RAM-backed Vault Cache:** Decrypting secrets into `/dev/shm/substrate-vault/` to reduce hardware touch requests.
- **Non-Fatal Bootstrapping:** Support for `SUBSTRATE_SKIP_VAULT=1` to allow headless deployments.
- **AI-Driven Automation:** Deployed `cz-commit` (phi4-mini) and `cz-discover-aliases` for shell productivity.
- **Secure SQLite Diffing:** Implemented `textconv-sqlite` for plain-text auditing of binary databases.

### Modified
- **Vault Orchestration:** Refactored `run_before` hooks to include 3-attempt retry loops and 30s timeouts for hardware touches.
- **Infrastructure-as-Code:** Enhanced `deploy-infrastructure` hooks to recursively sync service configurations to hypervisor nodes.

## [v1.0.0] - Foundation
### Added
- **Federated Infrastructure:** Initial management of `llmadmin01` (Master) and `t430` (Hypervisor) nodes.
- **UCH Policy Engine:** Role-based secret access and compliance enforcement via `uch.yaml`.
- **Ephemeral Secret Injection:** Eliminated persistent `.env` files by injecting hardware-encrypted secrets directly into `.bashrc`.
