
export CLICOLOR=1

alias gs='git status'
alias cd..="cd .."
alias cp='cp -iv'                           # Preferred 'cp' implementation
alias mv='mv -iv'                           # Preferred 'mv' implementation
alias mkdir='mkdir -pv'                     # Preferred 'mkdir' implementation
alias ll='ls -FGlAhp'                       # Preferred 'ls' implementation
alias ls="ls -G"
alias less='less -FSRXc'                    # Preferred 'less' implementation
alias which='type -all'                     # which:        Find executables
alias ttop="top -R -F -s 10 -o rsize"


function lazygit() {
    git add .
    git commit -a -m "$1"
    git push
}

if [ -f /Applications/Xcode.app/Contents/Developer/usr/share/git-core/git-completion.bash ]; then
    . /Applications/Xcode.app/Contents/Developer/usr/share/git-core/git-completion.bash
fi

source /Applications/Xcode.app/Contents/Developer/usr/share/git-core/git-prompt.sh



  export PS1='\w\[\033[01;32m\]$(__git_ps1)\[\033[00m\]\$ '
