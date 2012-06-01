pyprocess
=========

Package that includes a function to create a single unique process based on changing its name using setproctitle.

Install:
using easy_install:
- sudo easy_install pyprocess

using pip:
- pip install pyprocess

from source:
- python setup.py install.
(for Develop):
- python setup.py develop.

Usage:

- from pyprocess.setProcess import setSingleProcess
- setSingleProcess("somename")

If all was ok, setSingleProcess will return True. 

License: http://www.opensource.org/licenses/bsd-license.php
