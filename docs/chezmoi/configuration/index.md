
# Configuration file

chezmoi searches for its configuration file according to the XDG Base Directory
Specification. The base name of the config file is chezmoi. If multiple
configuration file formats are present, chezmoi will report an error.
markdownlint-disable first-line-heading
Info
chezmoi supports multiple file $FORMATs for configuration and data:
JSON, JSONC, TOML, and YAML.

In most installations, the config file will be read from
$HOME/.config/chezmoi/chezmoi.$FORMAT
(%USERPROFILE%/.config/chezmoi/chezmoi.$FORMAT), where $FORMAT is one of
json, jsonc, toml, or yaml. The config file can be set explicitly with
the --config command line option. By default, the format is detected based on
the extension of the config file name, but can be overridden with the
--config-format command line option.

## Examples

TOMLYAMLJSONJSONC


~/.config/chezmoi/chezmoi.tomlsourceDir = "/home/user/.dotfiles"
[git]
    autoPush = true



~/.config/chezmoi/chezmoi.yamlsourceDir: /home/user/.dotfiles
git:
    autoPush: true



~/.config/chezmoi/chezmoi.json{
    "sourceDir": "/home/user/.dotfiles",
    "git": {
        "autoPush": true
    }
}



~/.config/chezmoi/chezmoi.jsonc{
    // The chezmoi source files are stored here
    "sourceDir": "/home/user/.dotfiles",
    "git": {
        "autoPush": true
    }
}
