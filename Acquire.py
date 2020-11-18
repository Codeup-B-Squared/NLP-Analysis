# Imports

import pandas as pd
import numpy as np
from requests import get
from bs4 import BeautifulSoup
import os

######################################## Acquire URLS ########################################
def acquire_repo_urls(language, period):
    
    headers = {'User-Agent': 'GitHub'}

    # Trending with Language Python
    response = get(f'https://github.com/trending/{language}?since={period}', headers=headers)
    
    print(response.ok)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    h1 = soup.find_all('h1', class_='h3 lh-condensed')

    repo_names = []

    for h in h1:
        repo_name = h.get_text()
        repo_name = repo_name.replace("\n","")
        repo_name = repo_name.replace(" ","")
        repo_name = 'https://github.com/' + repo_name
        repo_names.append(repo_name)
    
    return repo_names

    ##################################### Web Scraping #####################################