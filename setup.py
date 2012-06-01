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
    name = "pyprocess",
    version = "0.0.1",
    author = "Daniel Mondaca",
    author_email = "dnielm@gmail.com",
    description = ("process name managment."),
    license = "Bsd",
    platforms = ['GNU/Linux'],
    keywords = "process name",
    url = "https://github.com/Nievous/pyprocess",
    packages=['pyprocess'],
    install_requires = ['setproctitle'],
    long_description=read('README.txt'),
    package_data = {'package' : files },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Software Development" 
    ],
)
