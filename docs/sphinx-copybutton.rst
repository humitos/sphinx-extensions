sphinx-copybutton
=================

``sphinx-copybutton`` adds a small "copy" button at the right of all
``.. code-block::`` directives [#]_, allowing the reader to copy all its
content into the clipboard with just one click.

It has some useful options to customize, like copying only lines that
does not contains prompt, among others.



Example
-------

.. code-block::

   Click in the right icon to copy this text!


Installation
------------

.. prompt:: bash

   pip install sphinx-copybutton


Configuration
-------------

.. code-block:: python

   # conf.py
   extensions = [
       '...',
       'sphinx_copybutton',
   ]


.. [#] it works nicely with ``.. prompt::`` as well (``sphinx-prompt``)
