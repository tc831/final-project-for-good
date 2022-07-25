from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd

base_url = 'https://fbref.com/'
scores_url = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'

scores = requests.get(scores_url)
soup = bs(scores.text)
next_season = soup.find("a", class_="next")
next_season_link = base_url + next_season["href"]

table = pd.read_html(next_season_link)
next_season_link_soup = bs(requests.get(next_season_link).text)
next_season_title = next_season_link_soup.find_all('div', class_='comps')

next_season_title = next_season_link_soup.find('div', class_='comps')
next_season_title1 = next_season_title.find('h1').text.strip('\t\r\n')

nxt_season = next_season_title1.split("-")[1].split(" ")[0]

upcoming_matches = table[0]
upcoming_matches = upcoming_matches[['Wk', 'Day', 'Date', 'Time', 'Home', 'Away', 'Venue']]

upcoming_matches= upcoming_matches.dropna()

upcoming_matches['season'] = nxt_season
upcoming_matches['mod1'] = ''
upcoming_matches['mod2'] = ''
upcoming_matches['mod3'] = ''
upcoming_matches['mod4'] = ''

upcoming_matches_df = upcoming_matches.iloc[1:]
upcoming_matches_df = upcoming_matches_df.reset_index(drop=True)
upcoming_matches_df