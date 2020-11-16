<!--
cSpell:ignore aquirdturtle autobuild docnb dotfiles htmlcov ijmbarr
cSpell:ignore labextension pylintrc ryantam serverextension testenv
-->

# Develop

[![GitPod](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ComPWA/PWA-pages)

This page describes some of the tools and conventions followed by the PWA pages
and by {ref}`affiliated PWA software projects <software:Sub-projects>`. Where
possible, we use the
[source code of the PWA-pages repository](https://github.com/ComPWA/PWA-pages)
as example, because its file structure is comparable to that of the others.

## Local set-up

### Virtual environment

When developing source code, it is safest to work within a
[virtual environment](https://realpython.com/python-virtual-environments-a-primer),
so that all package dependencies and developer tools are safely contained. This
is helpful in case something goes wrong with the dependencies: just trash the
environment and recreate it. In addition, you can easily install other versions
of the dependencies, without affecting other packages you may be working on.

Two common tools to manage virtual environments are Conda or Python's built-in
`venv`. In either case, you have to activate the environment whenever you want
to run the framework or use the developer tools.

````{tabbed} Conda environment
[Conda/Anaconda](https://www.anaconda.com) can be installed without
administrator rights, see instructions on
[this page](https://www.anaconda.com/distribution). In addition, Conda can
install more than just Python packages.

All projects {ref}`affiliated with the PWA pages <software:Sub-projects>`
provide a
[Conda environment file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
(see e.g.
[the one for the PWA-pages](https://github.com/ComPWA/PWA-pages/blob/master/environment.yml))
that defines the minimal dependencies to run the framework. To create an
environment specific for this package, simply navigate to the main folder of the
source code and run:

```bash
conda env create
```

Conda now creates an environment with a name that is defined in the
{file}`environment.yml` file. In addition, it will install the framework in
["editable" mode](#editable-installation), so that you can start developing
right away.
````

````{tabbed} Python venv
Alternatively, you can use
[Python's `venv`](https://docs.python.org/3/library/venv.html), if you have
that available on your system. Navigate to some convenient folder and run:

```bash
python3 -m venv ./venv
```

This creates a folder called {file}`venv` where all Python packages will be
contained. To activate the environment, run:

```bash
source ./venv/bin/activate
```

Now you can safely install the package you want to working on, as well as any
dependencies (see ["editable" mode](#editable-installation)):

```bash
pip install -e .
```
````

### Editable installation

It is most convenient to work on a package if you install the it in
["editable" mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs).
This allows you to tweak the source code and try out new ideas immediately,
because the source code is considered the 'installation'.

With `pip install`, a package can be installed in "editable" mode with the
[`--editable`](https://pip.pypa.io/en/stable/reference/pip_install/#install-editable)
flag. Simply
[clone](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#_git_cloning)
the repository you want to work on, navigate into it, and run:

```bash
python3 -m pip install -e .
```

````{toggle}
Internally, this just calls
```bash
python3 setup.py develop
```
````

This will install all required dependencies for the package as well.

### Optional dependencies

Packages can additionally define
[optional dependencies](https://setuptools.readthedocs.io/en/latest/userguide/dependency_management.html#optional-dependencies).
With `pip install` you can install these with
['extras' syntax](https://www.python.org/dev/peps/pep-0508/#extras) (e.g.
{command}`pip install -e .[dev]`). We follow the following structure to group
optional developer dependencies:

- {code}`doc` ― tools required to
  {ref}`build documentation <develop:Documentation>`
- {code}`format` ― tools that automate formatting, such as
  [black](https://black.readthedocs.io) and
  [isort](https://isort.readthedocs.io)
- {code}`lint` ― tools that point out bugs, typos, and other issues, such as
  [pylint](https://www.pylint.org)
- {code}`test` ― requirements for {ref}`runtime tests <develop:Testing>`
- {code}`dev` ― contains all of the above, as well as some other helpful tools
  like {ref}`Jupyter Lab <develop:Jupyter Notebooks>`.

All dependencies relevant for the developer that can be installed with:

```bash
pip install -e .[dev]
```

We explain some of those tools in the following sections.

````{dropdown} Node.js packages
If you have Node.js (`npm`) on your system, you can run a few additional
checks. Install these packages as follows (possibly with administrator rights):

```bash
npm install -g cspell markdownlint-cli pyright
```

Note that [`pyright`](https://github.com/microsoft/pyright) requires Node.js
v12.x (see install instructions
[here](https://nodejs.org/en/download/package-manager)).
````

### Updating

Whether installing extras or not, it may be that new commits in the repository
modify the dependencies. In that case, you have to rerun this command after
pulling new commits from the repository:

```bash
git checkout master
git pull
pip install -e .[dev]
```

If you still have problems, it may be that certain dependencies have become
redundant or conflicting. In that case, trash the virtual environment and
{ref}`create a new one <develop:Virtual environment>`.

## Developer tools

### Automated style checks

We try to define and enforce **our coding conventions** as much as possible
through automated tools instead of describing them in documentation. These
tools are configured through files such as
[pyproject.toml](https://github.com/ComPWA/PWA-pages/blob/master/pyproject.toml),
[.pylintrc](https://github.com/ComPWA/PWA-pages/blob/master/.pylintrc), and
[tox.ini](https://github.com/ComPWA/PWA-pages/blob/master/tox.ini). If you run
into persistent linting errors, this may mean we need to further specify our
conventions. In that case, it's best to
{ref}`create an issue <develop:Issue management>` and propose a policy change
that can then be formulated in those config files.

These tools perform their checks in the
{ref}`CI <develop:Continuous Integration>` when you make a
{ref}`pull request <develop:Git and GitHub>`, but you can run them locally as
well through {ref}`tox <develop:Testing>` (we call this 'local CI').
{ref}`develop:Pre-commit` performs certain style checks upon making a commit.

### Pre-commit

All **style checks** are enforced through a tool called
[pre-commit](https://pre-commit.com). This tool needs to be activated, but only
once, after you clone the repository:

```bash
pre-commit install
```

```{margin} Initializing pre-commit
The first time you run {command}`pre-commit` after installing or updating its
checks, it may take some time to initialize.
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

### Spelling

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

## Testing

````{margin} Profiling
To get an idea of performance per component, run

```bash
pytest --profile-svg
```
and check the stats and the {file}`prof/combined.svg` output file.
````

The fastest way to run all tests is with the command:

```bash
pytest -n auto
```

The flag {command}`-n auto` causes {code}`pytest` to
[run with a distributed strategy](https://pypi.org/project/pytest-xdist).

More thorough checks can be run in one go with the following command:

```{margin} Running jobs in parallel
The {code}`-p` flag lets the jobs run in parallel. It also provides a nicer
overview of the progress. See {ref}`tox:parallel_mode`.
```

```bash
tox -p
```

This command will run {code}`pytest`, build the documentation, and verify
cross-references in the documentation and the API. It's especially recommended
to **run tox before submitting a pull request!**

More specialized {code}`tox` tests are defined in the
[tox.ini](https://github.com/ComPWA/expertsystem/blob/master/tox.ini) config
file, under each {code}`testenv` section. You can list all environments, along
with a description of what they do, by running:

```bash
tox -av
```

````{margin}
```{tip}
In VScode, you can
visualize which lines in the code base are covered by tests with the
[Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters)
extension (for this you need to run {code}`pytest` with the flag
{code}`--cov-report=xml`).
```
````

Try to keep test coverage high. You can compute current coverage by running

```bash
tox -e cov
```

and opening {file}`htmlcov/index.html` in a browser.

```{dropdown} Organizing unit tests
When **unit** tests are well-organized, you avoid writing duplicate tests. In
addition, it allows you to check for coverage of specific parts of the code.

Therefore, when writing new tests, try to follow the module and class structure
of the package. For example, put unit tests that test the functions and methods
defined of some module called {code}`package.module` module into a test file called
{file}`test_module.py` that is directly placed under the
{file}`tests` folder. Similarly, bundle for a class {code}`SomeClass` under a
{code}`TestSomeClass` class in that file and test its methods (say,
{code}`SomeClass.my_method`) with `TestSomeClass.test_my_method`.

If possible, also try to order the tests by alphabetical order (that is, the
order of the {code}`import` statements).
```

## Documentation

The documentation that you find on [pwa.rtfd.io](http://pwa.rtfd.io) and its
sub-projects is built with [Sphinx](https://www.sphinx-doc.org). Sphinx also
[builds the API page](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)
of the packages and therefore checks whether the
[docstrings](https://www.python.org/dev/peps/pep-0257) in the Python source
code are valid and correctly interlinked.

You can quickly build the documentation from the root directory of any of the
repositories with the command:

```bash
tox -e doc
```

````{toggle}
Alternatively, you can run `sphinx-build` yourself as follows:

```bash
cd docs
make html
```
````

If you are doing a lot of work on the documentation,
[`sphinx-autobuild`](https://pypi.org/project/sphinx-autobuild) is a nice tool
to use. Just run:

```bash
sphinx-autobuild docs docs/_build/html --re-ignore="docs/api/.*" --open-browser
```

from the main directory. This will start a server
[http://127.0.0.1:8000](http://127.0.0.1:8000) where you can continuously
preview the changes you make to the documentation.

### Preview upon Pull Request

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

### Jupyter Notebooks

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
[Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable), which is
{ref}`installed with the dev requirements <develop:Optional dependencies>`.
Jupyter Lab offers a nicer developer experience than the default Jupyter
notebook editor does.

In addition, we recommend to install a few extensions:

```bash
jupyter labextension install jupyterlab-execute-time
jupyter labextension install @ijmbarr/jupyterlab_spellchecker
jupyter labextension install @aquirdturtle/collapsible_headings
jupyter labextension install @ryantam626/jupyterlab_code_formatter
jupyter labextension install @jupyter-widgets/jupyterlab-manager

jupyter serverextension enable --py jupyterlab_code_formatter
```

Now, if you want to test all notebooks in the documentation folder and check
what their output cells will look like in the {ref}`develop:Documentation`, you
can do this with:

```bash
tox -e docnb
```

This command takes more time than `tox -e doc`, but it is good practice to do
this before you submit a pull request.

## Git and GitHub

The source code of all related repositories is maintained with Git and
published through GitHub. We keep track of issues with the code, documentation,
and developer set-up with GitHub issues (see for instance
[here](https://github.com/ComPWA/PWA-pages/issues)). This is also the place
where you can
[report bugs](https://github.com/ComPWA/PWA-pages/issues/new/choose).

### Issue management

We keep track of issue dependencies, time estimates, planning, pipeline
statuses, et cetera with [ZenHub](https://app.zenhub.com). You can use your
GitHub account to log in there and automatically get access to the issue boards
of the packages once you are part of the
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
  [these examples](https://seesparkbox.com/foundry/semantic_commit_messages)),
  followed by [a column](https://git-scm.com/docs/git-interpret-trailers), then
  the message. The message itself should be in imperative mood — just imagine
  the commit to give a command to the code framework. So for instance:

  ```none
  ci: implement coverage report tools
  fix: fix typo in raised ValueError
  chore: remove redundant print statements
  docs!: rewrite welcome pages
  ```

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

Releases are managed with the
[GitHub release page](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/managing-releases-in-a-repository),
see for instance
[the one for the PWA pages](https://github.com/ComPWA/PWA-pages/releases).

Release notes are
[automatically generated from the PRs](https://github.com/release-drafter/release-drafter)
that were merged into the master branch since the previous tag. The changelog
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

## Code editors

### Visual Studio code

We recommend using [Visual Studio Code](https://code.visualstudio.com) as it's
free, regularly updated, and very flexible through it's wide offer of user
extensions.

If you add or open this repository as a
[VSCode workspace](https://code.visualstudio.com/docs/editor/multi-root-workspaces),
the file
[`.vscode/settings.json`](https://github.com/ComPWA/PWA-pages/blob/master/.vscode/settings.json)
will ensure that you have the right developer settings for this repository. In
addition, VSCode will automatically recommend you to install a number of
extensions that we use when working on this code base.
[They are defined](https://code.visualstudio.com/updates/v1_6#_workspace-extension-recommendations)
in the
[.vscode/extensions.json](https://github.com/ComPWA/PWA-pages/blob/master/.vscode/extensions.json)
file.

You can still specify your own settings in
[either the user or encompassing workspace settings](https://code.visualstudio.com/docs/getstarted/settings),
as the VSCode settings that come with this are folder settings.

````{dropdown} Conda and VSCode
Projects related to the PWA pages are best developed
{ref}`with Conda <develop:Virtual environment>` and VSCode. The complete
developer install procedure then becomes:

```bash
git clone https://github.com/ComPWA/PWA-pages.git  # or some other repo
cd PWA-pages
conda env create
conda activate pwa  # or whatever the name is
pip install -e .[dev]
code .  # open folder in VSCode
````
