![Project-Header](https://i.pinimg.com/originals/e4/6c/25/e46c2529c95068026efd3f537d6b06fc.png)

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
If you try to google which programming language to learn first, you'll come up with more answers than you'll know what to do with. To quote [Full Stack Academy](https://www.fullstackacademy.com/blog/nine-best-programming-languages-to-learn),  
> The toughest part of learning programming is deciding where to begin. There are hundreds of programming languages in widespread use, each with its own 
> complexities and idiosyncrasies.   

Perhaps this project could lead to the simplest answer - whichever language is most popular.

## Goals
The purpose of this project is to predict the programming language used in a repository based on the text within the Readme file alone. Data will be scraped from Github repositories of choice, such as the repositories with the most stars or highest trending.

## Initial Thoughts
Some ideas to keep in mind while exploring the data:  
- What are the most common words in READMEs?
- What does the distribution of IDFs look like for the most common words?
- Does the length of the README vary by programming language?
- Do different programming languages use a different number of unique words?
  
## Outline

## Data Dictionary

| DF Name | Feature Name | Description                                             |
|---------|--------------|---------------------------------------------------------|
| urls    | language     | coding language of repository by GitHub trending filter |
|         | link         | generated url by web scraping from GitHub trending page |
| df      | content      | raw text data from repository Readme file               |
|         | watchers     | count of users watching the repository                  |
|         | stars        | count of users that have starred the repository         |
|         | forks        | count of users that have forked the repository          |
|         | doc_length   | word length of content                                  |

[Back to Top](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Table-of-Contents)

# Deliverables
- Data_Analysis.ipynb
  - A well-documented jupyter notebook containing my analysis
- Presentation
  - Summary of findings including a well-labeled visual

[Back to Top](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Table-of-Contents)

# Project Steps
## Acquire
## Prepare
## Explore
## Model
## Conclusions

[Back to Top](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Table-of-Contents)

# How to Reproduce
## Tools Used
## Steps

# Authors
[Bethany Thompson](https://github.com/ThompsonBethany01)
[Bibek Mainali](https://github.com/MainaliB)

[Back to Top](https://github.com/ThompsonBethany01/Readme_Language_Analysis#Table-of-Contents)
