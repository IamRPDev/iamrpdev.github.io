
# status

Print the status of the files and scripts managed by chezmoi in a format
similar to git status.

The first column of output indicates the difference between the last state
written by chezmoi and the actual state. The second column indicates the
difference between the actual state and the target state, and what effect
running chezmoi apply will have.
CharacterMeaningFirst columnSecond columnSpaceNo changeNo changeNo change`A`AddedEntry was createdEntry will be created`D`DeletedEntry was deletedEntry will be deleted`M`ModifiedEntry was modifiedEntry will be modified`R`RunNot applicableScript will be run
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

### -p, --path-style style

Print paths in the given style. The default is relative.
StyleDescription`absolute`Absolute paths in the destination directory`relative`Relative paths to the destination directory`source-absolute`Absolute paths in the source tree directory`source-relative`Relative paths to the source tree directory`all`All path styles, indexed by relative
### -r, --recursive

Recurse into subdirectories.
Enabled by default. Can be disabled with --recursive=false.

## Examples

chezmoi status
