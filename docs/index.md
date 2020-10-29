# PWA Software Pages

```{title} Welcome

```

<!-- prettier:disable -->

```{eval-rst}
.. list-table::
  :widths: auto
  :align: left

  * - .. image:: https://img.shields.io/badge/License-GPLv3+-blue.svg
        :alt: GPLv3+ license
        :target: https://www.gnu.org/licenses/gpl-3.0-standalone.html
    - .. image:: https://readthedocs.org/projects/pwa/badge/?version=latest
        :alt: Documentation build status
        :target: https://pwa.readthedocs.io
```

<!-- prettier:enable -->

```{warning}
These pages and are **under development**.
```

The PWA Software Pages serve two purposes:

1. They aim to bring together the many Partial Wave Analysis frameworks out
   there on the market through interlinked documentation.

2. They provide a dynamic platform to collect and maintain knowledge on both
   PWA theory and software tools.

As such, the pages consist three main components: [theory](./theory.rst),
[analysis techniques](./analysis.rst), and [software](./software.rst). The
[theory pages](./theory.rst) are to be a collection of the basics of PWA
theory, along with references to more in-depth sources. This is useful, because
it is often difficult for newcomers to find their way around in the growing
amount of PWA literature and experimental results. The
[analysis section](./analysis.rst) visits some of the common statistics
techniques that you need to be familiar with to do PWA (and event selection
more generally). The [software pages](./software.rst) serve as a guide through
the available software tools that are relevant to PWA software development.

```{toctree}
---
maxdepth: 2
---
theory
analysis
software
develop
```

- {ref}`Python API <modindex>`

```{toctree}
---
hidden:
---
api
```

```{toctree}
---
caption: Related projects
hidden:
---
PWA Expert System <http://expertsystem.rtfd.io>
TensorWaves <http://tensorwaves.rtfd.io>
TF-PWA <http://tf-pwa.rtfd.io>
pycompwa <https://compwa.github.io>
```
