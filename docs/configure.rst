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
