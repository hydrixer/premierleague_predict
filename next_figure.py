from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import requests
import time

def next_fixture():
    fixtures = []
    standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
    data = requests.get(standings_url)

    soup = BeautifulSoup(data.text, features="lxml")
    standings_table = soup.select('table.stats_table')[0]
    links = standings_table.find_all('a')
    links = [l.get("href") for l in links]
    links = [l for l in links if '/squads/' in l]
    team_urls = [f"https://fbref.com{l}" for l in links]
    for team_url in team_urls:
        data = requests.get(team_url)
        team_name = team_url.split('/')[-1].replace("-Stats", "").replace("-", " ")
        matches = pd.read_html(StringIO(data.text), match="Scores & Fixtures")[0]
        matches['Date'] = pd.to_datetime(matches['Date'], errors='coerce')  #获取下一场比赛队伍
        future_matches = matches[
            (matches['Date'].dt.date >= pd.Timestamp.now().normalize().date())
        ]
        if future_matches.iloc[0]['Venue'] == 'Home':   #only add infomation HOME-AWAY
            match_record = {
                'date':future_matches.iloc[0]['Date'].date(),
                'home':team_name,
                'away':future_matches.iloc[0]['Opponent']
            }
            fixtures.append(match_record)
            print(f"date:{future_matches.iloc[0]['Date'].date()}, {team_name} VS {future_matches.iloc[0]['Opponent']}")
        else:
            continue
        time.sleep(10)
    return fixtures

print(next_fixture())