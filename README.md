# Git Basics
## Welcome
Welcome! Since you're cloning this repository from a remote, there's a few steps that you get to skip. Notably:
- `git init` to create a repository
- `git remote add <remote-name> <remote-url> && git push --set-upstream <remote-name> <master-name>` to set a remote repository and push it upstream
- making the initial commit

This is about the point where you'd start if you created the repository on GitHub and cloned it down to your local machine. However, this repository isn't empty—there have been some commits already made and there are already some files here. To view the commits that have already been made to this repository (including to this file), use `git log`.

If you're here on the GitHub website without any idea what to do, don't fret — your job is to create a _fork_ of this repository and then _clone_ that forked repository onto your local machine. You can fork this repository on the page you’re probably already on by clicking _Fork_ in the top-right corner.

![image](https://github.com/rokolinkon/cw2-git-basics/assets/70546234/e4809fa0-a303-4e00-85da-8b5938500e1e)

Then, after you're finished with that, you'll have a repository of your own by the same name, which you can find at `your-github-username/cw2-git-basics`. Now you have the URL you’ll need to clone the repository! You can do that with the command…

```bash
git clone https://github.com/your-github-username/cw2-git-basics
```
Simple, right? Now we can begin!

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
… so that it looks something like …
```xml
<player name="Melody">rokolinkon
    <favorite type="food">Cincinnati Chili</favorite>
    <favorite type="game">Pokémon</favorite>
</player>
```

Save the file, and check your `git status`. If done correctly, you should see an output stating you have one edited file, players.xml.

Stage the file with `git add`. Your `git status` should now show the file as staged.

Make your first commit with `git commit -m "<message>"`.

Push that commit upstream with `git push`!

## Staying up-to-date
Because you're the only one working on this fork of the repository, in order to pull changes from remote, you'll need to manually make some changes on the remote repository. Luckily, you can edit files manually on GitHub by navigating to the file and clicking the pencil button in the top right of the view pane, or using _vscode.dev_ by pressing the period key on your keyboard while viewing the file. Make any arbitrary edit, commit it, and then use `git pull` on your local machine to update it, verifying that the change now exists on your local files!

Now, make another change on remote, and before pulling, make a commit on your local repository _to a different file_. Now, when you use `git pull`, you'll need to make a _merge commit_—either set a commit message or leave the default one and save the file in the default text editor. Then, push that merge commit with `git push`.

## Resolving a merge conflict
This time, make a commit on the remote repository to a file, then commit on your local machine to the same file. 

On GitHub, edit `players.xml` to add a child key under the `player` tag with `name="Melody"`:
```xml
<favorite type="operating system">macOS</favorite>
```

Then, on your local machine, without pulling first, add _another_ tag to Melody:
```xml
<favorite type="Pokémon">Nidorina</favorite>
```

Commit that, then try to `git pull`, and you should experience a _merge conflict_. Open the affected file in your text editor of choice—you should see something like this:
![image](https://user-images.githubusercontent.com/70546234/223152140-50b363e9-16cd-4168-866f-385c164105d7.png)

Resolve the merge conflict by just removing the lines that Git has added automatically—this will, effectively, since these are small edits, merge both of the changes together, remote _and_ local. Stage the file, commit, and push. Congratulations! You've resolved a merge conflict!

---
## Ignoring files
Suppose you want to edit this file now that you're done with the basics—add a file at the root of this repository called `.gitignore` and add two lines:
```
README.md
.gitignore
```
Then save that file, and add your name into this box:
```
spencer
```
Then, check your `git status`, and this file should be ignored!
