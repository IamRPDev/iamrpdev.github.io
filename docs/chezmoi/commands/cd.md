
# cd [path]

Launch a shell in the working tree (typically the source directory). chezmoi
will launch the command set by the cd.command configuration variable with any
extra arguments specified by cd.args. If this is not set, chezmoi will
attempt to detect your shell and finally fall back to an OS-specific default.

If the optional argument path is present, the shell will be launched in the
source directory corresponding to path.

The shell will have various CHEZMOI* environment variables set, as for
scripts.

Hint
This does not change the current directory of the current shell. To do
that, instead use:
$ cd $(chezmoi source-path)

## Examples

chezmoi cd
chezmoi cd ~
chezmoi cd ~/.config
