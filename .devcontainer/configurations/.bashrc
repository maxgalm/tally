bash $HOME/.scripts/info-version.sh

echo "Initializing VSCode Terminal..."

alias version='$HOME/.scripts/info-version.sh'

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

alias ls='ls -hFG'
alias l='ls -lF'
alias ll='ls -alF'
alias lt='ls -ltrF'
alias ll='ls -alF'
alias lls='ls -alSrF'
alias llt='ls -altrF'

alias tarc='tar cvf'
alias tarcz='tar czvf'
alias tarx='tar xvf'
alias tarxz='tar xvzf'

alias g='git'
alias less='less -R'
alias os='lsb_release -a'
alias vi='vim'

echo "Making VSCode Terminal colorful..."

# Colorize directory listing
alias ls="ls -ph --color=auto"

# Colorize grep
if echo hello|grep --color=auto l >/dev/null 2>&1; then
  alias grep="grep $GREP_OPTIONS"
  export GREP_COLOR='1;32'
fi

# Shell
export CLICOLOR="1"
if [ -f $HOME/.scripts/git-prompt.sh ]; then
  source $HOME/.scripts/git-prompt.sh
  export GIT_PS1_SHOWDIRTYSTATE="1"
  export PS1="\[\033[40m\]\[\033[34m\][ \u@\H:\[\033[36m\]\w\$(__git_ps1 \" \[\033[35m\]{\[\033[32m\]%s\[\033[35m\]}\")\[\033[34m\] ]$\[\033[0m\] "
else
  export PS1="\[\033[40m\]\[\033[34m\][ \u@\H:\[\033[36m\]\w\[\033[34m\] ]$\[\033[0m\] "
fi
export LS_COLORS="di=34:ln=35:so=32:pi=33:ex=1;40:bd=34;40:cd=34;40:su=0;40:sg=0;40:tw=0;40:ow=0;40:"

# Git
source /usr/share/bash-completion/completions/git

# Enable command history
export PROMPT_COMMAND='history -a'
export HISTFILE=$XDG_CACHE_HOME/.bash_history

eval "$(direnv hook bash)"

# make history search match whatever is written in
# the console
if [[ $- == *i* ]]
then
    bind '"\e[A": history-search-backward'
    bind '"\e[B": history-search-forward'
fi

# Take local proxy only if proxy not set by docker
export HTTPS_PROXY="${HTTPS_PROXY:-${https_proxy:-$HTTPS_LOCAL_PROXY}}"
export HTTP_PROXY="${HTTP_PROXY:-${http_proxy:-$HTTP_LOCAL_PROXY}}"
export https_proxy="${https_proxy:-$https_local_proxy}"
export http_proxy="${http_proxy:-$http_local_proxy}"
#Add localhost to NO_PROXY in case it is not yet set
export NO_PROXY=${NO_PROXY:+$NO_PROXY,}localhost
#Lower case for robustness
export no_proxy=${no_proxy:+$no_proxy,}localhost

# Source user defined aliases if present
if [[ -f "${WORKSPACE_FOLDER}/.user_aliases" ]]; then
  source "${WORKSPACE_FOLDER}/.user_aliases"
fi