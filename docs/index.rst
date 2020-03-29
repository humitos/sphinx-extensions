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

* :doc:`sphinx-prompt`: directive to add unselectable prompt (``$``, ``>>>``, etc) in code blocks
* :doc:`sphinxemoji`: use emoji codes in your Sphinx documentation
* :doc:`sphinx-copybutton`: adds little "copy" button to the right of your code blocks
* :doc:`myst-parser`: powerful Markdown flavor for your Sphinx documentation without loosing the power of Sphinx itself
* :doc:`sphinxcontrib-httpdomain`: directives to document APIs in a very detailed way
* :doc:`sphinx-autobuild`: rebuild the documentation when a change is detected and reload the page to see the changes
* :doc:`sphinx-autoapi`: auto document your code API without executing the code itself (as ``sphinx.autodoc`` does)
* :doc:`nbsphinx`: render Jupyter Notebooks as documentation pages
* :doc:`sphinx-notfound-page`: renders a nice 404 page respecting all the look & feel of your documentation
* :doc:`sphinx-version-warning`: adds a warning banner at the top if reader is reading an old version of your documentation
* :doc:`sphinx-hoverxref`: adds tooltips on cross references of the documentation with the content of the linked section


Themes
------


* `sphinx-material`_: responsive Material Design theme
* `sphinx-rtd-theme`_: official Read the Docs theme
* `sphinx-typlog-theme`_: a sphinx theme designed by Typlog


.. _sphinx-material: https://bashtage.github.io/sphinx-material/index.html
.. _sphinx-rtd-theme: https://sphinx-rtd-theme.readthedocs.io/en/stable/
.. _sphinx-typlog-theme: https://sphinx-typlog-theme.readthedocs.io/en/latest/

.. tip::

   Each page have a "Show Source" link at the right navigation
   bar. You can click on it to see what you need to write in the
   source file to make it render as you see.



.. toctree::
   :glob:
   :hidden:

   *
