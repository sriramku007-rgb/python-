1.What is the difference between git clone and git pull?

GIT CLONE 
  To copy an entire remote repository to your local machine for the first time
  git clone <repository_url>
GIT PULL
  To update your existing local repository with the latest changes from the remote
  git pull

2.In which situation would you create a new branch instead of committing directly to the main branch?

In situation where i was working in a project with the team mates,To test and fix the issue safely 
without breaking existing code i'll create a New Branch instead of
commiting directly inton the Main Branch'

3. List the exact command sequence to initialize a repository, add files, commit them, and push to GitHub.

>Initialize a new Git repository
git init
>Add your files to staging
git add
>Commit the changes
git commit -m 
>GitHub repository
git remote add origin https://github.com/your-username/your-repo.git
>Push the commit to GitHub
git push -u origin main