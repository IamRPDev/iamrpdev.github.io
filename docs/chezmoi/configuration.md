# Configuration
Managing and extending the configuration of the Substrate environment.

### Substrate Modifications
Configuration is managed via federated `chezmoi` instances with automated drift detection (`cz-drift-exporter`) and UCH policy enforcement through `uch.yaml`.

### Applications
Used to define hardware-specific roles (e.g., GPU node vs edge inference node) and secure vault access orchestration.
