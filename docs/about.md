# About

The PWA pages are maintained by the open-source
["Common Partial Wave Analysis"](https://github.com/ComPWA) organization on
GitHub. ComPWA aims to make Partial Wave Analysis accessible through
transparent and modern documentation, professional software development tools,
and collaboration-independent frameworks.

This page sets out some of the ideals of the ComPWA organization. For practical
details, see the [develop page](./develop.md).

## Long-term development

Partial Wave Analysis is a complicated research discipline, where several
aspects of quantum field theory, experimental physics, statistics, regression
analysis, and high-performance computing come together. This has led to
{ref}`a large number of PWA frameworks <software:Other PWA packages>` that
taylor to the need of each collaboration.

This state of affairs is only natural: research requires a flexible and
specialized approach. If, say, some background component shows up in an ongoing
analysis, one may need to implement some formalism that can handle it or add
some alignment parameters that were not yet supplied by the framework.

Disadvantages:

- Collaborations frequently start developing a new framework from scratch
- Development is slow because expertise is splintered
- It takes long to move beyond basic PWA formalisms
- Once developers leave, the framework collapses

ComPWA ideas to break this:

- Open source
- Developer experience before functionality
- Collaboration-independent
- Industry standards
- Modern documentation

**Note:** The first two points a crucial. ComPWA rather sacrifices
functionality for design and developer experience related developments. A lot
of other frameworks have started with the same ideal of having a good software
design etc, but soon begin to drop those ideals. We believe that only by
sticking to those ideals, a long term available and collaboration wide common
tool is possible.

The flexible branching model aims to make up for the functionality loss.

### Open source

- Uncommon approach: open source development for Partial Wave Analysis
- Make it _easy_ for anyone to contribute

### Developer Experience

- Easy to setup for developers
- Code modularity & transparency facilitates extension of the framework
- Facilitate using industry techniques and tools in software development for
  PWA

### Design

- Code modularity and transparency. For example separation of the
  `expertsystem` and `tensorwaves`. The former includes all of the physics and
  builds an amplitude model. `Tensorwaves` can use amplitude models and perform
  fits, but does not include any physics logic.
- Accommodate both stable development and flexibility for ongoing analyses

## User Experience

- Easy to install and use for analysis users

### Documentation

- Interlinked
- Emphasis on code examples
- Interactive (Jupyter notebooks)
- Modern (Executable Book Project)
