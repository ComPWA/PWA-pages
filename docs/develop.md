<!-- cSpell:ignore aquirdturtle docnb htmlcov ijmbarr labextension pylintrc -->
<!-- cSpell:ignore ryantam serverextension testenv -->

# Develop

[![GitPod](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ComPWA/PWA-pages)

If you have installed the {mod}`pwa_pages` in {ref}`install:Editable mode`, it
is easy to tweak the source code and try out new ideas immediately, because the
source code is considered the 'installation'.

````{admonition} Conda and VSCode
---
class: dropdown
---
The easiest way to , is by using
{ref}`Conda <install:Step 2: Create a virtual environment>` and
{ref}`develop:Visual Studio code`. In that case, the complete developer install
procedure becomes:

```bash
git clone https://github.com/ComPWA/PWA-pages.git
cd PWA-pages
conda env create
conda activate es
pip install -e .[dev]
code .  # open folder in VSCode
```
````

For more info, see {ref}`develop:Visual Studio code`.

## Automated style checks

When working on the source code of the {mod}`pwa_pages`, it is highly
recommended to install certain additional Python tools. Assuming you installed
the {mod}`pwa_pages` in {ref}`editable mode <install:Editable mode>`, these
additional tools can be installed into your
{ref}`virtual environment <install:Step 2: Create a virtual environment>` in
one go:

```bash
pip install -e .[dev]
```

Most of the tools that are installed with this command use specific
configuration files (e.g.
[pyproject.toml](https://github.com/ComPWA/PWA-pages/blob/master/pyproject.toml)
for [black](https://black.readthedocs.io),
[.pylintrc](https://github.com/ComPWA/PWA-pages/blob/master/.pylintrc) for
[pylint](http://pylint.pycqa.org), and
[tox.ini](https://github.com/ComPWA/PWA-pages/blob/master/tox.ini) for
[flake8](https://flake8.pycqa.org) and
[pydocstyle](http://www.pydocstyle.org)). These config files **define our
convention policies**, such as {pep}`8`. If you run into persistent linting
errors, this may mean we need to further specify our conventions. In that case,
it's best to create an issue and propose a policy change that can then be
formulated in the config files.

````{tip}
---
class: dropdown
---
If you have Node.js (`npm`) on your system, you can run a few additional
checks. Install these packages as follows (possibly with administrator rights):

```bash
npm install -g cspell markdownlint-cli pyright
```
````

Normally, these packages are only run in the
{ref}`CI <develop:Continuous Integration>`, but if you have them installed,
they are also run when you run {ref}`tox <develop:Testing>` (local CI).

Note that `pyright` requires Node.js v12.x (see install instructions
[here](https://nodejs.org/en/download/package-manager)).

## Pre-commit

All **style checks** are enforced through a tool called
[pre-commit](https://pre-commit.com). This tool needs to be activated, but only
once, after you clone the repository:

```bash
pre-commit install
```

Upon committing, `pre-commit` now runs a set of checks as defined in the file
[.pre-commit-config.yaml](https://github.com/ComPWA/PWA-pages/blob/master/.pre-commit-config.yaml)
over all staged files. You can also quickly run all checks over _all_ indexed
files in the repository with the command:

```bash
pre-commit run -a
```

This command is also run on GitHub actions whenever you submit a pull request,
ensuring that all files in the repository follow the conventions set in the
config files of these tools.

## Documentation

The documentation that you find on [pwa.rtfd.io](http://pwa.rtfd.io) are built
from the
[documentation source code folder](https://github.com/ComPWA/PWA-pages/tree/master/docs)
(`docs`) with [Sphinx](https://www.sphinx-doc.org). Sphinx also
[builds the API](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)
and therefore checks whether the
[docstrings](https://www.python.org/dev/peps/pep-0257) in the Python source
code are valid and correctly interlinked.

You can quickly build the documentation from the root directory of this
repository with the command:

```bash
tox -e doc
```

Alternatively, you can run `sphinx-build` yourself as follows:

```bash
cd docs make html # or EXECUTE_NB= make html
```

A nice feature of [Read the Docs](https://readthedocs.org), where we host our
documentation, is that documentation is built for each pull request as well.
This means that you can view the documentation for your changes as well. For
more info, see
[here](https://docs.readthedocs.io/en/stable/guides/autobuild-docs-for-pull-requests.html),
or just click "details" under the RTD check once you submit your PR.

We make use of [Markedly Structured Text](https://myst-parser.readthedocs.io)
(MyST), so you can write the documentation in either
[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
or [Markdown](https://www.markdownguide.org). In addition, it's easy to write
(interactive) code examples in Jupyter notebooks and host them on the website,
(see [MyST-NB](https://myst-nb.readthedocs.io))!

## Jupyter Notebooks

````{margin}
```{tip}
Sometimes it happens that your Jupyter installation does not recognize
your {ref}`virtual environment <install:Step 2: Create a virtual environment>`.
In that case, have a look at
[these instructions](https://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments)
```
````

The [docs](https://github.com/ComPWA/PWA-pages/tree/master/docs) folder
contains a few Jupyter notebooks. These notebooks are run and tested whenever
you make a {ref}`pull request <develop:Git and GitHub>`. If you want to improve
those notebooks, we recommend working with
[Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable), which is installed
with the `dev` requirements of the {mod}`pwa_pages`. Jupyter Lab offers a nicer
developer experience than the default Jupyter notebook editor does. In
addition, we recommend to install a few extensions:

```bash
jupyter labextension install jupyterlab-execute-time jupyter labextension
install @ijmbarr/jupyterlab_spellchecker jupyter labextension install
@aquirdturtle/collapsible_headings jupyter labextension install
@ryantam626/jupyterlab_code_formatter jupyter labextension install
@jupyter-widgets/jupyterlab-manager

jupyter serverextension enable --py jupyterlab_code_formatter
```

Now, if you want to test all notebooks documentation folder and check how they
will look like in the {ref}`develop:Documentation`, you can do this with:

```bash
tox -e docnb
```

This command takes more time than `tox -e doc`, but it is good practice to do
this before you submit a pull request.

## Spelling

Throughout this repository, we follow American English
([en-us](https://www.andiamo.co.uk/resources/iso-language-codes)) spelling
conventions. As a tool, we use
[cSpell](https://github.com/streetsidesoftware/cspell/blob/master/packages/cspell/README.md),
because it allows to check variable names in camel case and snake case. This
way, a spelling checker helps you in avoid mistakes in the code as well!

Accepted words are tracked through the {file}`cspell.json` file. As with the
other config files, {file}`cspell.json` formulates our conventions with regard
to spelling and can be continuously updated while our code base develops. In
the file, the `words` section lists words that you want to see as suggested
corrections, while `ignoreWords` are just the words that won't be flagged. Try
to be sparse in adding words: if some word is just specific to one file, you
can [ignore it inline](https://www.npmjs.com/package/cspell#ignore), or you can
add the file to the `ignorePaths` section if you want to ignore it completely.

It is easiest to use cSpell in {ref}`develop:Visual Studio Code`, through the
[Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
extension: it provides linting, suggests corrections from the {code}`words`
section, and enables you to quickly add or ignore words through the
{file}`cspell.json` file. Alternatively, you can
[run cSpell](https://www.npmjs.com/package/cspell#installation) on the entire
code base (with {code}`cspell $(git ls-files)`), but for that your system
requires [npm](https://www.npmjs.com).

## Git and GitHub

The {mod}`pwa_pages` source code is maintained with Git and published through
GitHub. We keep track of issues with the code, documentation, and developer
set-up with GitHub issues (see overview
[here](https://github.com/ComPWA/PWA-pages/issues)). This is also the place
where you can
[report bugs](https://github.com/ComPWA/PWA-pages/issues/new/choose).

### Issue management

We keep track of issue dependencies, time estimates, planning, pipeline
statuses, et cetera with [ZenHub](https://app.zenhub.com). You can use your
GitHub account to log in there and automatically get access to the
{mod}`pwa_pages` issue board once you are part of the
[ComPWA organization](https://github.com/ComPWA).

Publicly available are:

- [Issue labels](https://github.com/ComPWA/PWA-pages/labels): help to
  categorize issues by type (maintenance, enhancement, bug, etc.).

- [Milestones](https://github.com/ComPWA/PWA-pages/milestones?direction=asc&sort=title&state=open):
  way to bundle issues for upcoming releases.

### Commit conventions

- Please use
  [conventional commit messages](https://www.conventionalcommits.org): start
  the commit with a semantic keyword (see e.g.
  [Angular](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#type)
  or
  [these examples](https://seesparkbox.com/foundry/semantic_commit_messages),
  followed by [a column](https://git-scm.com/docs/git-interpret-trailers), then
  the message. The message itself should be in imperative mood — just imagine
  the commit to give a command to the code framework. So for instance:
  {code}`feat: add coverage report tools` or {code}`fix: remove ...`.

- Keep pull requests small. If the issue you try to address is too big, discuss
  in the team whether the issue can be converted into an
  [Epic](https://blog.zenhub.com/working-with-epics-in-github) and split up
  into smaller tasks.

- Before creating a pull request, run `tox`. See also {ref}`develop:Testing`.

- Also use a [conventional commit message](https://www.conventionalcommits.org)
  style for the PR title. This is because we follow a
  [linear commit history](https://docs.github.com/en/github/administering-a-repository/requiring-a-linear-commit-history)
  and the PR title will become the eventual commit message. Note that a
  conventional commit message style is
  [enforced through GitHub Actions](https://github.com/ComPWA/PWA-pages/actions?query=workflow%3A%22PR+linting%22),
  as well as {ref}`PR labels <develop:Issue management>`.

- PRs can only be merged through 'squash and merge'. There, you will see a
  summary based on the separate commits that constitute this PR. Leave the
  relevant commits in as bullet points. See the
  [commit history](https://github.com/ComPWA/PWA-pages/commits/master) for
  examples. This comes in especially handy when
  {ref}`drafting a release <develop:Milestones and releases>`!

### Milestones and releases

An overview of the {mod}`pwa_pages` releases can be found on the
[release page](https://github.com/ComPWA/PWA-pages/releases).

Release notes are automatically generated from the PRs that were merged into
the master branch since the previous tag (see
[latest draft](https://github.com/ComPWA/PWA-pages/releases)). The changelog
there is generated from the PR titles and categorized by issue label. New
releases are automatically published to PyPI when a new tag with such release
notes is created (see
[setuptools-scm](https://pypi.org/project/setuptools-scm)).

### Continuous Integration

All {ref}`style checks <develop:Automated style checks>`, testing of the
{ref}`documentation and links <develop:Documentation>`, and
{ref}`unit tests <develop:Testing>` are performed upon each pull request
through [GitHub Actions](https://docs.github.com/en/actions) (see status
overview [here](https://github.com/ComPWA/PWA-pages/actions)). All checks
performed for each PR have to pass before the PR can be merged.

## Visual Studio code

We recommend using [Visual Studio Code](https://code.visualstudio.com) as it's
free, regularly updated, and very flexible through it's wide offer of user
extensions.

If you add or open this repository as a
[VSCode workspace](https://code.visualstudio.com/docs/editor/multi-root-workspaces),
the file
[.vscode/settings.json](https://github.com/ComPWA/PWA-pages/blob/master/.vscode/settings.json)
will ensure that you have the right developer settings for this repository. In
addition, VSCode will automatically recommend you to install a number of
extensions that we use when working on this code base
[they are defined](https://code.visualstudio.com/updates/v1_6#_workspace-extension-recommendations)
in the
[.vscode/extensions.json](https://github.com/ComPWA/PWA-pages/blob/master/.vscode/extensions.json)
file).

You can still specify your own settings in
[either the user or encompassing workspace settings](https://code.visualstudio.com/docs/getstarted/settings),
as the VSCode settings that come with this are folder settings.
