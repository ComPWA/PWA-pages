.. |br| raw:: html

  <br />

GitHub
------

.. warning::

  Old text from here on

If you are new to git, maybe you should read some documentation first, such as
the `Git Manual <https://git-scm.com/docs/user-manual.html>`_, `Tutorial
<http://rogerdudler.github.io/git-guide/>`_, a `CheatSheet
<https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf>`_.
The `Git Pro <https://git-scm.com/book/en/v2>`_ book particularly serves as a
great, free overview that is a nice read for both beginners and more
experienced users.

For your convenience, here is the Git workflow you should use if you want to
contribute:

1. Log into GitHub with your account and fork the ComPWA repository
2. Get a local copy of repository: |br|
   ``git clone git@github.com:YOURACCOUNT/pycompwa.git`` |br|
   (this uses the SSH protocol, so you need to `set your SSH keys
   <https://help.github.com/en/github/authenticating-to-github/managing-commit-signature-verification>`_
   first)
3. Add the main repository as a second remote called ``upstream``: |br|
   ``git remote add upstream git@github.com:ComPWA/pycompwa.git``

.. note::
  You can name the repository with any name you wish: ``upstream`` is just a
  common label for the main repository.

  Note that the remote from which you cloned the repository is named ``origin``
  by default (here: your fork). A local ``master`` branch is automatically
  checked out from the origin after the clone. You can list all branches with
  ``git branch -a``.

You repeat the following steps until your contribution is finished. Only then
can your contributions be added main repository through a `pull request
<https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests>`_
(PR).

* ... edit some files ...
* Check changes: ``git status`` and/or ``git diff``
* Stage updated files for commit: |br|
  ``git add -u`` or add new files ``git add <list of files>``
* Commit changes: ``git commit`` (opens up editor for commit message)
* Enter a meaningful commit message. First line is a overall summary. Then, if
  necessary, skip one line and add a more detailed description form the third
  line on.
* Synchronize with the changes from the main repository/upstream:

  - Fetch new changes: |br|
    ``git fetch upstream``
  - Re-apply your current branch commits to the head of the ``upstream`` master
    branch: |br|
    ``git rebase -i upstream/master``
  - At this point, conflicts between your changes and those from the main
    ``upstream`` repository may occur. If no conflicts appeared, then you are
    finished and you can continue coding or push your work onto you fork.
    Otherwise repeat these steps until you're done (you can abort the whole
    rebase process via ``git rebase --abort``):

    + Review the conflicts (`VS Code <https://code.visualstudio.com/>`_ is a
      great tool for this)
    + Mark them as resolved ``git add <filename>``
    + Continue the rebase ``git rebase --continue``
* Push your changes to your fork: |br|
  ``git push origin <branchname>`` |br|
  This step 'synchronizes' your local branch and the branch in your fork. It is
  not required after every commit, but it is certainly necessary once you are
  ready to merge your code into ``upstream``.

.. tip::
  Remember to commit frequently instead of submitting a PR of just one commit.
  Making frequent snapshots (commits) of your work is safer workflow in
  general. Later on, rebasing can help you to group and alter commit messages,
  so don't worry.

.. tip::
  It can be useful to push your local branch to your fork under a different
  name using: |br|
  ``git push origin <local-branchname>:<remote-branchname>``

Once you think your contribution is finished and can be merged into the main
repository:

* Make sure your the latest commits from the ``upstream/master`` are rebased
  onto your new branch and pushed to your fork
* Log into GitHub with your account and create a PR. This is a request to merge
  the changes in your fork branch with the ``master`` branch of the pycompwa or
  ComPWA repository.
* While the PR is open, commits pushed to the fork branch behind your PR will
  immediately appear in the PR.

Commit conventions
^^^^^^^^^^^^^^^^^^

* In the master branch, it should be possible to compile and test the framework
  **in each commit**. In your own topic branches, it is recommended to commit
  frequently (WIP keyword), but `squash those commits
  <https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History>`_
  to compilable commits upon submitting a merge request.
* Please use `conventional commit messages
  <https://www.conventionalcommits.org/>`_: start the commit subject line with
  a semantic keyword (see e.g. `Angular
  <https://github.com/angular/angular/blob/master/CONTRIBUTING.md#type>`_ or
  `these examples
  <https://seesparkbox.com/foundry/semantic_commit_messages>`_,
  followed by `a column <https://git-scm.com/docs/git-interpret-trailers>`_,
  then the message. The subject line should be in imperative mood—just imagine
  the commit to give a command to the code framework. So for instance:
  ``feat: add coverage report tools`` or ``fix: remove ...``. The message
  should be in present tense, but you can add whatever you want there (like
  hyperlinks for references).


Linear commit history
^^^^^^^^^^^^^^^^^^^^^

* Note on rebasing
* Note on squashing upon pull request
* Note on keeping branches topical
