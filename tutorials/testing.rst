Unit testing
------------

You also check the coverage of the unit tests:

.. code-block:: shell

  cd tests
  pytest

Now you can find a nice graphical overview of which parts of the code are not
covered by the tests by opening ``htmlcov/index.html``!

If you want to speed up the tests you can run ``pytest`` with the flag
``-m "not slow"``. Note, however, that in that case, the test coverage is not
reliable.


Continuous Integration (CI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The master branch is automatically build using TravisCI. Probably it is
interesting to check out the `log file
<https://travis-ci.com/ComPWA/pycompwa>`_ and the projects TravisCI
configuration file `travisCI.yml
<https://github.com/ComPWA/pycompwa/blob/master/.travis.yml>`_.

A code coverage report is generated for each pull request. Try to keep coverage
high by writing new tests if coverage decreases. You can see an overview
pycompwa's coverage `here <https://codecov.io/gh/ComPWA/pycompwa>`_. Under
`files <https://codecov.io/gh/ComPWA/pycompwa/tree/master/pycompwa>`_ you have
a detailed overview of coverage per module, and you can investigate coverage
all the way down to the source code.
