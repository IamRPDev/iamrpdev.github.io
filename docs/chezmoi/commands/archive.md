
# archive [target....]

Generate an archive of the target state, or only the targets specified. This
can be piped into tar to inspect the target state.

## Flags

### -f, --format format

Write the archive in format. If --output is set the format is guessed from
the extension, otherwise the default is tar.
Supported formats`tar``tar.gz``tgz``zip`
### -z, --gzip

Compress the archive with gzip. This is automatically set if the format is
tar.gz or tgz and is ignored if the format is zip.

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

chezmoi archive | tar tvf -
chezmoi archive --output=dotfiles.tar.gz
chezmoi archive --output=dotfiles.zip
