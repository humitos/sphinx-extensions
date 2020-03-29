Welcome to sphinx-extensions' documentation!
============================================

This is a curated and *opinionated* list of Sphinx_ extensions that I
found useful while working with different Sphinx documentation
projects. All the extension listed here have their own page **showing
a working live example** and it's minimum configuration to make it
work in your docs.

.. _Sphinx: https://www.sphinx-doc.org/

.. note::

   Sphinx already has a list of `Built-in extensions`_ that are really
   useful. Besides, there is also a list of `Third-party extensions`_
   in that page but unfortunately, it's a bit out of date.

.. _Built-in extensions: https://www.sphinx-doc.org/en/master/usage/extensions/index.html#builtin-sphinx-extensions
.. _Third-party extensions: https://www.sphinx-doc.org/en/master/usage/extensions/index.html#third-party-extensions


Extensions
----------

* :doc:`sphinx-prompt`

  * Homepage: https://github.com/sbrunner/sphinx-prompt/
  * Description: directive to add unselectable prompt (``$``, ``>>>``, etc)

* :doc:`sphinxemoji`

  * Homepage: https://github.com/sphinx-contrib/emojicodes/
  * Description: use emoji codes in your Sphinx documentation

* :doc:`sphinx-copybutton`

  * Homepage: https://sphinx-copybutton.readthedocs.io/en/latest/
  * Description: adds little "copy" button to the right of your code blocks

* :doc:`myst-parser`

  * Homepage: https://myst-parser.readthedocs.io/en/latest/index.html
  * Description: powerful Markdown flavor for your Sphinx documentation without loosing the power of Sphinx itself

* :doc:`sphinxcontrib-httpdomain`

  * Homepage: https://sphinxcontrib-httpdomain.readthedocs.io/en/stable/
  * Description: directives to document APIs in a very detailed way

* :doc:`sphinx-autobuild`

  * Homepage: https://github.com/GaretJax/sphinx-autobuild
  * Description: watch a directory and rebuild the documentation when a change is detected and reload the page to see the changes

* :doc:`sphinx-autoapi`

  * Homepage: https://sphinx-autoapi.readthedocs.io/en/latest/
  * Description: auto document your code API without executing the code itself (as ``sphinx.autodoc`` does)

* :doc:`nbsphinx`

  * Homepage: https://nbsphinx.readthedocs.io/en/latest/
  * Description: render Jupyter Notebooks as documentation pages

* :doc:`sphinx-notfound-page`

  * Homepage: https://sphinx-notfound-page.readthedocs.io/en/latest/
  * Description: renders a nice 404 page respecting all the look & feel of your documentation

* :doc:`sphinx-version-warning`

  * Homepage: https://sphinx-version-warning.readthedocs.io/en/latest/
  * Description: adds a warning banner at the top if reader is reading an old version of your documentation

* :doc:`sphinx-hoverxref`

  * Homepage: https://sphinx-hoverxref.readthedocs.io/
  * Description: adds tooltips on cross references of the documentation with the content of the linked section


Themes
------

* :doc:`sphinx-material`

  * Homepage: https://bashtage.github.io/sphinx-material/index.html
  * Description: responsive Material Design theme

* :doc:`sphinx-rtd-theme`

  * Homepage: https://sphinx-rtd-theme.readthedocs.io/en/stable/
  * Description: official Read the Docs theme

* :doc:`sphinx-typlog-theme`

  * Homepage: https://sphinx-typlog-theme.readthedocs.io/en/latest/
  * Description: a sphinx theme designed by Typlog


.. tip::

   Each page have a "Show Source" link at the right navigation
   bar. You can click on it to see what you need to write in the
   source file to make it render as you see.



.. toctree::
   :glob:
   :hidden:

   *
