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
    df['lemmatized'] = lemmatizing(df.tokenized)
    df['filtered'] = remove_stopwords(df.lemmatized)

    df['word_list'] = df.lemmatized.str.split()
    df['char_length'] = df.lemmatized.str.len()
    df['word_length'] = [len(wordlist) for wordlist in df.word_list]

    return df

################################# Split to Train & Validate ##################################

def train_validate(df):
    '''
    Function to split df into 68% train and 32% validate. Returns the two split
    dataframes. Random seed splits into 18 observations from java and javscript
    and 16 observations from python and swift.
    '''
    # Import to use split function, can only split two at a time
    from sklearn.model_selection import train_test_split

    # split into train + validate together and test by itself
    # Set random_state so we can reproduce the same 'random' data
    train, validate = train_test_split(df, test_size = .32, random_state = 123)

    # Will print the shape of eachvariable as a percentage of the total data set
    # Varialbe to hold the sum of all rows (total observations in the data)
    total = df.count()[0]
    print("\ntrain percent: ", round(((train.shape[0])/total),2) * 100, 
            ", validate percent: ", round(((validate.shape[0])/total),2) * 100, )

    return train, validate