sphinx-favicon
==============

:Homepage:
   https://github.com/tcmetzger/sphinx-favicon

:Documentation:
   https://sphinx-favicon.readthedocs.io/en/latest/

With ``sphinx-favicon``, you can add custom favicons to your Sphinx html
documentation quickly and easily.

You can define favicons directly in ``conf.py``, with different ``rel``
attributes such as `icon <https://html.spec.whatwg.org/multipage/links.html#rel-icon>`_
or `apple-touch-icon <https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html>`_
and any favicon size.

The ``sphinx-favicon`` extension gives you more flexibility than the `standard
favicon.ico supported by Sphinx
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon>`_.
It provides a quick and easy way to add the most important favicon formats for
different browsers and devices.

Example
-------

HTML code generated with ``sphinx-favicon``:

.. code-block:: HTML

   <link rel="icon" href="https://secure.example.com/favicon/favicon-16x16.png" sizes="16x16" type="image/png">
   <link rel="icon" href="https://secure.example.com/favicon/favicon-32x32.png" sizes="32x32" type="image/png">
   <link rel="apple-touch-icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">

Installation
------------

.. prompt:: bash

   pip install sphinx-favicon


Configuration
-------------

.. code-block:: python

   # conf.py
   extensions = [
       '...',
       'sphinx_favicon',
   ]

   favicons = [
      {
         "sizes": "16x16",
         "href": "https://secure.example.com/favicon/favicon-16x16.png",
      },
      {
         "sizes": "32x32",
         "href": "https://secure.example.com/favicon/favicon-32x32.png",
      },
      {
         "rel": "apple-touch-icon",
         "sizes": "180x180",
         "href": "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
      },
   ]

See `the project documentation <https://sphinx-favicon.readthedocs.io/en/latest/>`_
for more configuration options!
