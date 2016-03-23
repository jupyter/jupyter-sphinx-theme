# jupyter-sphinx-theme
A Jupyter [Sphinx](http://www.sphinx-doc.org/en/stable/) theme for narrative
documentation.

## Installation
Install the package using PIP:

```bash
pip install jupyter_sphinx_theme
```

Edit the "conf.py" configuration file to point to the bootstrap theme:

```python
# At the top.
import jupyter_sphinx_theme

# ...

# Activate the theme.
html_theme = 'bootstrap'
html_theme_path = jupyter_sphinx_theme.get_html_theme_path()
```
