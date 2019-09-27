Testing authors
===============

To conduct testing, run the following commands from your shell.

.. code-block:: console

   [user@host authors]$ flake8 --count authors
   [user@host authors]$ pytest --cov --cov-report=term-missing

If any of the tests fail due to a `PermissionError`, then run the following command from your shell.

.. code-block:: console

   [user@host authors]$ sudo $(which pytest) --cov --cov-report=term-missing

On a final note, if you edit any of the existing templates, then be sure to make the corresponding changes to the unit tests.  Otherwise, they will fail.
