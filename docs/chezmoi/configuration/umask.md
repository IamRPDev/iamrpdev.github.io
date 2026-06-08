
# umask

By default, chezmoi uses your current umask as set by your operating system and
shell. chezmoi only stores crude permissions in its source state, namely in the
executable  and private attributes, corresponding to the umasks of 0o111
and 0o077 respectively.

For machine-specific control of umask, set the umask configuration variable in
chezmoi's configuration file.

Example
TOMLYAMLJSON


~/.config/chezmoi/chezmoi.tomlumask = 0o22



~/.config/chezmoi/chezmoi.yamlumask: 18



~/.config/chezmoi/chezmoi.json{
    "umask": 18
}
