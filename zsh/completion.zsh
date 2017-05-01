zstyle ':completion:*' completer _complete _ignored _correct        # ?
zstyle ':completion:*' matcher-list '' 'm:{[:lower:]}={[:upper:]}'  # ?
zstyle :compinstall filename '/home/benjamin/.zshrc'                # ?

autoload -Uz compinit                                               # ?
compinit                                                            # ?
