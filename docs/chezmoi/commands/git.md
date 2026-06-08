
# git [arg...]

Run git args in the working tree (typically the source directory).

Note
Flags in args must occur after -- to prevent chezmoi from interpreting
them.

## Examples

chezmoi git add .
chezmoi git add dot_gitconfig
chezmoi git -- commit -m "Add .gitconfig"
