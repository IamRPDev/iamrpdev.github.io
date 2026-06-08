
# merge-all

Perform a three-way merge for file whose actual state does not match its target
state. The merge is performed with chezmoi merge.

## Common flags

### --init
markdownlint-disable first-line-heading
Regenerate and reload the config file from its template before computing
the target state.

### -r, --recursive

Recurse into subdirectories.
Enabled by default. Can be disabled with --recursive=false.

## Examples

chezmoi merge-all
