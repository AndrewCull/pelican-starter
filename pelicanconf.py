#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrew Cull'
SITENAME = u'Agema Corporation'
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ["theme/plugins"]
PLUGINS = ['assets', 'related-posts', 'optimize_images']
STATIC_PATHS = ['images', 'pdfs']

THEME = "theme"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Plugin Settings
# RELATED_POSTS_SKIP_SAME_CATEGORY = True

# Page Ordering
ARTICLE_ORDER_BY = 'reversed-date'
PAGE_ORDER_BY = 'page_order'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Build Settings
IGNORE_FILES = ['.#*','scss']
# Development Settings
LOAD_CONTENT_CACHE = False
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
