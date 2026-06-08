
# import filename

Import the source state from an archive file in to a directory in the source
state. This is primarily used to make subdirectories of your home directory
exactly match the contents of a downloaded archive. You will generally always
want to set the --destination, --exact, and --remove-destination flags.

The supported archive formats are rar, tar, tar.gz, tgz, tar.bz2,
tbz2, txz, tar.zst, and zip.

## Flags

### -d, --destination directory

Set the destination (in the source state) where the archive will be imported.

### --exact

Set the exact attribute on all imported directories.

### -r, --remove-destination

Remove destination (in the source state) before importing.

### --strip-components n

Strip n leading components from paths.

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

## Examples

curl -s -L -o ${TMPDIR}/oh-my-zsh-master.tar.gz https://github.com/ohmyzsh/ohmyzsh/archive/master.tar.gz
mkdir -p $(chezmoi source-path)/dot_oh-my-zsh
chezmoi import --strip-components 1 --destination ~/.oh-my-zsh ${TMPDIR}/oh-my-zsh-master.tar.gz
