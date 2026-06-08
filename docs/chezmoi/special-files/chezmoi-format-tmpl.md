
# .chezmoi.$FORMAT.tmpl

If a file called .chezmoi.$FORMAT.tmpl exists in the root of the source state
then chezmoi init will use it to create or update the chezmoi config
file. $FORMAT must be one of the supported config file formats.

This template differs from source state templates because this template is
executed prior to the reading of the source state.
FeatureAvailable?data in theconfig file✅data in`.chezmoidata.$FORMAT`files🚫data in`.chezmoidata/`directories🚫templates in`.chezmoitemplates`🚫template functions✅init functions✅
Example
~/.local/share/chezmoi/.chezmoi.yaml.tmpl{{ $email := promptStringOnce . "email" "What is your email address" -}}

data:
    email: {{ $email | quote }}
markdownlint-disable first-line-heading
Info
chezmoi supports multiple file $FORMATs for configuration and data:
JSON, JSONC, TOML, and YAML.

Info
This file will also be used to update the config file when a command
supports the --init flag, such as chezmoi update --init.
