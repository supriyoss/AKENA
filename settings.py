__tile__ = 'news'
__author__ = 'Supriyo Sarkar'
__license__ = 'JISCE'
__copyright__ = 'Copyright 2022, Supriyo Sarkar'

import logging
import os
import tempfile

from http.cookiejar import CookieJar as cj
from version import __version__

log = logging.getLogger(__name__)
PARENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
USER_AGENTS = os.path.join(PARENT_DIRECTORY, 'user_agents.txt')
STOPWORDS_DIR = os.path.join(PARENT_DIRECTORY, 'text')

NLP_STOPWORDS_EN = os.path.join(PARENT_DIRECTORY, 'resources/misc/stopwords-nlp-en.txt')

DATA_DIRECTORY = '.news_scraper'

TOP_DIRECTORY = os.path.join(tempfile.gettempdir(), DATA_DIRECTORY)

# Error log
LOGFILE = os.path.join(TOP_DIRECTORY, 'newspaper_errors_%s.log' % __version__)
MONITOR_LOGFILE = os.path.join(
    TOP_DIRECTORY, 'newspaper_monitors_%s.log' % __version__)

# Memo directory (same for all concur crawlers)
MEMO_FILE = 'memoized'
MEMO_DIR = os.path.join(TOP_DIRECTORY, MEMO_FILE)

# category and feed cache
CF_CACHE_DIRECTORY = 'feed_category_cache'
ANCHOR_DIRECTORY = os.path.join(TOP_DIRECTORY, CF_CACHE_DIRECTORY)

#TRENDING_URL = 'http://www.google.com/trends/hottrends/atom/feed?pn=p1'

for path in (TOP_DIRECTORY, MEMO_DIR, ANCHOR_DIRECTORY):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

