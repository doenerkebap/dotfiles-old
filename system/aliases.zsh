alias q='exit'
alias c='clear'
alias fm='ranger'

alias ll='ls -l'
alias la='ls -A'
alias lla='ls -lA'
alias l.='ls -d .*'

alias cd..="cd .."
alias ..='cd ..'

alias ranger='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'
