# jupyter-sphinx-theme
A Jupyter [Sphinx](http://www.sphinx-doc.org/en/stable/) theme for narrative
documentation.

## Installation
Install the package using PIP:

```bash
pip install jupyter_sphinx_theme
```

Edit the "conf.py" configuration file to point to the jupyter theme:

```python
# At the top.
from jupyter_sphinx_theme import *
init_theme()

# ...

# Comment out the `html_theme =` line
```
