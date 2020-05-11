import sys
from os import path

from bs4 import BeautifulSoup

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from src.stats.player_stats import (
    STAT_RECS,
    get_player_stats_from_pfr,
    get_stat_for_season,
)

# Feel free to change this to the URL of your favorite player
PLAYER_PFR_URL = "https://www.pro-football-reference.com/players/M/MoorD.00/gamelog/"
YEAR_2019 = "2019"


if __name__ == "__main__":
    html_doc = get_player_stats_from_pfr(PLAYER_PFR_URL, YEAR_2019)
    soup = BeautifulSoup(html_doc, "html.parser")
    game_stats = soup.find_all("tr", id=lambda x: x and x.startswith("stats."))

    receptions = get_stat_for_season(game_stats, STAT_RECS)
    print(f"DJ Moore 2019 receptions: {receptions}")
