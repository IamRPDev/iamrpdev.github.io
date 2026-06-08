
# update

Pull changes from the source repo and apply any changes.

If update.command is set then chezmoi will run update.command with
update.args in the working tree. Otherwise, chezmoi will run git pull
--autostash --rebase [--recurse-submodules] , using chezmoi's builtin git if
useBuiltinGit is true or if git.command cannot be found in $PATH.

## Flags

### -a, --apply

Apply changes after pulling, true by default. Can be disabled with --apply=false.

### --recurse-submodules

Update submodules recursively. This defaults to true. Can be disabled with --recurse-submodules=false.

## Common flags

### -x, --exclude types
markdownlint-disable first-line-heading
Exclude target state entries of specific types. The default is
none.

Types can be explicitly included with the --include flag.

Example
--exclude=scripts will cause the command to not run scripts and
--exclude=encrypted will exclude encrypted files.

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

chezmoi update
