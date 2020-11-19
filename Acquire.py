# Imports

import pandas as pd
import numpy as np
from requests import get
from bs4 import BeautifulSoup
import os

######################################## Acquire URLS ########################################

def acquire_repo_urls(language, period):
    '''
    Acquire URL's of GitHub's Most Trending repositories in English and filtered by coding 
    language and time period of choice. Period can be daily, weekly, or monthly. Top
    coding languages include Python, Javascript, and Swift. Returns a list of 25 URLS.
    '''
    headers = {'User-Agent': 'GitHub'}

    # URL of GitHub trending repo page with langauge and period specified
    response = get(f'https://github.com/trending/{language}?since={period}&spoken_language_code=en', headers=headers)
    
    # parse html text
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # all html text from trending page with h1 heading
    h1 = soup.find_all('h1', class_='h3 lh-condensed')

    # empty list to hold urls
    repo_urls = []

    # looping through all headers in h1
    for h in h1:

        # converting name to normalized text, no backspaces, spaces
        repo_name = h.get_text()
        repo_name = repo_name.replace("\n","")
        repo_name = repo_name.replace(" ","")

        # adding github url to complete the url
        repo_name = 'https://github.com/' + repo_name

        # adding one url to list of urls
        repo_urls.append(repo_name)
    
    return repo_urls

    ##################################### Web Scraping #####################################