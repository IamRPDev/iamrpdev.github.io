
# .chezmoidata.$FORMAT

If .chezmoidata.$FORMAT files exist in the source state, they are interpreted
as structured static data in the given format. This data can then be used in
templates. See also .chezmoidata/.

Example
If .chezmoidata.$FORMAT contains the following:
TOMLYAMLJSON


~/.local/share/chezmoi/.chezmoidata.tomlfontSize = 12



~/.local/share/chezmoi/.chezmoidata.yamlfontSize: 12



~/.local/share/chezmoi/.chezmoidata.json{
    "fontSize": 12
}




Then the .fontSize variable is available in templates, e.g.
FONT_SIZE={{ .fontSize }}

Will result in:
FONT_SIZE=12
markdownlint-disable first-line-heading
Info
chezmoi supports multiple file $FORMATs for configuration and data:
JSON, JSONC, TOML, and YAML.

Info
There may be multiple .chezmoidata.$FORMAT files in the source state. They
all merge to the root of the data dictionary and they are read in lexical
(alphabetic) filesystem order.
As an example, if I have four .chezmoidata.$FORMAT files in my
dot_config source directory, they will be merged according to the sort
order of the files:
dot_config/.chezmoidata.json{ "z": { "z": 3 } }

dot_config/.chezmoidata.jsonc{ "z": { "z": 4 } }

dot_config/.chezmoidata.tomlz.x = 1

dot_config/.chezmoidata.yamlz:
  y: 2

The output of chezmoi data will include the following merged z
dictionary. Note that the value in .chezmoidata.jsonc overwrote the value
in .chezmoidata.json because of the lexical file sorting.
{
  "z": {
    "x": 1,
    "y": 2,
    "z": 4
  }
}

Only dictionaries are merged; all other values (in particular lists) are
replaced.

Warning
.chezmoidata.$FORMAT files cannot be templates because they must be
present prior to the start of the template engine. Dynamic machine data
should be set in the data section of .chezmoi.$FORMAT.tmpl.
Dynamic environment data should be read from templates using the
output, fromJson, fromYaml, or
similar functions.
