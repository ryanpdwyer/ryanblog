#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ryan Dwyer'
SITENAME = u"Ryan's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

OUTPUT_RETENSION = (".hg", ".git", ".bzr")

THEME = "pelican-elegant"

PLUGIN_PATHS = ["pelican-plugins"]

PLUGINS = ['sitemap', 'extract_toc', 'tipue_search',
           'neighbors', 'render_math']

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives',
                    'search', '404'))

STATIC_PATHS = ['theme/images', 'images', 'files', 'notebooks',
                'pelican-plugins']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
