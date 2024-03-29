.. image:: https://travis-ci.com/critical-path/authors.svg?branch=master
   :target: https://travis-ci.com/critical-path/authors

.. image:: https://coveralls.io/repos/github/critical-path/authors/badge.svg?branch=master
   :target: https://coveralls.io/github/critical-path/authors?branch=master

.. image:: https://readthedocs.org/projects/authors/badge/?version=latest
   :target: https://authors.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Introduction
============

Thank the people who contribute to your Git/GitHub project by creating an AUTHORS file.

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

Using authors
=============

First, select a project whose contributors you want to thank and change to its working directory (the directory in which the :code:`.git` subdirectory resides).

.. code-block:: console

   [user@host ~]$ cd example-project

Then, run :code:`git` with the :code:`log` command and the :code:`--format` option, redirecting standard output to :code:`authors`.

.. code-block:: console

   [user@host example-project]$ git log --format=%an | authors

Finally, add and commit the newly-created :code:`AUTHORS` file.

.. code-block:: console

   [user@host example-project]$ git add AUTHORS
   [user@host example-project]$ git commit

Configuring authors
===================

To configure authors, create a file named :code:`.authors.yml` in your project's working directory.  :code:`.authors.yml` should be valid YAML and contain five key-value pairs.  

authors recognizes the following five keys.

- :code:`name`: The name of the output file generated by authors.
- :code:`kind`: The format of the output file, where :code:`adoc`, :code:`html`, :code:`md`, :code:`rst`, and :code:`txt` are valid values.
- :code:`heading`: The heading string.
- :code:`opening`: The opening string.
- :code:`closing`: The closing string.

If authors cannot find :code:`.authors.yml`, or if it detects any missing or invalid values, then it will use the following default values.

.. code-block:: yaml

   name: AUTHORS
   kind: md
   heading: Authors
   opening: Thank you to all of our contributors.
   closing: This project would not be possible without you.

Testing authors
===============

To conduct testing, run the following commands from your shell.

.. code-block:: console

   [user@host authors]$ flake8 --count authors
   [user@host authors]$ pytest --cov --cov-report=term-missing

If any of the tests fail due to a :code:`PermissionError`, then run the following command from your shell.

.. code-block:: console

   [user@host authors]$ sudo $(which pytest) --cov --cov-report=term-missing

On a final note, if you edit any of the existing templates, then be sure to make the corresponding changes to the unit tests.  Otherwise, they will fail.
