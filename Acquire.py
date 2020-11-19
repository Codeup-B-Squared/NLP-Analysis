# Imports

import pandas as pd
import numpy as np
from requests import get
from bs4 import BeautifulSoup
import os

######################################## Acquire URLS ########################################

# option for period is 
# daily, weekly, monthly

# enhancing the function to take a list of language and timeline as input and return lists of url and
# and a list of language

def get_top_repo(language_list, timeline):

    '''
    Creates a list of repository urls, 25 for each url specified at the given time period of daily,
    weekly, or monthly. Returns the urls in a df with the coding language catagory and the url.
    '''
    repo_links = []
    language=[]
    for element in language_list:
        
        url = f'https://github.com/trending/{element}?since={timeline}&spoken_language_code=en'
        response = get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        h1s = soup.find_all('h1', class_ = 'h3 lh-condensed')
        
        
        for elem  in h1s:
            repo_name = elem.get_text()
            repo_name = repo_name.replace('\n', '')
            repo_name = repo_name.replace(' ', '')
            links = 'https://github.com/' + repo_name
            repo_links.append(links)
            item= element
            language.append(item)

    df = pd.DataFrame(repo_links, language).reset_index().rename(columns = {'index': 'language', 0:'link'})
            
    return df

##################################### Web Scraping #####################################

# creating a function that automates the parsing process given a list of links to parse
def get_content_df(links):

    '''Takes in a list of urs and parses through everyone of them to return a df of the 
    repo associated with the url and its Readme file, watcher count, star count, and 
    forks count.
    '''
    
    # empty list to hold feadme file content
    content = []
    # empty list to hold counts of user watchers
    watchers = []
    # empty list to hold counts of user stars
    stars = []
    # empty list to hold counts of user forks
    forks = []
    
    # looping through each url generated from function above
    for url in links:
        
        # empty list to hold individual repo ['watchers','stars','forks']
        counts = []
        
        # scraping for readme content
        response = get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        article = soup.find('article', itemprop = 'text')
        article_text = article.get_text()
        item = {
        'content': article_text
        }
        content.append(item)
        
        # scraping for watcher, star, fork counts
        text = soup.find_all('a', class_='social-count')
        for h in text:
            #['watchers','stars','forks']
            counts.append(h.get_text().replace('\n','').replace(' ',''))
        
        # splitting counts to appropriate list
        watchers.append(counts[0])
        stars.append(counts[1])
        forks.append(counts[2])
    
    # creating content into a df
    df = pd.DataFrame(content)
    df['watchers'] = watchers
    df['starts'] = stars
    df['forks'] = forks
    
    return df