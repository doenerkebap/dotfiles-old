HISTFILE=~/.zsh_history        # history filename
HISTSIZE=10000                 # ?
SAVEHIST=10000                 # ?
setopt APPENDHISTORY           # add history
setopt EXTENDED_HISTORY        # add timestamps to history
setopt HIST_IGNORE_ALL_DUPS    # no duplicates
setopt HIST_REDUCE_BLANKS      # no superfluous white space
setopt SHARE_HISTORY           # import from and append to history file

setopt CORRECT                 # correct spelling

setopt COMPLETE_ALIASES        # prevents aliases from being internally substituted before completion is attempted.
setopt COMPLETE_IN_WORD        # cursor stays at position after completion

setopt PROMPT_SUBST            #  allow parameter expansion, command substitution and arithmetic expansion in prompt

bindkey -v                     # ?

zle-line-init() { zle -K vicmd; }
zle -N zle-line-init
