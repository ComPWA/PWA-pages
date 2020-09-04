Writing documentation
=====================

.. warning::
  These pages and are **under development**.

Sphinx
------

Some conventions:

* Reference rigorously! This not only allows the user to navigate easily
  through the website, but each link also forms a check that the text is
  consistent with the internal and external APIs and with the rest of the
  documentation.


reStructured Text
-----------------


Jupyter notebook
----------------

Jupyter notebooks aren't the most friendly with regard to Version Control
Systems like Git because in the back-end, a notebook is a JSON file that
changes for instances when you run a cell. There is no simple solution for this
other than to clean the cell output upon saving. You can automatize this with
`nbstripout <https://github.com/kynan/nbstripout>`_ if you have activated
``pre-commit`` (see :ref:`software/python:Python developer tools`).

Jupyter offers several other useful extensions that can be activate `like this
<https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html#enabling-disabling-extensions>`_
If you want to contribute to the example notebooks, make sure to check out the
following extensions:

* `jupyter-autopep8
  <https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/code_prettify/README_autopep8.html>`_
* `ruler
  <https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/ruler/readme.html>`_
* `spellchecker
  <https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/spellchecker/README.html>`_



Documentation
-------------
Generally try to code in such a way that it is self explanatory and its
documentation is not necessary. Of course this ideal case is not achieved in
reality, but avoid useless comments such as ``getValue() # gets value``. Also
try to comment only parts, which really need an explanation. Because keeping
the documentation in sync with the code is crucial, and is a lot of work.

The documentation is built with sphinx using the "read the docs" theme. For the
python code/modules ``sphinx-apidoc`` is used. The comment style is following
the ``doc8`` conventions.

You can build the documentation locally as follows. In your Conda environment,
navigate to the pycompwa repository, then do:

.. code-block:: shell

  cd doc
  conda install --file requirements.txt
  make html

Now, open the file ``doc/source/_build/html/index.html``.
