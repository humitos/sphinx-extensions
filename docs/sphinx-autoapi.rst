sphinx-autoapi
==============

``sphinx-autoapi`` provides "autodoc" style documentation for multiple
programming languages without needing to load, run, or import the
project being documented.

In contrast to the traditional ``sphinx.ext.autodoc``, which is Python-only
and uses code imports, AutoAPI finds and generates documentation by
parsing source code.

Example
-------

.. note::

   This example shows the AutoAPI documentation of ``sphinx-notfound-page`` extension.

.. toctree::

    autoapi/index


Installation
------------

.. prompt:: bash

   pip install sphinx-autoapi


Configuration
-------------

.. code-block:: python

   # conf.py
   extensions = [
       '...',
       'autoapi.extension',
   ]

   autoapi_dirs = [
       'your-module/',
   ]
