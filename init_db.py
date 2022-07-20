def scrape_data():
    import requests
    standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
    data = requests.get(standings_url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text)
    standings_table = soup.select('table.stats_table')[0]
    links = standings_table.find_all('a')
    links = [l.get("href") for l in links]
    links = [l for l in links if '/squads/' in l]
    team_urls = [f"https://fbref.com{l}" for l in links]

    data = requests.get(team_urls[0])

    import pandas as pd
    matches = pd.read_html(data.text, match="Scores & Fixtures")[0]

    soup = BeautifulSoup(data.text)
    links = soup.find_all('a')
    links = [l.get("href") for l in links]
    links = [l for l in links if l and 'all_comps/shooting/' in l]
    links
    data = requests.get(f"https://fbref.com{links[0]}")

    shooting = pd.read_html(data.text, match="Shooting")[0]

    shooting.columns = shooting.columns.droplevel()
    team_data = matches.merge(shooting[["Date", "Sh", "SoT", "Dist", "FK", "PK", "PKatt"]], on="Date")

    years = list(range(2022, 2018, -1))
    print(years)
    all_matches = []

    standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"

    import time
    for year in years:
        data = requests.get(standings_url)
        soup = BeautifulSoup(data.text)
        standings_table = soup.select('table.stats_table')[0]

        links = [l.get("href") for l in standings_table.find_all('a')]
        links = [l for l in links if '/squads/' in l]
        team_urls = [f"https://fbref.com{l}" for l in links]
        
        previous_season = soup.select("a.prev")[0].get("href")
        standings_url = f"https://fbref.com{previous_season}"
        
        for team_url in team_urls:
            team_name = team_url.split("/")[-1].replace("-Stats", "").replace("-", " ")
            data = requests.get(team_url)
            matches = pd.read_html(data.text, match="Scores & Fixtures")[0]
            soup = BeautifulSoup(data.text)
            links = [l.get("href") for l in soup.find_all('a')]
            links = [l for l in links if l and 'all_comps/shooting/' in l]
            data = requests.get(f"https://fbref.com{links[0]}")
            time.sleep(5)
            shooting = pd.read_html(data.text, match="Shooting")[0]
            shooting.columns = shooting.columns.droplevel()
            try:
                team_data = matches.merge(shooting[["Date", "Sh", "SoT", "Dist", "FK", "PK", "PKatt"]], on="Date")
            except ValueError:
                continue
            team_data = team_data[team_data["Comp"] == "Premier League"]
            
            team_data["Season"] = year
            team_data["Team"] = team_name
            all_matches.append(team_data)
            time.sleep(3)

        match2_df = pd.concat(all_matches)
        len(match2_df)
        match2_df.columns = [c.lower() for c in match2_df.columns]

    return match2_df

def retrieve_file():
    import pandas as pd

    # Dataframe clean
    data_file = "Resources/matches_2.csv"
    data_file_df = pd.read_csv(data_file)

    matches_df = data_file_df.drop(columns=['Unnamed: 0', 'notes'], axis=1)


    matches_final = matches_df.drop_duplicates(subset=['date', 'time', 'comp', 'round', 'day', 'venue', 'result',
        'gf', 'ga', 'opponent', 'xg', 'xga', 'poss', 'attendance', 'captain',
        'formation', 'referee', 'match report', 'sh', 'sot', 'dist',
        'fk', 'pk', 'pkatt', 'season', 'team'])

    matches_final = matches_final.rename(columns={'match report': 'match_report'})
    matches_final.to_csv("Resources\matches_final.csv", index=False)

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
    # Execute a command: this creates a new table
    engine.execute('DROP TABLE IF EXISTS matches_final CASCADE;')
    engine.execute('CREATE TABLE matches_final (id INT, date DATE, ' 
                'time VARCHAR, comp VARCHAR, round VARCHAR, '
                'day VARCHAR, venue VARCHAR, result VARCHAR, ' 
                'gf INT, ga INT, opponent VARCHAR, xg FLOAT, '
                'xga FLOAT, poss FLOAT, attendance FLOAT, ' 
                'captain VARCHAR, formation VARCHAR, referee VARCHAR, '
                'match_report VARCHAR, sh FLOAT, sot FLOAT, ' 
                'dist FLOAT, fk FLOAT, pk FLOAT, pkatt FLOAT, season INT, '
                'team VARCHAR);'
                )
    matches_final.to_sql('matches_final', con=engine, if_exists='replace')

    return matches_final