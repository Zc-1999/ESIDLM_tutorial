import os
import sys
from datetime import datetime
import sphinx_theme

# add system
sys.path.insert(0, os.path.abspath('D:/project_esidlm_tutorial/esidlm/learner/'))

# -- Project information -----------
project = 'ESIDLM'
copyright = f"{datetime.now().year}"
author = 'BNU'

release = '0.1.0'

htmlhelp_basename = "BNU_ESIDLM"

extensions = [
    "sphinx_copybutton",
    "sphinx_panels",
    "sphinx_design",
    "sphinx_toggleprompt",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    'sphinxcontrib.images', 
    'sphinx.ext.viewcode',
    "nbsphinx",
]

pygments_style = "sphinx"

html_theme = 'pydata_sphinx_theme'

html_static_path = ["_static"]

html_title = f"ESIDLM {release}"

html_css_files = [
    'custom.css',
    'custom1.css'
]
html_sourcelink_suffix = ""

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
}
templates_path = ['_templates']

language = 'en_US'

exclude_patterns = []

html_theme_options = {
    "external_links": [],
    "github_url": "https://github.com/RegiusQuant/ESIDLM",
    "secondary_sidebar_items": ["page-toc.html"],
}

def setup(app):
    app.add_css_file('_static/custom.css')
    app.add_css_file('_static/custom1.css')


