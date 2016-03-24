"""Sphinx Bootstrap Theme package."""
import os
from setuptools import setup, find_packages

from jupyter_sphinx_theme import __version__

###############################################################################
# Environment and Packages.
###############################################################################
# Don't copy Mac OS X resource forks on tar/gzip.
os.environ['COPYFILE_DISABLE'] = "true"

# Packages.
MOD_NAME = "jupyter_sphinx_theme"
PKGS = [x for x in find_packages() if x.split('.')[0] == MOD_NAME]


###############################################################################
# Helpers.
###############################################################################
def read_file(name):
    """Read file name (without extension) to string."""
    cur_path = os.path.dirname(__file__)
    exts = ('txt', 'rst', 'md')
    for ext in exts:
        path = os.path.join(cur_path, '.'.join((name, ext)))
        if os.path.exists(path):
            with open(path, 'rt') as file_obj:
                return file_obj.read()

    return ''


###############################################################################
# Setup.
###############################################################################
setup(
    name="jupyter-sphinx-theme",
    version=__version__,
    use_2to3=True,
    description="Jupyter Sphinx Theme.",
    long_description=read_file("README"),
    url="http://github.com/jupyter/sphinx-theme",

    author="Ryan Roemer, Project Jupyter, and contributors",
    author_email="jupyter@googlegroups.com",

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
    ],

    install_requires=[
        "setuptools",
    ],

    packages=PKGS,
    include_package_data=True,
)
