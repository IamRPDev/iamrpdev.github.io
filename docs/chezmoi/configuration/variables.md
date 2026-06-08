
# Variables

## Top level

### cacheDir
TypeDefault`string``$XDG_CACHE_HOME/chezmoi`/`$HOME/.cache/chezmoi`/`%USERPROFILE%/.cache/chezmoi`
Cache directory.

### color
TypeDefault`string``auto`
Colorize output.

### data
TypeDefault`object`none
Template data.

### destDir
TypeDefault`string``$HOME`/`%USERPROFILE%`
Destination directory.

### encryption
TypeDefault`string`none
Encryption type, either age, gpg, or transparent.

### env
TypeDefault`object`none
Extra environment variables for scripts and commands.

### format
TypeDefault`string``json`
Format for data output, either json or yaml.

### interactive
TypeDefault`string``false`
Prompt for all changes.

### mode
TypeDefault`string``file`
Mode in target dir, either file or symlink.

### pager
TypeDefault`string``$PAGER`
Default pager CLI command.

### pagerArgs
TypeDefault`[]string`none
Extra args to the pager command.

### persistentState
TypeDefault`string``$XDG_CONFIG_HOME/chezmoi/chezmoi.boltdb`/`$HOME/.config/chezmoi/chezmoi.boltdb`/`%USERPROFILE%/.config/chezmoi/chezmoi.boltdb`
Location of the persistent state file.

### progress
TypeDefault`bool``false`
Display progress bars.

### scriptEnv
TypeDefault`object`none
Extra environment variables for scripts, hooks, and commands.

### scriptTempDir
TypeDefault`string`none
Temporary directory for scripts.

### sourceDir
TypeDefault`string``$XDG_SHARE_HOME/chezmoi`/`$HOME/.local/share/chezmoi`/`%USERPROFILE%/.local/share/chezmoi`
Source directory.

### tempDir
TypeDefault`string`from system
Temporary directory.

### umask
TypeDefault`int`from system
Umask.

### useBuiltinAge
TypeDefault`string``auto`
Use builtin age if age command is not found in $PATH.

### useBuiltinGit
TypeDefault`string``auto`
Use builtin git if git command is not found in $PATH.

### verbose
TypeDefault`bool``false`
Make output more verbose.

### workingTree
TypeDefault`string`source directory
git working tree directory.

## add

### add.encrypt
TypeDefault`bool``false`
Encrypt by default.

### add.secrets
TypeDefault`string``warning`
Action when secrets are found when adding files.

### add.templateSymlinks
TypeDefault`bool``false`
Template symlinks to source and home dirs.

## age

### age.args
TypeDefault`[]string`none
Extra args to age CLI command.

### age.command
TypeDefault`string``age`
age CLI command.

### age.identities
TypeDefault`[]string`none
age identity files.

### age.identity
TypeDefault`string`none
age identity file.

### age.passphrase
TypeDefault`bool``false`
Use age passphrase instead of identity.

### age.recipient
TypeDefault`string`none
age recipient.

### age.recipients
TypeDefault`[]string`none
age recipients.

### age.recipientsFile
TypeDefault`string`none
age recipients file.

### age.recipientsFiles
TypeDefault`[]string`none
age recipients files.

### age.suffix
TypeDefault`string``.age`
Suffix appended to age-encrypted files.

### age.symmetric
TypeDefault`bool``false`
Use age symmetric encryption.

## awsSecretsManager

### awsSecretsManager.profile
TypeDefault`string`none
AWS shared profile name.

### awsSecretsManager.region
TypeDefault`string`none
AWS region.

## azureKeyVault

### azureKeyVault.defaultVault
TypeDefault`string`none
Default Azure Key Vault name.

## bitwarden

### bitwarden.command
TypeDefault`string``bw`
Bitwarden CLI command.

### bitwarden.unlock
TypeDefault`bool``false`
Whether to unlock the Bitwarden CLI.

## bitwardenSecrets

### bitwardenSecrets.command
TypeDefault`string``bws`
Bitwarden Secrets CLI command.

## cd

### cd.args
TypeDefault`[]string`none
Extra args to shell in cd command.

### cd.command
TypeDefault`string`none
Shell to run in cd command.

## completion

### completion.custom
TypeDefault`bool``false`
Enable custom shell completions.

## dashlane

### dashlane.args
TypeDefault`[]string`none
Extra args to Dashlane CLI command.

### dashlane.command
TypeDefault`string``dcli`
Dashlane CLI command.

## diff

### diff.args
TypeDefault`[]string`see`diff`
Extra args to external diff command.

### diff.command
TypeDefault`string`none
External diff command.

### diff.exclude
TypeDefault`[]string`none
Entry types to exclude from diffs.

### diff.pager
TypeDefault`string`none
Diff-specific pager.

### diff.pagerArgs
TypeDefault`[]string`none
Extra args to the diff-specific pager command.

### diff.reverse
TypeDefault`bool``false`
Reverse order of arguments to diff.

### diff.scriptContents
TypeDefault`bool``true`
Show script contents.

## docker

### docker.command
TypeDefault`string``docker`
Docker CLI command.

## doppler

### doppler.args
TypeDefault`[]string`none
Extra args to Doppler CLI command.

### doppler.command
TypeDefault`string``doppler`
Doppler CLI command.

### doppler.config
TypeDefault`string`none
Default config (aka environment) if none is specified.

### doppler.project
TypeDefault`string`none
Default project name if none is specified.

## edit

### edit.apply
TypeDefault`bool``false`
Apply changes on exit.

### edit.args
TypeDefault`[]string`none
Extra args to edit command.

### edit.command
TypeDefault`string``$EDITOR`/`$VISUAL`
Edit command.

### edit.hardlink
TypeDefault`bool``true`
Invoke editor with a hardlink to the source file.

### edit.minDuration
TypeDefault`duration``1s`
Minimum duration for edit command.

### edit.watch
TypeDefault`bool``false`
Automatically apply changes when files are saved.

## ejson

### ejson.key
TypeDefault`string`none
The private key to use for decryption, will supersede using the keyDir if set.

### ejson.keyDir
TypeDefault`string``/opt/ejson/keys`
Path to directory containing private keys. Setting the $EJSON_KEYDIR environment variable will also set this value, with lower precedence.

## git

### git.autoAdd
TypeDefault`bool``false`
Add changes to the source state after any change.

### git.autoCommit
TypeDefault`bool``false`
Commit changes to the source state after any change.

### git.autoPush
TypeDefault`bool``false`
Push changes to the source state after any change.

### git.command
TypeDefault`string``git`
git CLI command.

### git.commitMessageTemplate
TypeDefault`string`none
Commit message template.

### git.commitMessageTemplateFile
TypeDefault`string`none
Commit message template file (relative to source directory).

### git.lfs
TypeDefault`bool``false`
Run git lfs pull after cloning.

## gitHub

### gitHub.refreshPeriod
TypeDefault`duration``1m`
Minimum duration between identical GitHub API requests.

## gopass

### gopass.command
TypeDefault`string``gopass`
gopass CLI command.

### gopass.mode
TypeDefault`string`none
See gopass functions.

## gpg

### gpg.args
TypeDefault`[]string`none
Extra args to GPG CLI command.

### gpg.command
TypeDefault`string``gpg`
GPG CLI command.

### gpg.recipient
TypeDefault`string`none
GPG recipient.

### gpg.recipients
TypeDefault`[]string`none
GPG recipients.

### gpg.suffix
TypeDefault`string``.asc`
Suffix appended to GPG-encrypted files.

### gpg.symmetric
TypeDefault`bool``false`
Use symmetric GPG encryption.

## hooks

### hooks.command.post.args
TypeDefault`[]string`none
Extra arguments to command to run after command.

### hooks.command.post.command
TypeDefault`[]string`none
Command to run after command.

### hooks.command.pre.args
TypeDefault`[]string`none
Extra arguments to command to run before command.

### hooks.command.pre.command
TypeDefault`[]string`none
Command to run before command.

## interpreters

### interpreters.extension.args
TypeDefault`[]string`none
See Interpreters.

### interpreters.extension.command
TypeDefault`string`special
See Interpreters.

## keepassxc

### keepassxc.args
TypeDefault`[]string`none
Extra args to KeePassXC CLI command.

### keepassxc.command
TypeDefault`string``keepassxc-cli`
KeePassXC CLI command.

### keepassxc.database
TypeDefault`string`none
KeePassXC database.

### keepassxc.mode
TypeDefault`string``cache-password`
See KeePassXC functions.

### keepassxc.prompt
TypeDefault`bool``true`
Prompt for password.

## keeper

### keeper.args
TypeDefault`[]string`none
Extra args to Keeper CLI command.

### keeper.command
TypeDefault`string``keeper`
Keeper CLI command.

## lastpass

### lastpass.command
TypeDefault`string``lpass`
LastPass CLI command.

## merge

### merge.args
TypeDefault`[]string`See`merge`
Extra args to three-way merge CLI command.

### merge.command
TypeDefault`string`none
Three-way merge CLI command.

## onepassword

### onepassword.cache
TypeDefault`bool``true`
Enable optional caching provided by op.

### onepassword.command
TypeDefault`string``op`
1Password CLI command.

### onepassword.mode
TypeDefault`string``account`
See 1Password Secrets Automation.

### onepassword.prompt
TypeDefault`bool``true`
Prompt for sign-in when no valid session is available.

## pass

### pass.command
TypeDefault`string``pass`
Pass CLI command.

## passhole

### passhole.args
TypeDefault`[]string`none
Extra args to Passhole CLI command.

### passhole.command
TypeDefault`string``ph`
Passhole CLI command.

### passhole.prompt
TypeDefault`bool``true`
Prompt for password.

## pinentry

### pinentry.args
TypeDefault`[]string`none
Extra args to pinentry CLI command.

### pinentry.command
TypeDefault`string`none
pinentry CLI command.

### pinentry.options
TypeDefault`[]string`See`pinentry`
Extra options for pinentry.

## protonPass

### protonPass.command
TypeDefault`string``pass-cli`
Proton Pass CLI command.

## rbw

### rbw.command
TypeDefault`string``rbw`
Unofficial Bitwarden CLI command.

## secret

### secret.args
TypeDefault`[]string`none
Extra args to secret CLI command.

### secret.command
TypeDefault`string`none
Generic secret CLI command.

## status

### status.exclude
TypeDefault`[]string`none
Entry types to exclude from status.

### status.pathStyle
TypeDefault`string``relative`
How to present the path to files in status output.

## template

### template.options
TypeDefault`[]string``["missingkey=error"]`
Template options.

## textconv

### textconv.
TypeDefault`[]object`none
See textconv.

## update

### update.apply
TypeDefault`bool``true`
Apply after pulling.

### update.args
TypeDefault`[]string`none
Extra args to update command.

### update.command
TypeDefault`string`none
Update command.

### update.recurseSubmodules
TypeDefault`bool``true`
Update submodules recursively.

## vault

### vault.command
TypeDefault`string``vault`
Vault CLI command.

## verify

### verify.exclude
TypeDefault`[]string`none
Entry types to exclude from verify.

## warnings

### warnings.
TypeDefault`object`none
See Warnings.
