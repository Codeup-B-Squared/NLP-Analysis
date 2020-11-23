import pandas as pd
import numpy as np
import unicodedata
import re
import json
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

##################################### Basic Text Cleaner ######################################

def clean_content(content_list):
    clean_content = []
    for item in content_list:
        article = unicodedata.normalize('NFKD', item)\
        .encode('ascii', 'ignore')\
        .decode('utf-8', 'ignore')
        article = article.replace('\n', '')
        article = article.lower()
        article = re.sub(r'[^a-z0-9\s]', '', article)
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

####################################### User Input #######################################

readme = input('Enter Readme File Content in string:')

df2 = {'text': readme}

df2 = pd.DataFrame(df2, columns=['text'], index=range(0,1))

df2['cleaned'] = clean_content(df2.text)

df2['tokenized'] = tokenizing(df2.cleaned)

df2['lemmatized'] = lemmatizing(df2.tokenized)

df2['filtered'] = remove_stopwords(df2.lemmatized)

####################################### Create the Model #######################################

df = pd.read_csv('final_df.csv', index_col = 0)

tfidf = TfidfVectorizer(stop_words='english', min_df=10)
X = tfidf.fit_transform(df.filtered)
y = df.language

lm_tfidf = LogisticRegression(penalty='none').fit(X, y)

####################################### Predict #######################################

x = tfidf.transform(df2.filtered)

predicted = lm_tfidf.predict(x)

print('\n\nI predict the Repository is', predicted[0], 'based on the readme file given.')