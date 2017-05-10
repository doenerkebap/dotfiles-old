typeset -U config_files
config_files=($ZSH/**/*.zsh)
# exclude everything in vim.symlink
config_files=(${config_files[@]//*vim.symlink*})
# exclude path and aliases (already loaded in .zshenv)
config_files=(${${config_files:#*/path.zsh}:#*/aliases.zsh})


# load everything but the completion files
for file in ${config_files:#*/completion.zsh}
do
  source $file
done

# initialize autocomplete here, otherwise functions won't be loaded
autoload -U compinit
compinit

# load every completion after autocomplete loads
for file in ${(M)config_files:#*/completion.zsh}
do
  source $file
done

unset config_files
