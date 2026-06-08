
# re-add [target...]

Re-add modified files in the target state, preserving any encrypted_
attributes. chezmoi will not overwrite templates, and all entries that are not
files are ignored. Directories are recursed into by default.

If no targets are specified then all modified files are re-added. If one or
more targets are given then only those targets are re-added.

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

### --re-encrypt

Re-encrypt encrypted files.

### -r, --recursive

Recurse into subdirectories.
Enabled by default. Can be disabled with --recursive=false.

## Examples

chezmoi re-add
chezmoi re-add ~/.bashrc
chezmoi re-add --recursive=false ~/.config/git

## Notes

Hint
If you want to re-add a single file unconditionally, use chezmoi add --force instead.
