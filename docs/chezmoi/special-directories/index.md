
# Special directories

All directories in the source state whose name begins with . are ignored by
default, unless they are one of the special directories listed here. All of
these directories are optional and are evaluated in a specific order described
in special files.
- The files in .chezmoidata/ directories are read in lexical order
  with any .chezmoidata.$FORMAT files in the source state.
- The files in .chezmoitemplates/ are made available for use in
  source templates.
- The files in .chezmoiscripts/ are read, templated, and according
  to their phase attributes (run_after_, run_before_, etc.) and lexical
  ordering.
- Files in .chezmoiexternals/ are read in lexical order with
  any .chezmoiexternal.$FORMAT files.
