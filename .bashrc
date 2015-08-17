alias gs='git status'
alias ls='ls --color=auto --format=vertical'
alias ll='ls -lh'

PS1='\w\[\033[01;32m\]$(__git_ps1)\[\033[00m\]\$ '

function lazygit() {
    git add .
    git commit -a -m "$1"
    git push
}
