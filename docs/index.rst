Welcome to sphinx-extensions' documentation!
============================================

This is a curated and *opinionated* list of Sphinx_ extensions that I
found useful while working with different Sphinx documentation projects.
All the extension listed here have their own page **showing a working live example**
and its minimum configuration to make it work in your docs.

.. _Sphinx: https://www.sphinx-doc.org/


Extensions
----------

.. How-To create the ``img-top``

   1. Capture a screenshot
   2. Crop to 300x
   3. Add a red arrow of 2px width
   4. Save it in PNG with 7 as compression level

.. grid:: 1 2 3 3

   .. grid-item-card:: sphinx-prompt
      :img-top: _static/sphinx-prompt.gif
      :link: sphinx-prompt
      :link-type: doc
      :padding: 1

      Sphinx directive (``.. prompt::``) to add unselectable prompt (``$``, ``>>>``, etc) in code blocks.

   .. grid-item-card:: sphinxemoji
      :img-top: _static/sphinxemoji.png
      :link: sphinxemoji
      :link-type: doc
      :padding: 1

      Use emoji codes in your Sphinx documentation.

   .. grid-item-card:: sphinx-copybutton
      :img-top: _static/sphinx-copybutton.png
      :link: sphinx-copybutton
      :link-type: doc
      :padding: 1

      Adds a little "Copy" button to the top-right of your code blocks.

   .. grid-item-card:: sphinx-favicon
      :img-top: _static/sphinx-favicon.png
      :link: sphinx-favicon
      :link-type: doc
      :padding: 1

      Adds custom favicons to your Sphinx documentation.

   .. grid-item-card:: myst-parser
      :img-top: _static/myst-parser.png
      :link: myst-parser
      :link-type: doc
      :padding: 1

      Powerful Markdown flavor for your Sphinx documentation without loosing the power of Sphinx itself.

   .. grid-item-card:: sphinxcontrib-httpdomain
      :img-top: _static/sphinxcontrib-httpdomain.png
      :link: sphinxcontrib-httpdomain
      :link-type: doc
      :padding: 1

      Adds new Sphinx directives to document APIs in a very detailed way.

   .. grid-item-card:: sphinx-autobuild
      :img-top: _static/sphinx-autobuild.png
      :link: sphinx-autobuild
      :link-type: doc
      :padding: 1

      Rebuilds the documentation when a change is detected and reload the page to see the changes.

   .. grid-item-card:: sphinx-autoapi
      :img-top: _static/sphinx-autoapi.png
      :link: sphinx-autoapi
      :link-type: doc
      :padding: 1

      Auto documents your API code without executing the code itself (as ``sphinx.autodoc`` does).

   .. grid-item-card:: nbsphinx
      :img-top: _static/nbsphinx.png
      :link: nbsphinx
      :link-type: doc
      :padding: 1

      Renders Jupyter Notebooks as documentation pages.

   .. grid-item-card:: sphinx-notfound-page
      :img-top: _static/sphinx-notfound-page.png
      :link: https://sphinx-notfound-page.readthedocs.io/
      :padding: 1

      Renders nice 404 pages respecting all the look & feel of your documentation.

   .. grid-item-card:: sphinx-version-warning
      :img-top: _static/sphinx-version-warning.png
      :link: http://sphinx-version-warning.readthedocs.io/
      :padding: 1

      Adds a warning banner at the top if the reader is reading an old version of your documentation.

   .. grid-item-card:: sphinx-hoverxref
      :img-top: _static/sphinx-hoverxref.png
      :link: https://sphinx-hoverxref.readthedocs.io/
      :padding: 1

      Adds tooltips on cross references of the documentation with the content of the linked section.

   .. grid-item-card:: sphinx-last-updated-by-git
      :img-top: _static/sphinx-last-updated-by-git.png
      :link: https://github.com/mgeier/sphinx-last-updated-by-git
      :padding: 1

      Adds the "last updated" date at the bottom of each documentation page (obtained from the Git commit date).
      
   .. grid-item-card:: sphinxext-opengraph
      :img-top: _static/sphinxext-opengraph.png
      :link: https://github.com/wpilibsuite/sphinxext-opengraph
      :padding: 1

      Generates Open Graph metadata ✨ for each page of your documentation.
      
      


Themes
------


Visit https://sphinx-themes.org/ for a full list of live themes!


.. tip::

   Each page have a "Show Source" link at the right navigation
   bar. You can click on it to see what you need to write in the
   source file to make it render as you see.



.. toctree::
   :glob:
   :hidden:

   *

.. seealso::

   Sphinx already has a list of `Built-in extensions`_ that are really useful.
   Besides, there is also a list of `Third-party extensions`_ in that page but unfortunately,
   it's a bit out of date.

   .. _Built-in extensions: https://www.sphinx-doc.org/en/master/usage/extensions/index.html#builtin-sphinx-extensions
   .. _Third-party extensions: https://www.sphinx-doc.org/en/master/usage/extensions/index.html#third-party-extensions

   Besides the official documentation, there is an `Awesome Sphinx`_ site that automatically collects Sphinx extensions
   and let you search them by types and tags.

   .. _Awesome Sphinx: https://awesomesphinx.useblocks.com/
