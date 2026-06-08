# Templating
Powerful templating to handle environmental differences.

### Substrate Modifications
Templates utilize resilient patterns like `get $secrets "KEY" | default "..."` and incorporate FIDO2 security (AFD FIDO keys) for secret access, optimized with RAM-backed cache (`/dev/shm/substrate-vault/`).

### Applications
Used for dynamic environment configuration across the fleet, ensuring secrets are injected securely and ephemeral data is cached effectively to reduce hardware touches.
