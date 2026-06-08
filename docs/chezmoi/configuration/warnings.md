
# Warnings

By default, chezmoi will warn you when it encounters potential problems. Some of
these warnings can be suppressed by setting values in configuration file.
VariableTypeDefaultDescription`configFileTemplateHasChanged`bool`true`Warn when the config file template has changed
Example
TOMLYAMLJSON


~/.config/chezmoi/chezmoi.toml[warnings]
    configFileTemplateHasChanged = false



~/.config/chezmoi/chezmoi.yamlwarnings:
  configFileTemplateHasChanged: false



~/.config/chezmoi/chezmoi.json{
    "warnings": {
        "configFileTemplateHasChanged": false
    }
}
