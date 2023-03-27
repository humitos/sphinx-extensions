sphinx-autobuild
================

:Homepage:
  https://github.com/executablebooks/sphinx-autobuild


``sphinx-autobuild`` is a useful extension to use while we are writing our documentation and we want to see how it looks like immediately after making any change.

Once executed, it will watch the source files and trigger a re-build of our documentation when a file changes. Besides, it will refresh the page of our browser to render the new changes.


Installation
------------

.. prompt:: bash

   pip install sphinx-autobuild


Usage
-----

Run this command in your terminal,

.. prompt:: bash

   sphinx-autobuild docs docs/_build/html


* ``docs`` is the directory of your source documentation
* ``docs/_build/html`` is the directory where the output will be written


Then, access http://127.0.0.1:8000/ with your browser.
