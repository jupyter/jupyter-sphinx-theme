"""Jupyter sphinx theme."""
import os
from recommonmark.parser import CommonMarkParser

VERSION = (0, 0, 1)

__version__ = ".".join(str(v) for v in VERSION)
__version_full__ = __version__
theme_version = __version__

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return [cur_dir]

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
