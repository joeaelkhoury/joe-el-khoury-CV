#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://joeaelkhoury/Joe-el-khoury-CV.github.io/'
RELATIVE_URLS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
#RELATIVE_URLS = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Uncomment the following line to include Google Analytics
#GOOGLE_ANALYTICS = "UA-XXXXXXXX-X"

# Uncomment the following line to include Disqus comments
#DISQUS_SITENAME = "your-disqus-sitename"

# Uncomment the following lines if you want to enable social sharing
#TWITTER_USERNAME = "your-twitter-username"
#FACEBOOK_APPID = "your-facebook-app-id"

# Additional metadata to include in HTML output
SITE_DESCRIPTION = "Joe El Khoury - Data Scientist & MLOps Expert"
SITE_KEYWORDS = "data science, MLOps, AI, machine learning"

# Enable caching to speed up site generation
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True

# Plugins to use in production (make sure they're installed)
PLUGINS = [
    # Add any plugins you want to use in production
    # For example:
    # 'sitemap',
    # 'seo',
]

# Sitemap settings
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

# Enable caching to speed up site generation
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True

# Minify HTML
MINIFY_HTML = True