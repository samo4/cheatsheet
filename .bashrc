alias gpu='git pull'
alias gpsh='git push'
alias gs='git status'
alias ls='ls --color=auto --format=vertical'
alias ll='ls -lh'
alias gl="git log --pretty=format:'%C(yellow)%h %Cred%ad %C(auto)%an%Cgreen%d %Creset%s' --date=short"

PS1='\w\[\033[01;32m\]$(__git_ps1)\[\033[00m\]\$ '

function lg() {
    git add .
    git commit -a -m "$1"
    git push
}
