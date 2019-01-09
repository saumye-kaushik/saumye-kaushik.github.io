#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Saumye Kaushik'
SITENAME = "Saumye's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

THEME= 'themes/flex'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/saumye-kaushik/'),
          ('Github', 'https://github.com/saumye-kaushik'),)
		  
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True