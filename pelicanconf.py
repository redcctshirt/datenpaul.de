#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os  # for PATH - PELICAN_COMMENT_SYSTEM_DIR
PATH = os.getcwd()  # for PATH - PELICAN_COMMENT_SYSTEM_DIR

AUTHOR = u'heiko'
SITENAME = u'datenpaul'
SITEURL = 'https://www.datenpaul.de'

TIMEZONE = 'Europe/Berlin'

TAGLINE = 'Creative Commons Zeug und was mit Daten'

DEFAULT_LANG = u'de'

THEME = "./pelican-svbhack-master"

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['pelican_comment_system']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = 'feeds/%s.tag.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.tag.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
TRANSLATION_FEED_ATOM = None

# DISQUS_SITENAME = 'datenpaul'
PELICAN_COMMENT_SYSTEM = True
PELICAN_COMMENT_SYSTEM_IDENTICON_DATA = ('datenpaul',)

PELICAN_COMMENT_SYSTEM_DIR = PATH + "/comments"

# Blogroll
LINKS =  (('Projekte', 'projekte/'),
	  ('Flickr', 'http://www.flickr.com/photos/redcctshirt'),
          ('openclipart', 'http://www.openclipart.org/user-detail/redccshirt'),
          ('tumblr', 'http://redcctshirt.tumblr.com/'),
	  ('pixabay', 'http://www.pixabay.com/de/users/redcctshirt'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/redcctshirt'),
          ('github', 'https://github.com/redcctshirt'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
