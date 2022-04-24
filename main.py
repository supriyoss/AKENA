__tile__ = 'news'
__author__ = 'Supriyo Sarkar'
__license__ = 'JISCE'
__copyright__ = 'Copyright 2022, Supriyo Sarkar'


import pandas as pd
from websites import english_news_sites
import newspaper
from bert import generate_phrases as gp
from NER import wordBasedNER,senBasedNER

"""
Dependency Check:
1. Newspaper3k module
2. pandas
3. nltk.punkt for nlp() method in newspaper3k
"""


'''def build_category(site):
    # category wise build function for future use
    for category in site.category_urls()[1]:
        each_category = newspaper.build(category)
        build_articles(each_category)'''

INITIALIZED_CSV = False
def initialize_csv(article,keyphrases):
    #Article to csv file coversion function for first time running the scraper
    article_values = [article.title,article.keywords,keyphrases,article.url]
    db_to_df = {'Title': article_values[0],'Keywords': ','.join(article_values[1]),'Url': article_values[2]}
    df = pd.DataFrame(db_to_df,columns=['Title','Keywords', 'url'],index=[0])
    df.to_csv('news_articles3.csv',sep=';',index=True)

    print('Txt created')


def append_to_csv(article,keyphrases):
    # Article to csv file conversion functon for appending to existing csv file
    article_values = [article.title, article.keywords, keyphrases, article.url]
    db_to_df = {'Title': article_values[0], 'Keywords': ','.join(article_values[1]),
                'url': article_values[2]}

    df = pd.DataFrame(db_to_df, columns=['Title', 'Keywords', 'url'],index=[0])
    df.to_csv('news_articles3.csv', mode='a', header=False, index=True, sep=';')


def build_articles(article):
    #For building every article object in the newspaper into a human readable format and better storing capabilities
    try:
        article.download()
        article.parse()
        # article.nlp()
        # print(article.text)
        results = gp(article.text)
        mss_phrases = list(results[0])
        mmr_phrases = list(results[1])
        word_ner = wordBasedNER(article.text)
        sen_ner = senBasedNER(article.text)
        # keyphrases =                              # To be decided

    except:
        return
    global INITIALIZED_CSV
    if INITIALIZED_CSV == False:
        initialize_csv(article,keyphrases)
        INITIALIZED_CSV = True
    else:
        append_to_csv(article)
    '''print('Title:', article.title)
    print('Summary: ', article.summary)
    print('\n\n')'''


if __name__ == '__main__':
    for i in english_news_sites[1:2]:
        paper = newspaper.build(i, memoize_articles=False)
        for article in paper.articles[1:2]:
            build_articles(article)
