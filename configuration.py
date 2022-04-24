__tile__ = 'news'
__author__ = 'Supriyo Sarkar'
__license__ = 'JISCE'
__copyright__ = 'Copyright 2022, Supriyo Sarkar'

import logging

from parsers import Parser
from text import (StopWords, StopWordsHindi)
from version import __version__

log = logging.getLogger(__name__)


class Configuration(object):
    def __init__(self):
        """
        Modify any of these Article / Source properties
        TODO: Have a separate ArticleConfig and SourceConfig extend this!
        """
        self.MIN_WORD_COUNT = 300  # num of word tokens in text
        self.MIN_SENT_COUNT = 7  # num of sentence tokens
        self.MAX_TITLE = 200  # num of chars
        self.MAX_TEXT = 100000  # num of chars
        self.MAX_KEYWORDS = 35  # num of strings in list
        self.MAX_AUTHORS = 10  # num strings in list
        self.MAX_SUMMARY = 5000  # num of chars
        self.MAX_SUMMARY_SENT = 5  # num of sentences

        # max number of urls we cache for each news source
        self.MAX_FILE_MEMO = 20000

        # Cache and save articles run after run
        self.memoize_articles = True

        # Set this to false if you don't care about getting images
        self.fetch_images = True
        self.image_dimension_ration = 16 / 9.0

        # Follow meta refresh redirect when downloading
        self.follow_meta_refresh = False

        # Don't toggle this variable, done internally
        self.use_meta_language = True

        # You may keep the html of just the main article body
        self.keep_article_html = False

        # Fail for error responses (e.g. 404 page)
        self.http_success_only = True

        # English is the fallback
        self._language = 'en'

        # Unique stopword classes for oriental languages, don't toggle
        self.stopwords_class = StopWords

        self.browser_user_agent = 'newspaper/%s' % __version__
        self.headers = {}
        self.request_timeout = 7
        self.proxies = {}
        self.number_threads = 10

        self.verbose = False  # for debugging

        self.thread_timeout_seconds = 1
        self.ignored_content_types_defaults = {}
        # Set this to False if you want to recompute the categories
        # *every* time you build a `Source` object
        # TODO: Actually make this work
        # self.use_cached_categories = True

    def get_language(self):
        return self._language

    def del_language(self):
        raise Exception('wtf are you doing?')

    def set_language(self, language):
        """Language setting must be set in this method b/c non-occidental
        (western) languages require a separate stopwords class.
        """
        if not language or len(language) != 2:
            raise Exception("Your input language must be a 2 char language code, \
                for example: english-->en \n and german-->de")

        # If explicitly set language, don't use meta
        self.use_meta_language = False

        # Set oriental language stopword class
        self._language = language
        self.stopwords_class = self.get_stopwords_class(language)

    language = property(get_language, set_language,
                        del_language, "language prop")

    @staticmethod
    def get_stopwords_class(language):
        if language == 'hi':
            return StopWordsHindi
        return StopWords

    @staticmethod
    def get_parser():
        return Parser


class ArticleConfiguration(Configuration):
    pass


class SourceConfiguration(Configuration):
    pass
