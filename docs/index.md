# PWA Software Pages

```{title} Welcome

```

[![GPLv3+ license](https://img.shields.io/badge/License-GPLv3+-blue.svg)](https://www.gnu.org/licenses/gpl-3.0-standalone.html)
[![Documentation build status](https://readthedocs.org/projects/pwa/badge/?version=latest)](https://pwa.readthedocs.io)
[![Spelling checked](https://img.shields.io/badge/cspell-checked-brightgreen.svg)](https://github.com/streetsidesoftware/cspell/tree/master/packages/cspell)

```{warning}
These pages and are **under development**.
```

The PWA Software Pages serve two purposes:

1. They aim to bring together the many Partial Wave Analysis frameworks out
   there on the market through interlinked documentation.

2. They provide a dynamic platform to collect and maintain knowledge on both
   PWA theory and software tools.

As such, the pages consist three main components: {doc}`theory <theory>`,
{doc}`analysis techniques <analysis>`, and {doc}`software <software>`. The
{doc}`theory pages <theory>` are to be a collection of the theoretical basis of
Partial Wave Analysis, along with references to more in-depth sources. This is
useful, because it is often difficult for newcomers to find their way around in
the growing amount of PWA literature and experimental results. The
{doc}`analysis section <analysis>` visits some of the common statistics
techniques that you need to be familiar with to do PWA (and event selection
more generally). The {doc}`software pages <software>` serve as a guide through
the available software tools that are relevant to PWA software development.

Finally, the {doc}`develop page <develop>` formulates some conventions and
tools that are used by
{ref}`affiliated software packages <software:Sub-projects>`.

## Table of Contents

```{toctree}
---
maxdepth: 2
---
theory
analysis
software
develop
about
API <api/pwa_pages>
```

- {ref}`Python API <modindex>`
- {ref}`General Index <genindex>`
- {ref}`Search <search>`

```{toctree}
---
caption: Related projects
hidden:
---
AmpForm <https://ampform.rtfd.io>
QRules <https://qrules.rtfd.io>
TensorWaves <https://tensorwaves.rtfd.io>
TF-PWA <https://tf-pwa.rtfd.io>
```
