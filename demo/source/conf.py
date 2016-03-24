# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
from jupyter_sphinx_theme import *

extensions = extensions + ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.ifconfig', 'sphinx.ext.viewcode']

templates_path = ['_templates']

master_doc = 'index'

project = u'Demo'
copyright = u'Ryan Roemer, Project Jupyter, and contributors'

version = theme_version
release = theme_version

exclude_patterns = []

pygments_style = 'sphinx'
todo_include_todos = True

html_theme_options = {
    'navbar_title': "Demo",
}
html_static_path = ["_static"]
htmlhelp_basename = 'MyProjectDoc'

latex_elements = { }

latex_documents = [
  ('index', 'MyProject.tex', u'My Project',
   u'Ryan Roemer', 'manual'),
]
man_pages = [
    ('index', 'myproject', u'My Project',
     [u'Ryan Roemer'], 1)
]
texinfo_documents = [
  ('index', 'MyProject', u'My Project',
   u'Ryan Roemer', 'MyProject', 'One line description of project.',
   'Miscellaneous'),
]
intersphinx_mapping = {'http://docs.python.org/': None}
