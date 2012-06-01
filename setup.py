import os
from setuptools import setup
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

files = ["pyprocess/*"]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyutils",
    version = "0.0.1",
    author = "Daniel Mondaca",
    author_email = "dnielm@gmail.com",
    description = ("process name managment."),
    license = "New Bsd License",
    keywords = "process name",
    url = "http://www.opensource.org/licenses/bsd-license.php",
    packages=['pyprocess'],
    install_requires = ['setproctitle'],
    long_description=read('README.txt'),
    package_data = {'package' : files },
    classifiers=[
        "Development Status :: 0 - Alpha",
        "Topic :: single process name",
        "License :: New Bsd License",
    ],
)
