Package to create a single unique process based on changing its name using setproctitle.

- Installation using easy_install: $ sudo easy_install pyprocess

- using pip: $ sudo pip install pyprocess

- from source: $ python setup.py install.

- (or for develop): $ python setup.py develop.

Usage:

- from pyprocess.setProcess import setSingleProcess
- setSingleProcess("somename")

If all was ok, setSingleProcess will return True. 

license: http://www.opensource.org/licenses/bsd-license.php
