####################################### Prepare Imports #######################################

import pandas as pd
import numpy as np
import unicodedata
import re
import json
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

################################### Helper Prep Functions #####################################

##################################### Basic Text Cleaner ######################################

def clean_content(content_list):
    clean_content = []
    for item in content_list:
        article = unicodedata.normalize('NFKD', item)\
        .encode('ascii', 'ignore')\
        .decode('utf-8', 'ignore')
        article = article.replace('\n', '')
        article = article.lower()
        clean_content.append(article)
    return clean_content

######################################## Tokenizer Cleaner ######################################

def tokenizing(content_list):
    tokenize_content = []
    tokenizer = nltk.tokenize.ToktokTokenizer()
    for item in content_list:
        article = tokenizer.tokenize(item, return_str = True)
        tokenize_content.append(article)
    return tokenize_content

######################################## Stemming Cleaner #######################################

def stemming(content_list):
    stemmed = []
    ps = nltk.porter.PorterStemmer()
    for item in content_list:
        stems = [ps.stem(words) for words in item.split()]
        item_stemmed = ' '.join(stems)
        stemmed.append(item_stemmed)
    return stemmed

######################################## Lematizer Cleaner #####################################

def lemmatizing(content_list):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmatized = []
    for item in content_list:
        lemmas = [wnl.lemmatize(word) for word in item.split()]
        item_lemmatized = ' '.join(lemmas)
        lemmatized.append(item_lemmatized)
    return lemmatized

####################################### Remove Stopwords #######################################

def remove_stopwords(content_list):
    no_stopwords = []
    stopword_list = stopwords.words('english')
    for item in content_list:
        words = item.split()
        filtered_words = [w for w in words if w not in stopword_list]
        article_without_stopwords = ' '.join(filtered_words)
        no_stopwords.append(article_without_stopwords)
    return no_stopwords

###################################### Prepare Function #######################################

def prepare_df(df):
    '''
    Cleaning readme file content with natural language processing. Converting count columns
    from string to integers (i.e. 1.5k to 1500)
    '''

    # using pandas to convert string numbers to integers
    for col in ['watchers','stars','forks']:
        df[col] = df[col].str.replace('k','00').str.replace('.','').astype('int')

    df['clean'] = clean_content(df.content)
    df['tokenized'] = tokenizing(df.clean)
    df['stemmed'] = stemming(df.tokenized)
    df1['lemmatized'] = lemmatizing(df.tokenized)
    df1['filtered'] = remove_stopwords(df.lemmatized)

    return df