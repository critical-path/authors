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
