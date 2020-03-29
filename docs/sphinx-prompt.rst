sphinx-prompt
=============

:Homepage:
   https://github.com/sbrunner/sphinx-prompt/


``sphinx-prompt`` is useful to show commands outputs, Python REPL
scripts and more. It allows you to show a prompt on each line but
making it *unselectable*, so the reader can just copy and paste your
script without worry about modifying it to remove the prompt.


Example
-------

.. prompt:: python >>> auto

   >>> import datetime
   >>> datetime.now()
   >>> datetime.datetime.now()
   datetime.datetime(2020, 3, 29, 16, 13, 30, 100129)


Installation
------------

.. prompt:: bash

   pip install sphinx-prompt


Configuration
-------------

.. code-block:: python

   # conf.py
   extensions = [
       '...',
       'sphinx-prompt'
   ]
