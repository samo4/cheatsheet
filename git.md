
###### How to get repository, that you haven't worked on before:
```
git clone https://rs.unfuddle.com/git/rs_mercedes/
```
###### How to check what was added/replaced/delete before you add files to a commit
```
git status
```
###### How to commit
Key point is that commit is always a two stage process: you add a file to commit, then you commit. GIT will warn you if some files were deleted (a "deletion" must also be commited) and propose what to do.
```
git add .
git comit –m "message"
```
###### How to move your changes to central repository
```
git push
```
###### How to get things that other people did
```
git pull
```
###### List all branches (local and remote).. 
What is a branch you say? If a project is done and you start develoment of a new feature, it's expected that this development will take some time. In the mean time a new bug might show up and you will need to fix it. So in order to be able to fix bugs without publishing your current development we use branches.
```
git branch --list -a
```
###### Remove single file from add 
```
git reset -- main/dontcheckmein.txt
```
###### Delete all of your changes to file and revert to content as it is in main repository:
```
git checkout – pot_do_datoteke
```
###### Delete all of your changes and revert to state in main repository:
```
git reset --hard HEAD
```

