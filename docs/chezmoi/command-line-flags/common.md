
# Common command line flags

The following flags apply to multiple commands where they are relevant.

## Flags

### --age-recipient recipient

Temporarily override the age recipient for this command. This
only has an effect if age encryption is configured and the --encrypt flag is
passed, and cannot be combined with --age-recipient-file.

### --age-recipient-file recipient-file

Temporarily override the age recipient for this command. This
only has an effect if age encryption is configured and the --encrypt flag is
passed, and cannot be combined with --age-recipient.

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

### -h, --help

Print help.

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

### --override-data json-data
markdownlint-disable first-line-heading
Override template data with json-data.

### --override-data-file filename
markdownlint-disable first-line-heading
Override template data with JSON data read from filename.

### -P, --parent-dirs
markdownlint-disable first-line-heading
Execute the command on target and all its parent directories.

### -p, --path-style style

Print paths in the given style. The default is relative.
StyleDescription`absolute`Absolute paths in the destination directory`relative`Relative paths to the destination directory`source-absolute`Absolute paths in the source tree directory`source-relative`Relative paths to the source tree directory`all`All path styles, indexed by relative
### -r, --recursive

Recurse into subdirectories.

### --tree
markdownlint-disable first-line-heading
Print paths as a tree instead of a list.

## Available entry types

You can provide a list of entry types, separated by commas.
Types can be preceded with no to remove them, e.g. scripts,noalways.
TypeDescription`all`All entries`none`No entries`dirs`Directories`files`Files`remove`Removes`scripts`Scripts`symlinks`Symbolic links`always`Scripts that are always run`encrypted`Encrypted entries`externals`External entries`templates`Templates