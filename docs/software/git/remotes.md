# Working together: remotes

Now that we have seen
{doc}`how Git records changes as a stream of 'commits' <commit>` and
{doc}`how you can use branches and merging to streamline those commits <branching>`,
we can explore how to distribute our workflow over a team. For illustration, we
use a [fork](https://guides.github.com/activities/forking/) of the
[ComPWA source code](https://github.com/ComPWA/ComPWA) as a sample repository.

:::{note}

You will need to [create a GitHub account](https://github.com/join) first. It
is also highly recommended to
[set up GitHub with an SSH key](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).
In the following, we assume that `$ACCOUNT` is your GitHub username.

:::

First, [fork the ComPWA repository](https://github.com/ComPWA/ComPWA/fork), so
that you have a copy of that repository under your own user account. To get a
copy of that repository locally, run:

```shell
git clone git@github.com:$ACCOUNT/ComPWA.git
cd ComPWA
git branch -vv
```

The last command shows you that you are automatically checked out to the
`master` branch. It also shows `origin/master`. This is because the
{command}`git clone` command added a
[remote](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes) named
`origin` to your local Git repository pointing to your the SSH address of your
ComPWA fork.

```shell
git remote -v
```

A remote is just a _protected_ collection of branches that mirror the state of
the remote repository. You can see all these branches, both remote and local,
with:

```shell
git branch -a
```

The remote branches are protected in the sense that you can only update them by
[fetching (downloading) and pushing (uploading)](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes#_fetching_and_pulling).
For the rest, you only have 'read access', meaning for instance that you can
only
[merge](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
or [rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) them onto
local branches. If you checkout a remote branch, Git therefore only creates a
local copy of that remote branch.

You can add an arbitrary number of remotes. In a team project, it's common to
have one main repository (here
[github.com/CompWA/ComPWA](https://github.com/ComPWA/ComPWA)) that you add as a
remote named `upstream`:
