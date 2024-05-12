# Tally

Tally is an app with which users can book purchases of any goods, whereby the user's balance is tracked.

## Getting started

1. Install [Visual Studio Code](https://code.visualstudio.com/download)
2. Install [Docker](https://docs.docker.com/get-docker)
3. Run ``setup_host.sh`` to install the [Visual Studio Code Devcontainers Extension](https://code.visualstudio.com/docs/devcontainers/containers)
4. Run ``build_docker.sh`` to pre-build the Visual Studio Code Devcontainer

# Useful CLI commands

## Django

If you want to start the server on your local machine, you have to do the following steps:

1. Change the directory into the django project

```
$ cd tally
```

2. Start the server

```
$ python3 manage.py runserver
```

---

If you changed the data models, you have to make migrations and migrate the database using those migration files. **Make sure you are in the directory of the django project.**

1. Generating migration files

```
$ python3 manage.py makemigrations
```

2. Migrate the database

```
$ python3 manage.py migrate
```

You can read more about this in the official Documentation of the [Django Rest-Framework](https://www.django-rest-framework.org/)

## GIT

**How to check a repository's status:**

This command will show the status of the current repository including staged, unstaged, and untracked files.

```
$ git status
```

---

**How to add a file to the staging area:**

The command below will add a file to the staging area. Just replace filename_here with the name of the file you want to add to the staging area.

```
$ git add filename_here
```

If you want to add all files in your project to the staging area, you can use a wildcard . and every file will be added for you.

```
$ git add .
```

Normally, calling ``git add \<file>`` will add all the changes in that file to the index, but add supports an interesting option: ``--patch``, or ``-p`` for short.

When you pass this option to add, instead of immediately adding all the changes in the file to the index, it goes through each change and asks you what you want to do, and looks like this:

```
@@ -24,7 +32,12 @@ module CoreMIDI
   ]

   functions.each do |func|
-    attach_function *func
+    begin
+      attach_function *func
+    rescue Exception => e
+      $stderr.puts "Couldn't attach function #{func.first}"
+      raise
+    end
   end

   def midi_read_proc()
Stage this hunk [y/n/a/d/K/j/J/e/?]?
```

At the top is some diff info about the current position in the file, followed by the actual diff of the source code (called “hunk”), and below that are your available options. Pressing ? will give you a short explanation for each one, but the ones I use most often are:

* ``y`` - Yes, add this hunk
* ``n`` - No, don’t add this hunk
* ``d`` - No, don’t add this hunk and all other remaining hunks.
* ``s`` - Split the hunk into smaller hunks. This only works if there’s unchanged lines between the changes in the displayed hunk.
* ``e`` - Manually edit the hunk.

---

**How to commit changes with a message:**

You can add a commit message without opening the editor. This command lets you only specify a short summary for your commit message.

```
$ git commit -m "your commit message here"
```

---

**How to create a new branch:**

By default, you have one branch, the main branch. With this command, you can create a new branch. Git won't switch to it automatically – you will need to do it manually with the next command.

```
$ git branch branch_name
```

**How to switch branches:**

Switch to a specified branch. The working tree and the index are updated to match the branch. All new commits will be added to the tip of this branch.

```
$ git switch branch_name
```

**How to show the commit log as a graph of all branches:**

We can use ``--graph`` to get the commit log to show as a graph. Also, ``--oneline`` will limit commit messages to a single line. The option ``--decorate`` prints out the ref names of any commits that are shown and ``--all`` specifies the command should be run for all branches.

```
$ git log --graph --oneline --decorate --all
```

---

**How to push a new branch to a remote repo:**

If you want to push a branch to a remote repository you can use the command below. Just remember to add ``-u`` to create the branch upstream:

```
$ git push -u origin branch_name
```