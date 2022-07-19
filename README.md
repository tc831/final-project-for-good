# Final Project For Good

## Project Overview

Our group’s final project topic is to create an application to make a prediction of the winning team of the English Premier League by using match historical data. 
The data source that we have chosen to use contains information from 2017 to 2022 which consists of team names, Goals For, Goals against, expected goal, expected goals against. 

The idea is to gather the data, then use historic win-loss-draw with Goals For and against to get prediction on the selected match.

The method and language used are Python, Pandas, Postgres and Tableau. Once the data was cleaned we used ML to then populate the results shown on 


**Project Steps**

* Scrape match data using requests, BeautifulSoup, and pandas.  
* Clean the data and get it ready for machine learning using pandas.
* Make predictions about who will win a match using scikit-learn.
* Measure error and improve our predictions.

## Code

You can find the code for this project [here](https://github.com/dataquestio/project-walkthroughs/tree/master/football_matches).

File overview:

* `scraping.ipynb` - a Jupyter notebook that scrapes our data.
* `predictions.ipynb` - a Jupyter notebook that makes predictions.

# Local Setup

## Installation

To follow this project, please install the following locally:

* JupyerLab
* Python 3.8+
* Python packages
    * pandas
    * requests
    * BeautifulSoup
    * scikit-learn
    
## Datasource
https://fbref.com/en/comps/9/Premier-League-Stats
