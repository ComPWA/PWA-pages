Recording the workflow: committing
----------------------------------

Chances are that you're already familiar with Git from cloning source code of
some online project. At core, however, Git is just a tool for managing file
versions, which can be done completely locally on any collection of files
you're working on. It's quite easy to try this out, so easy in fact that it may
seem trivial, but it's a helpful exercise to familiar with the fundamental Git
concepts.

So, let's use Git to `apply version control
<https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>`_ over
some local folder. Create an empty folder somewhere on your system and navigate
into it:

.. code-block:: shell

  mkdir test
  cd test

We call this folder the **working directory**: it's the place where you work on
your files. When we now run:

.. code-block:: shell

  git init

we create a folder :file:`.git` within the working directory. This folder is
the **Git repository** and it's the place where Git stores all settings for
that folder and keeps a version of each tracked file.

Now it's just a matter of adding files to the working directory, modifying
them, and―most importantly―telling Git to store a version of those files now
and then. In that process, there is a third concept to be aware of: the
**staging area**. In order to tell Git to store a selection of files, you have
*stage* them. In our example, let's create some files in the working directory
and stage them:

.. code-block:: shell

  touch file1.txt file2.txt # create empty files
  git add file*.txt         # stage the files

If you run :command:`git status`, you can see that :file:`file1.txt` and
:file:`file2.txt` fall under the "Changes to be committed". This means that the
two files are ready to be registered in the :file:`.git` folder. You can
:command:`git add` additional files if there were any, but let's say we are
satisfied with this selection and want to register it as a change to the
repository.

As opposed to most other version control systems, Git works in a kind of
snapshots (called "`commits
<https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F#_snapshots_not_differences>`_")
that store **all files**, but does so smartly: files that haven't changed with
regard to the previous commit are only stored as a link to that previous
commit. A commit has to be given a short description (a message), but is always
uniquely identifiable, because it is marked with a `SHA-1 checksum
<https://en.wikipedia.org/wiki/SHA-1>`_ over all files that it contains (plus a
timestamp). To :command:`git commit` the staged file with a certain message
(:command:`-m`), run:

.. code-block:: shell

  git commit -m "initial commit"

We have now created a first commit for this repository. Now let's edit one of
the files and see what happens:

.. code-block:: shell

  echo "some content" > file1.txt
  git status

You'll see that Git notices that :file:`file1.txt` is "modified", but that it
is "not staged". This is because there are two different files now: the empty
one that was recorded under the first commit in the :file:`.git` repository and
the modified one in your working directory. You can see the difference between
those two files with :command:`git diff`.

To register this new change, stage the changed file and commit it. We can
lazily stage all (:command:`-A`), because already know from :command:`git
status` that only :file:`file1.txt` was changed, and Git won't stage files that
weren't changed:

.. code-block:: shell

  git add -A
  git commit -m "feat: add content"

As you see, Git has registered that "1 file changed" with "1 insertion". If you
now run :command:`git log`, you'll see that there are two commits, each with a
unique SHA-1 code. With :command:`git log --oneline`, you'll have a more
condense overview with an abbreviated SHA-1. Here it's ``e41a065`` and
``e28a30c``, but it can be anything as the SHA-1 also entails the timestamp.

It's important to realize that the Git repository now contains *three files*:
an empty :file:`file1.txt` in the first commit, a :file:`file1.txt` with "some
content" in the second commit, and empty :file:`file2.txt` in both commits.
This is the core of version control: Git has organised these three file
versions in two 'snapshot' commits and has recorded how the files in those
commits relate to each other.

As you can see in the :command:`git log`, we are currently situated in the
second commit (indicated by **HEAD**). In addition, by running :command:`git
status`, we know that there is "nothing to commit" and that the "working tree"
is "clean". This means that the files we see in the working directory in the
working are exactly the same as the ones in that latest commit.

Now, Git allows you to "checkout" the files of the previous commit. You can do
this by using its SHA-1 (abbreviated is fine), or by a relative reference,
namely the one commit above (``^``) the one that the ``HEAD`` points to:

.. code-block:: shell

  git checkout HEAD^

(In the above situation, this would be equivalent to :command:`git checkout
e28a30c^` and :command:`git checkout e41a065`). Now :file:`file1.txt` is again
the good old, empty version. We've now mastered the basic operations for doing
version control with Git and are ready to learn about branching!

For more of these fundamental operations, see `this page
<https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository>`_.

.. figure:: https://git-scm.com/book/en/v2/images/areas.png
  :alt: the three stages
  :align: center

  Main concepts when registering changes with Git.
