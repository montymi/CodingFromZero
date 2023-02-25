cd ~/coding/python-testing # move to the correct repository

git init # initialize the git commands inside the local repository
git remote add origin <ssh url to remote repo> # add remote connection to specific repository

touch README.md # create README file
vim README.md # use text editor of choice
  
git checkout main # make sure you are on the <main> branch

git add .     # add all files to staging
git commit -m "Adding files to my first remote repository" # add changes to commit history
git push # files sent to server

git log # check commit history
