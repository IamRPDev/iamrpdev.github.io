
# diff [target...]

Print the difference between the target state and the destination state for
targets. If no targets are specified, print the differences for all targets.

If a diff.pager command is set in the configuration file then the output will
be piped into it.

If diff.command is set then it will be invoked to show individual file
differences with diff.args passed as arguments. Each element of diff.args
is interpreted as a template with the variables .Destination and .Target
available corresponding to the path of the file in the source and target state
respectively. The default value of diff.args is
["{{ .Destination }}", "{{ .Target }}"]. If diff.args does not contain any
template arguments then {{ .Destination }} and {{ .Target }} will be
appended automatically.

## Flags

### --pager pager

Configuration: diff.pager

Pager to use for output.

### --reverse

Configuration: diff.reverse

Reverse the direction of the diff, i.e. show the changes to the target required
to match the destination.

### --script-contents

Show script contents, defaults to true.

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

## Examples

chezmoi diff
chezmoi diff ~/.bashrc
