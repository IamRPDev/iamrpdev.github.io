
# managed [path...]

List all managed entries in the destination directory under all paths in
alphabetical order. When no paths are supplied, list all managed entries in
the destination directory in alphabetical order.

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

### -0, --nul-path-separator
markdownlint-disable first-line-heading
Separate paths with the NUL character instead of a newline.

### -p, --path-style style

Print paths in the given style. The default is relative.
StyleDescription`absolute`Absolute paths in the destination directory`relative`Relative paths to the destination directory`source-absolute`Absolute paths in the source tree directory`source-relative`Relative paths to the source tree directory`all`All path styles, indexed by relative
### -t, --tree
markdownlint-disable first-line-heading
Print paths as a tree instead of a list.

## Examples

chezmoi managed
chezmoi managed --include=files
chezmoi managed --include=files,symlinks
chezmoi managed -i dirs
chezmoi managed -i dirs,files
chezmoi managed -i files ~/.config
chezmoi managed --exclude=encrypted --path-style=source-relative
