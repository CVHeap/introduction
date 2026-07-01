#!/usr/bin/env python3
'''
Basic introduction to the product being built.

Build Dependencies: python3-sphinx python3-pydata-sphinx-theme
'''

# Project Options
project = 'CV Heap'
author = 'Michael Lustfield'
copyright = '2026, Michael Lustfield. All rights reserved.'
exclude_patterns = ['README.rst']

# HTML Output
# https://pydata-sphinx-theme.readthedocs.io/
html_title = project
html_theme = 'pydata_sphinx_theme'
html_show_sourcelink = False
html_show_sphinx = False
html_theme_options = {
        'footer_end': [],
        'search_bar_text': 'Search this site...',
}
