#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jim Braux-Zin'
SITENAME = u"Jim Braux-Zin's homepage"
SITESUBTITLE = u'Ph.D. candidate in Computer Vision'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = u'themes/jim/'

STATIC_PATHS = ['images', 'pdf', 'CNAME']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATH = 'plugins'
PLUGINS = ['pelican-bibtex', 'assets']
PUBLICATIONS_SRC = 'content/pubs.bib'

# Markdown options
MD_EXTENSIONS = (['extra', 'headerid'])

# Disable unneeded generation
DEFAULT_PAGINATION = False
AUTHORS_SAVE_AS = False
ARCHIVES_SAVE_AS = False
TAGS_SAVE_AS = False
ARTICLE_URL = '{category}.html#{slug}'
