Trying out different ideas: branching
-------------------------------------

Now that we're familiar with the :doc:`concept of a commit <commit>` and know
how to record changes to our code base, we can experiment with `what many call
Git's "killer feature"
<https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell>`_:
branching.

Branching allows you to, well, 'branch off' a series of snapshot commits in
some other direction, and merge that series with another branch later on. This
is particularly useful when working together with others: each can work in
their own branch and you can safely bring those ideas together later on (see
:doc:`remotes`).

At core, a branch is just a label to a commit that moves on to the next if you
:command:`git commit`. In fact, when you make your first commit after
initializing a repository, Git automatically creates a branch called
``master``. In :doc:`our example <commit>`, you can see this when running:

.. code-block:: shell

    git branch

There is a ``master`` branch next to the ``HEAD`` (which is in a "detached"
state). The master moved along on to the second commit you made and stayed
there after you checked out the first commit. We can start a new branch from
that first commit (the one that contains two empty files). Let's call this new
branch ``new_idea``:

.. code-block:: shell

    git branch new_idea
    git branch -v

The second commands prints the existing branches along with the commits they
point to. You'll see that there is a ``new_idea`` branch pointing to the first
commit, next to the ``master`` branch, which is indeed pointing to the second
commit ("feat: add content"). The ``HEAD`` is still "detached", even though it
points to the same commit as ``new_idea``. To let the ``HEAD`` point to the new
branch, run:

.. code-block:: shell

    git checkout new_idea

.. sidebar:: Checkout ambiguity

    The :command:`git checkout` command is a tricky one: it `functions
    differently depending on context
    <https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified>`_. In the
    context of the examples here, :command:`git checkout` does two things: it
    (1) tries to unpack the files of the branch to which you try to switch to
    the working directory and, (2) if that succeeds, moves the ``HEAD`` to that
    other branch. In this context, :command:`git checkout` is a safe to use:
    Git will warn you and abort the checkout if the unpacking were to overwrite
    *modified* files.

    Imagine, however, that you have modified :file:`file1.txt` and left it
    unstaged. If you now run :command:`git checkout file1.txt`, Git would
    overwrite :file:`file1.txt` with the version of the latest commit to the
    current branch **without warning**. The behaviour is completely different
    than before: Git doesn't move ``HEAD`` either. To address the confusion,
    the Git developers `introduced two new commands
    <https://www.infoq.com/news/2019/08/git-2-23-switch-restore/>`_, but
    checkout remains most commonly used.

In this case, all this command did, was let the ``HEAD`` point to the
``new_idea`` branch. Remember that the ``HEAD`` represents the state of the
working directory. In fact, the ``HEAD`` is literally a file :file:`.git/HEAD`
containing one line that tells to which commit or branch it points. When the
``HEAD`` points to a commit (not a branch), it is detached. (As you probably
already noticed from the terminal output when creating the ``new_idea`` branch,
it is possible to do the branch+checkout step in one go with :command:`git
checkout -b new_idea`).

We can move the ``new_idea`` branch forward by modifying some files, staging
them, and creating a new commit from those changes:

.. code-block:: shell

    echo "this content is much better!" > file1.txt
    echo "from the new idea" > file2.txt
    git add -A
    git commit -m "fix: add content to files"

There is a nice way to visualize the current situation (so nice, in fact, that
we label it):

.. code-block:: shell
    :caption: Visualize branching tree
    :name: visualize-branches

    git log --graph --all --oneline

This shows that there are now three commits: the initial commit, the commit to
which the ``master`` branch points, and the commit to which the ``new_idea``
branch and the HEAD currently point. The dashes also nicely display that the
``new_idea`` branch **diverted** from the ``master`` branch and that the
"initial commit" is their common parent. We can continue developing the
``new_idea`` branch while the ``master`` branch stays where it is:

.. code-block:: shell

    mkdir folder
    mv file2.txt folder/moved_file.txt
    git add folder
    git rm file2.txt
    git status -s
    git commit -m "refactor: move file"

Notice that we used :command:`git status -s`, a nice way to summarize the
situation in the working tree. In this case, it shows that :file:`file2.txt`
was renamed (moved): ``file2.txt -> folder/moved_file.txt``: when staging
files, Git tries to see how the new situation relates to that of the previous
commit. In this case, it noticed that :file:`file2.txt` was only moved and
renamed.

If we again :ref:`visualize the branching structure <visualize-branches>`, we
see that the ``new_idea`` branch moved forward by one commit. When we checkout
the ``master`` again, Git removes the ``new_idea`` versions of
:file:`file1.txt` and :file:`file2.txt` from the working directory and unpacks
the old ones from the ``master`` branch (but see the sidebar note).

.. code-block:: shell

    git checkout master
    ls

Let's see what happens if we `merge
<https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>`_
the ``new_idea`` branch *into* the ``master``:

.. code-block::

    git merge new_idea

Wow, what's this?? Git tells it is "removing :file:`file2.txt`", but then runs
into a conflict for :file:`file1.txt`. Here we see that *Git does line-wise
file comparisons*! Git noticed that the line in :file:`file1.txt` is different
in ``new_idea`` than in ``master``. It has indicated that difference within the
file itself and is waiting for your input. If you have a look in the file:


.. code-block:: shell

    vi file1.txt

you'll see:

.. code-block::

    <<<<<<< HEAD
    this content is much better!
    =======
    some content
    >>>>>>> master

It shows that "some content" was the line from the ``master`` branch and "this
content is much better!" came in from the ``HEAD`` (the ``HEAD`` was moved to
``new_idea``). *It's up to you what to do with this.* You can choose one of
these two, write something entirely new, or leave it like this (not
recommended, of course). If you think the merge is completely messed up, you
can even just run :command:`git merge --abort` to land back safely in the
untouched ``master`` branch!

Here, let's just remove all lines but for "some content" (the ``master``) and
safe the file. Then it's a matter of staging the modifed :file:`file1.txt` and
creating a new **merge commit**. This time, we commit the :command:`-m` message
flag for the :command:`git commit` command. Git will launch `vi
<https://en.wikipedia.org/wiki/Vi>`_ with a pre-generated merge message. Just
safe it (:command:`:x`) and Git will use it as a commit message.

.. code-block:: shell

    git add file1.txt
    git commit

If we again :ref:`visualize the branch structure <visualize-branches>`, we see
something cool: the "initial commit" branches off into two branches, then
merges into a final "Merge branch 'new_idea'" commit to which the ``master``
branch has moved. The ``new_idea`` branch is in its old place, but we can just
delete it now that the 'new idea' has been merged with the ``master``:

.. code-block:: shell

    git branch -d new_idea

That's it, the fundamentals of branching! To be sure, the example here is
trivial, but what makes Git so powerful is that it can handle large numbers of
files and commits while the branches develop onwards and can do this comparing
and merging blazingly fast.

Branching has a nice application locally: you can just create a branch from one
of your commits, develop a bit, checkout another branch and work on that, and
merge the changes later on. But branching becomes much more important when
working together in a team. For this, we need to :doc:`dive into remotes
<remotes>`.
