# Instructions

In this challenge, you will create your first commit. Happy branching! 🎋

## 🎯 Data and Context

For this challenge we'll create text files in VS Code and then push them to a remote repository on GitHub.

This time, you won't save different versions of your work with names like `Thesis_FINAL_FINAL_FINAL.doc`. Instead we will use the power of Git to track changes in your files!

## 📁 Setup

To make challenge completion simpler, we have added terminal instructions to challenges that have test suites.

If you haven't already, **copy the terminal instructions at the top of this page and run them in your terminal**.

This will:

- Create and navigate to a directory (folder) for this challenge in your terminal
- Download all of the files for this challenge
- Set up a new repository locally and on GitHub
- Open the challenge in VS Code
- Run the test suite for this challenge

At this point the tests will fail with a lot of red, that is expected: we haven't started working yet. Keep on reading.

Run the following command in the terminal to check you are in the right directory:

```bash
pwd
```

Your result should look like this:

```bash
~/code/<user.github_nickname>/{{ local_path_to("03-Data-Transformation/08-Intro-To-Git-And-Versioning/02-First-Repository") }}/
```

The `~` sign ("tilde") at the start of the line will be replaced by either `/Users/{YOUR_COMPUTER_USERNAME}` (macOS) or `/home/{YOUR_COMPUTER_USERNAME}` (Windows / Linux). The `~` is a terminal shorthand for your personal home folder on your machine.

❌ If it doesn't, consult a TA!

✅ If it does, then you are ready to take on this challenge!

Want to know where git is tracking your changes? Enter the following command in your terminal:

```bash
ls -a
```

You will see a directory appearing called `.git`. This directory contains files that will track all of the changes made to the files inside of your local repository!

<details>
<summary markdown="span">💡 Why do I need to add -a?</summary>

Adding `-a` to `ls` shows all files, including the hidden ones.

Files that start with `.` are hidden from standard `ls` commands (and by default in your file system).

</details>

## 🧩 Implementation

### 1. Working in VS Code

We'll be using VS Code to create and edit some text files. Let's open VS Code at our repository's location.

1. Open the folder with VS Code using the terminal

    <details>
    <summary markdown="span">💡 Hint</summary>

    You can open your current directory in VS Code using the command `code .` in the terminal.

    </details>

    It's also possible to open the folder directly from VS Code as shown in the screenshot below:

    ![Screenshot of VS Code: clicked file from the menu bar, then the Open Folder...](https://wagon-public-assets.s3.eu-west-3.amazonaws.com/04-Data-Collection/05-Intro-To-Git-And-Versioning/02-First-Commit-asset-2-Screenshot_2023-09-21_at_15.34.59.png)

    You should see any files inside your folder on the left hand side.

### 2. Your first commit

> 💡 Note that your current branch will be `master`, but if you see `main` in explanations online that's also a default branch name. In the last few years main/default branch names have generally changed to be `main` and not `master`. If you want to read more about the change in naming conventions, take a look [at this link](https://github.com/github/renaming?tab=readme-ov-file).

Let's create a file and commit it:

1. In VS Code, create a new file called `zen.txt`. Let's add just the first two lines of [Tim Peters' `Zen of Python` rules](https://peps.python.org/pep-0020/):

    ```markdown
    Beautiful is better than ugly.
    Explicit is better than implicit.
    ```

1. Save and go back to your terminal.  Enter the command `git status` to see the status of your files. What do you expect to see?

    <details>
    <summary markdown="span">💡 Hint</summary>

    Git has detected a new file has been added. Git tracks every change you make! It will show the name and inform you that it is currently untracked!

    </details><br>

1. In the terminal, you need to add this file to start tracking it.

    <details>
    <summary markdown="span">💡 Hint</summary>

    To add the file you'll need to `git add <file_name>`

    </details><br>

1. Then, you'll need to create a new snapshot of your changes by creating a new `commit`. Use “First two lines of zen” as the commit message.

    <details>
    <summary markdown="span">💡 Hint</summary>

    To commit the file you'll need to `git commit -m "First two lines of zen"`

    Always add a message to your commits with `-m` (short for `--message`), it let's other developers (and even more importantly you!) know what you were changing.

    </details><br>

1. Now push your commit to your remote repository.

    <details>
    <summary markdown="span">💡 Hint</summary>

    To push your commit you'll use `git push origin master`, but be aware, that we don't always just push our master branch, you will use `git push origin <BRANCH_NAME>` depending on the name of your branch. We will cover this in more detail later!

    </details><br>

1. Go to [github.com](http://github.com/) to your newly created repository.

    You'll find it at this address `https://github.com/<user.github_nickname>/data-analytics-first-repository`

    You should now see your zen text file on your remote repository.

    If your computer is lost, stolen, or damaged, you can pull your code from GitHub. You won’t lose your work anymore. Don’t forget to push your code regularly!

## 📤 Submission

Shortly after your push is completed, [GitHub will tell Kitt](https://sebastien.saunier.me/blog/2014/04/21/practical-example-of-using-git-in-a-school.html) about this push thanks to a [webhook](https://developer.github.com/webhooks/).

Kitt will then pull your code, run `make` and update your challenge status (completion + style score). You should also see how your buddy of the day is doing!

## 🏁 Finishing up

You've updated a file, created your first commit, and pushed - congratulations! 🎉

There was a few steps with setting everything up, but we are now primed to git into some deeper git concepts!
