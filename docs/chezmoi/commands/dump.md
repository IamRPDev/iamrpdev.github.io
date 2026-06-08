
# dump [target...]

Dump the target state of targets. If no targets are specified, then the
entire target state.

## Common flags

### -x, --exclude types
markdownlint-disable first-line-heading
Exclude target state entries of specific types. The default is
none.

Types can be explicitly included with the --include flag.

Example
--exclude=scripts will cause the command to not run scripts and
--exclude=encrypted will exclude encrypted files.

### -f, --format json|yaml
markdownlint-disable first-line-heading
Set the output format, json by default.

### -i, --include types
markdownlint-disable first-line-heading
Include target state entries of specific types. The default is all.

Types can be explicitly excluded with the --exclude flag.

Example
--include=files specifies all files.

### --init
markdownlint-disable first-line-heading
Regenerate and reload the config file from its template before computing
the target state.

### -P, --parent-dirs
markdownlint-disable first-line-heading
Execute the command on target and all its parent directories.

### -r, --recursive

Recurse into subdirectories.
Enabled by default. Can be disabled with --recursive=false.

## Examples

chezmoi dump ~/.bashrc
chezmoi dump --format=yaml
