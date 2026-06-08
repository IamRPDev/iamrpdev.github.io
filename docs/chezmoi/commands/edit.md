
# edit [target...]

Edit the source state of targets, which must be files or symlinks. If no
targets are given then the working tree of the source directory is opened.

Encrypted files are decrypted to a private temporary directory and the editor
is invoked with the decrypted file. When the editor exits the edited decrypted
file is re-encrypted and replaces the original file in the source state.

If the operating system supports hard links, then the edit command invokes the
editor with filenames which match the target filename, unless the
edit.hardlink configuration variable is set to false or the
--hardlink=false command line flag is set. Templates preserve their .tmpl
extension so editors can highlight them as templates.

Hint
Depending on your editor, you can set the format of a file in the file itself
using a modeline. This can be useful if you want to syntax
highlight a template as a different format.

## Flags

### -a, --apply

Configuration: edit.apply

Apply the target immediately after editing. This is ignored if there are no
targets, and does not apply scripts.

### --hardlink bool

Configuration: edit.hardlink

Invoke the editor with a hard link to the source file with a name matching the
target filename. This can help the editor determine the type of the file
correctly. This is the default.

Hint
Creating hardlinks is not possible between different filesystems. Hence,
if your tempDir resides on a different filesystem (e.g. a
tmpfs, which is sometimes used for /tmp), this will not work.

### --watch

Configuration: edit.watch

Automatically apply changes when files are saved, with the following limitations:
- Only available when chezmoi edit is invoked with arguments (i.e.
  argument-free chezmoi edit is not supported).
- All edited files are applied when any file is saved.
- Only the edited files are watched, not any dependent files (e.g.
  .chezmoitemplates and included files in templates are not watched).
- Only works on operating systems supported by fsnotify.
- Only works if edit.hardlink is enabled and works.

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

## Examples

chezmoi edit ~/.bashrc
chezmoi edit ~/.bashrc --apply
chezmoi edit
