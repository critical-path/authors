Installing authors
==================

authors is available on GitHub at https://github.com/critical-path/authors.

If you do not have pip version 18.1 or higher, then run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --upgrade pip

To install authors with test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --editable git+https://github.com/critical-path/authors.git#egg=authors[test]

To install it without test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install git+https://github.com/critical-path/authors.git

(If necessary, replace :code:`pip` with :code:`pip3`.)

