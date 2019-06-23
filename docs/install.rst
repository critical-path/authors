Installing authors
==================

authors is available on GitHub at https://github.com/critical-path/authors.

To install authors with test-related dependencies, run the following commands from your shell.

.. code-block:: console

    [user@host ~]$ git clone git@github.com:critical-path/authors.git
    [user@host ~]$ cd authors
    [user@host authors]$ sudo pip install --editable .[test]

To install it without test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install git+https://github.com/critical-path/authors.git

(If necessary, replace :code:`pip` with :code:`pip3`.)
