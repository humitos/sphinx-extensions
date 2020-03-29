sphinxemoji
===========

``sphinxemoji`` allows you to easily add emojis in your documentation. It uses internal's Sphinx roles to make it possible.

You can find all the emoji codes available at https://sphinxemojicodes.readthedocs.io/en/stable/

Example
-------

This text includes a smily face |:smile:| and a snake too! |:snake:|

Don't you love it? |:heart_eyes:|


Installation
------------

.. prompt:: bash

   pip install sphinxemoji


Configuration
-------------

.. code-block:: python

   # conf.py
   extensions = [
       '...',
       'sphinxemoji.sphinxemoji',
   ]
