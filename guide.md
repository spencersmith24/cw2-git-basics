# Git Basics
## Welcome
Welcome! Since you're cloning this repository from a remote, there's a few steps that you get to skip. Notably:
- `git init` to create a repository
- `git remote add <remote-name> <remote-url> && git push --set-upstream <remote-name> <master-name>` to set a remote repository and push it upstream
- making the initial commit
This is about the point where you'd start if you created the repository on GitHub and cloned it down to your local machine. However, this repository isn't empty—there have been some commits already made and there are already some files here. To view the commits that have already been made to this repository (including to this file), use `git log`.
---
## Making changes
Let's edit some code! There's a folder called “players,” and inside there’s some files. There's some code (players_viewer.py), and some data that that code pulls from (players.xml). Edit the file _players.xml_ to include a tag with your name, following the syntax of the name(s) already there, e.g.
```xml
<player name="Your Name">Your GitHub username</player>
```
Save the file, and check your `git status`. If done correctly, you should see an output stating you have one edited file, players.xml.

Stage the file with `git add`. Your `git status` should now show the file as staged.

Make your first commit with `git commit -m "<message>"`.

Push that commit upstream with `git push`!