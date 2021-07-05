# About

The PWA pages are maintained by the open-source
["Common Partial Wave Analysis"](https://github.com/ComPWA) organization on
GitHub. ComPWA aims to make Partial Wave Analysis accessible through
transparent and modern documentation, professional software development tools,
and collaboration-independent frameworks.

This page sets out some of the ideals of the ComPWA organization. For practical
details, see the {doc}`develop page <develop>`.

## Long-term development

Partial Wave Analysis is a complicated research discipline, where several
aspects of quantum field theory, experimental physics, statistics, regression
analysis, and high-performance computing come together. This has led to
{ref}`a large number of PWA frameworks <software:Other recommendations>` that
taylor to the need of each collaboration.

This state of affairs is only natural: research requires a flexible and
specialized approach. If, say, some background component shows up in an ongoing
analysis, one may need to implement some formalism that can handle it or add
some alignment parameters that were not yet supplied by the framework. It's
therefore hard to facilitate ongoing research while at the same time developing
a general, long-term PWA tool.

This state of affairs has a few major disadvantages:

- Collaborations usually start developing a PWA framework from scratch.
  Therefore, it takes years for packages to move offer more than the basic PWA
  formalisms.
- Development is slow because expertise is splintered: every group is working
  on their own package.
- Results become unreliable: the fewer people use a package, the more bugs will
  remain unnoticed.
- Once developers leave, the framework collapses. Sadly, this happens more
  often than not, as developers are usually scientists on short-term contracts.

ComPWA ideas to break this:

- Have everything {ref}`open source <about:Open source>`
- {ref}`Developer experience <about:Developer Experience>` before functionality
- Remain collaboration-independent and general in applicability
  ({ref}`about:Design`)
- Follow industry standards and tools (e.g. ticket system, CI, ADR, etc...)
- {ref}`Modern, interlinked documentation <about:Documentation>`

The first two points are crucial. ComPWA rather sacrifices functionality for
design and developer experience related developments. Many other frameworks
have started with the same ideal of having a good software design etc., but
soon begin to drop those ideals. We believe that only by sticking to those
ideals, it is possible to maintain a long-term and collaboration-wide common
tool.

### Open source

- Uncommon approach: open source development for Partial Wave Analysis
- Make it _easy_ for anyone to contribute

### Developer Experience

- Easy to setup for developers
- Code modularity & transparency facilitates extension of the framework
- Facilitate using industry techniques and tools in software development for
  PWA
- Record the decision making

### Design

- Code modularity and transparency. For example separation of the
  {mod}`expertsystem` and {mod}`tensorwaves`. The former includes all of the
  physics and builds an amplitude model. {mod}`tensorwaves` can use amplitude
  models and perform fits, but does not include any physics logic.
- Accommodate both stable development and flexibility for ongoing analyses
- Keep it simple by sticking to the core responsibility: construct amplitude
  models and fitting them to data

## User Experience

- Easy to install and use for analysis users
- Interlinked documentation
- Open-closed principle: give users the flexibility to for instance insert
  custom dynamics or use their own preferred plotting tools

### Documentation

- Interlinked
- Emphasis on code examples
- Interactive (Jupyter notebooks)
- Modern (Executable Book Project)
