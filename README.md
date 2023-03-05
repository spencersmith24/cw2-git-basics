# Git Basics
## Welcome
Welcome! Since you're cloning this repository from a remote, there's a few steps that you get to skip. Notably:
- `git init` to create a repository
- `git remote add <remote-name> <remote-url> && git push --set-upstream <remote-name> <master-name>` to set a remote repository and push it upstream
- making the initial commit

This is about the point where you'd start if you created the repository on GitHub and cloned it down to your local machine. However, this repository isn't empty—there have been some commits already made and there are already some files here. To view the commits that have already been made to this repository (including to this file), use `git log`.

---
## Making changes
Let's edit some code! There's a folder called “players,” and inside there’s some files. There's some code (players_viewer.py), and some data that that code pulls from (players.xml). Before you make any changes, make sure to update your working tree and local repository with `git pull`. You should get the message that you're already up-to-date. Edit the file _players.xml_ to include a tag with your name, following the syntax of the name(s) already there, e.g.,
```xml
<player name="Your Name">Your GitHub username</player>
```
… with child tags for your favorite things, following the format,
```xml
<favorite type="thing">Thing</favorite>
<!-- such as… -->
<favorite type="food">Pizza</favorite>
```

Save the file, and check your `git status`. If done correctly, you should see an output stating you have one edited file, players.xml.

Stage the file with `git add`. Your `git status` should now show the file as staged.

Make your first commit with `git commit -m "<message>"`.

Push that commit upstream with `git push`!

## Staying up-to-date
Because you're the only one working on this fork of the repository, in order to pull changes from remote, you'll need to manually make some changes on the remote repository. Luckily, you can edit files manually on GitHub by navigating to the file and clicking the pencil button in the top right of the view pane, or using _vscode.dev_ by pressing the period key on your keyboard while viewing the file. Make any arbitrary edit, commit it, and then use `git pull` on your local machine to update it, verifying that the change now exists on your local files!

Now, make another change on remote, and before pulling, make a commit on your local repository _to a different file_. Now, when you use `git pull`, you'll need to make a _merge commit_—either set a commit message or leave the default one, save the file in the default text editor (if your OS automatically chooses Vim, exit by typing `:wq` and pressing Enter). Then, push that merge commit with `git push`.

## Resolving a merge conflict
This time, make a commit on the remote repository to a file, then commit on your local machine to the same file. Then, try to `git pull`, and you should experience a _merge conflict_. Open the affected file in your text editor of choice, remove the lines added by Git and resolve the merge conflict as necessary, stage the file, commit, and push. Congratulations! You've resolved a merge conflict!