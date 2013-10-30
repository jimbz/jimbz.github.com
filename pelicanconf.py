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

CONTACT = (
        ('Email', 'mailto:j.brauxin@gmail.com', 'send'),
        ('Google+', 'https://google.com/+JimBrauxZin', '//ssl.gstatic.com/images/icons/gplus-16.png'),
        ('LinkedIn', 'http://lnkd.in/2Ff7Ts', 'images/linkedin.png'),
        )

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
