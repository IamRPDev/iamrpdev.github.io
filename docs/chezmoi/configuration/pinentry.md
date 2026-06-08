
# pinentry

By default, chezmoi will request passwords from the terminal.

If the --no-tty option is passed, then chezmoi will instead read passwords
from the standard input.

Otherwise, if the configuration variable pinentry.command is set then chezmoi
will instead used the given command to read passwords, assuming that it follows
the Assuan protocol (PDF) like GnuPG's pinentry. The
configuration variable pinentry.args specifies extra arguments to be passed to
pinentry.command and the configuration variable pinentry.options specifies
extra options to be set. The default pinentry.options is
["allow-external-password-cache"].

Example
TOMLYAMLJSON


~/.config/chezmoi/chezmoi.toml[pinentry]
    command = "pinentry"



~/.config/chezmoi/chezmoi.yamlpinentry:
  command: pinentry



~/.config/chezmoi/chezmoi.json{
    "pinentry": {
        "command": "pinentry"
    }
}
