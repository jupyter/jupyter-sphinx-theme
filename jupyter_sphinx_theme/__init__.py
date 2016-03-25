"""Jupyter sphinx theme."""
import os
import subprocess
import sys
from recommonmark.parser import CommonMarkParser

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return [cur_dir]

def bash(fileName):
    """Runs a bash script in the local directory"""
    sys.stdout.flush()
    subprocess.call("bash {}".format(fileName), shell=True)

VERSION = (0, 0, 2)
__version__ = ".".join(str(v) for v in VERSION)
__version_full__ = __version__
theme_version = __version__

# Conf.py import settings
source_parsers = {
    '.md': CommonMarkParser,
}

html_theme = 'jupyter'
html_theme_path = get_html_theme_path()

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'nbsphinx'
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md', '.ipynb']

html_sidebars = {
    '**': [
        'sidebartoc.html'
    ]
}
