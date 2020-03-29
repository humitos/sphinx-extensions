sphinxemoji
===========

:Homepage:
  https://github.com/sphinx-contrib/emojicodes/

:Documentation:
   https://sphinxemojicodes.readthedocs.io/en/stable/


``sphinxemoji`` allows you to easily add emojis in your documentation. It uses internal's Sphinx roles to make it possible.


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
