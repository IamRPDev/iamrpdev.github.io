
# edit-encrypted filename...

Edit the encrypted files filenames.

Each filename is decrypted to a temporary directory, the editor is invoked on
the decrypted files. After the editor returns, each the decrypted file is
re-encrypted.

## Examples

chezmoi edit-encrypted encrypted_file
