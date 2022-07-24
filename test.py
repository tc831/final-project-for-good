from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

base_url = 'https://fbref.com/'

scores_url = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'

browser.visit(scores_url)

time.sleep(1)

# Scrape page into Soup
html = browser.html
soup = bs(html, "html.parser")
next_season = soup.find("a", class_="next")
next_season_link = base_url + next_season["href"]
browser.quit()
table = pd.read_html(next_season_link)
upcoming_matches = table[0]
upcoming_matches = upcoming_matches[['Wk', 'Day', 'Date', 'Time', 'Home', 'Away', 'Venue']]
upcoming_matches = upcoming_matches.dropna()

browser = Browser('chrome', **executable_path, headless=False)    
browser.visit(next_season_link)
next_season_link = browser.html
next_season_link_soup = bs(next_season_link, 'html.parser')
# next_season_title = next_season_link_soup.find_all('div', class_='comps')

next_season_title = next_season_link_soup.find('div', class_='comps')
next_season_title1 = next_season_title.find('h1').text.strip('\t\r\n')

nxt_season = next_season_title1.split("-")[1].split(" ")[0]
browser.quit()

upcoming_matches['season'] = nxt_season
upcoming_matches['mod1'] = ''
upcoming_matches['mod2'] = ''
upcoming_matches['mod3'] = ''
upcoming_matches['mod4'] = ''

upcoming_matches_df = upcoming_matches.iloc[1:]
upcoming_matches_df = upcoming_matches_df.reset_index(drop=True)

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from config import password

url = f'postgresql://postgres:{password}@localhost:5432/final_project'
engine = create_engine(url)

# Create database if doesn't exist
if not database_exists(engine.url):
    create_database(engine.url)
else:
    # Connect the database if exists.
    engine.connect()

upcoming_matches_df.to_sql('upcoming_matches_df', con=engine, if_exists='replace')