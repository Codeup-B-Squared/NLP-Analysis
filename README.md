![Project-Header](https://i.pinimg.com/originals/76/f3/33/76f333fd9fd2ad9bd020b49d4bb71f31.gif)

# Table of Contents
1. [About the Project](https://github.com/ThompsonBethany01/Readme_Language_Analysis#About-the-Project)  
    - [*Background*](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Background) | [*Goals*](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Goals) |  [*Initial Thoughts*](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Initial-Thoughts)  |  [*Outline*](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Outline)  |  [*Data Dictionary*](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Data-Dictionary)
2. [Deliverables](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Deliverables)  
3. [Project Steps](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Project-Steps)  
    - [*Acquire*](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Acquire) | [*Prepare*](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Prepare) | [*Explore*](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Explore) | [*Model*](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Model) | [*Conclusions*](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Conclusions)
4. [How to Reproduce](https://github.com/ThompsonBethany01/Readme_Language_Analysis#How-to-Reproduce)  
5. [Author](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Author)

# About the Project

## Background
For this project, we are acquiring the data ourselves from trending GitHub repositories. We need to use Natural language processing (NLP) to convert the data for our model to use. To quote [IBM](https://www.ibm.com/cloud/learn/natural-language-processing),  
> "NLP refers to the branch of computer science — and more specifically, the branch of artificial intelligence or AI — concerned 
> with giving computers the ability to understand text and spoken words in much the same way human beings can."

## Goals
The purpose of this project is to predict the programming language used in a repository based on the text within the Readme file alone. Data will be scraped from Github repositories of choice, such as the repositories with the most stars or highest trending.

## Initial Thoughts
Some ideas to keep in mind while exploring the data:  
- What are the most common words in READMEs?
- What does the distribution of IDFs look like for the most common words?
- Does the length of the README vary by programming language?
- Do different programming languages use a different number of unique words?
  
## Outline

![Project-Outline](https://i.pinimg.com/originals/6c/41/af/6c41af04787b169bd7a5ee79769c5e27.png)

## Data Dictionary

| Feature Name | Description                                             |
|--------------|---------------------------------------------------------|
| content      | raw text data from repository Readme file               |
| watchers     | count of users watching the repository                  |
| stars        | count of users that have starred the repository         |
| forks        | count of users that have forked the repository          |
| clean        | content that has been cleaned.                          |
| tokenized    | clean content that have been tokenized                  |
| stemmed      | tokenized content that has been stemmed                 |
| lemmatized   | tokenized content that has been lemmatized              |
| filtered     | lemmatized content that has been filtered               |
| word_list    | list of words used in content, not unique               |
| char_length  | count of characters used in content                     |
| word_length  | count of words in word_list                             |
| language     | coding language of repository by GitHub trending filter |
| link         | generated url by web scraping from GitHub trending page |

[Back to Top](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Table-of-Contents)

# Deliverables
- Data_Analysis.ipynb
  - A well-documented jupyter notebook containing my analysis
  - [Click here](https://github.com/Codeup-B-Squared/NLP-Analysis/blob/main/Data_Analysis.ipynb) to be directed to the file.
- Presentation
  - Summary of findings including a well-labeled visual
  - [Click here](https://www.canva.com/design/DAEN6nqX74E/f8zXdDZc8EIHpqd-nnFYxg/view?utm_content=DAEN6nqX74E&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu) to be directed to the presentation.

[Back to Top](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Table-of-Contents)

# Project Steps
## Acquire
- Acquired data from the top trending repositories in Github for 4 different languages: Python, Java, JavaScript, Swift
- First, we extracted 100 repositories(25 for each language) that were trending on a monthly basis, repeated the same for weekly basis, and then daily basis
- Automated the webscrapping by creating a function that extracts the content of the read me from each of the repositories 
## Prepare
- Cleaned the data by removing white spaces, characters, and lowercasing all of the words
- Tokenized the content
- Stemmed the content, lemmatized the content, and then filtered by removing the stop words
- Splitted the data into train and test data set

## Explore
- Explored the word counts
- Plotted the  most frequent words in repos for each language
- Created a word cloud of the words for each language
- Created bigrams and plotted the bigrams(barplot, wordcloud)
## Model
- Created a bag of words and used it to train the logistic model 
- Created a tf-idf and created a logit model
- logit model with tf-idf beat the baseline and the model created using bag of words

Accuracy of Models Created

| Model Name                         | Train  | Validate | Test   |
|------------------------------------|--------|----------|--------|
| TF-iDF + LogisticsRegression       | 100%.  | 80.49 %  | 80.65 %|
| Bag of Words + LogisticsRegression | 100 %  | 69.51 %  | 74.19 %|

## Conclusions
- Logit model with Tf-iDF performed at 81% accuracy.
- The accuracy of the model improved as we acquired more data.

[Back to Top](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Table-of-Contents)

# How to Reproduce
- [X] Read this Readme.md file
- [ ] Download <kbd>Data_Anlysis.ipynb</kbd>, <kbd>Acquire.py</kbd>, and <kbd>Prepare.py</kbd> in your working directory.
- [ ] Run <kbd>Data_Analysis.ipynb</kbd>
- [ ] Continue your own work in the notebook, or start from scratch with a new notebook in the same directory (be sure to import the modules)

# Authors
[Bethany Thompson](https://github.com/ThompsonBethany01)  
[Bibek Mainali](https://github.com/MainaliB)

[Back to Top](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Table-of-Contents)
