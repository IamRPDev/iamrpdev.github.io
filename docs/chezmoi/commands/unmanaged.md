
# unmanaged [path...]

List all unmanaged files in paths. When no paths are supplied, list all
unmanaged files in the destination directory.

It is an error to supply paths that are not found on the file system.

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

### -0, --nul-path-separator
markdownlint-disable first-line-heading
Separate paths with the NUL character instead of a newline.

### -p, --path-style style

Print paths in the given style. The default is relative.
StyleDescription`absolute`Absolute paths in the destination directory`relative`Relative paths to the destination directory
### -t, --tree
markdownlint-disable first-line-heading
Print paths as a tree instead of a list.

## Examples

chezmoi unmanaged
chezmoi unmanaged ~/.config/chezmoi ~/.ssh
