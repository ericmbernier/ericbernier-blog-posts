import csv
import logging

import requests
from bs4 import BeautifulSoup

from src.constants import CSV_FILE
from src.data.db_columns import CSV_HEADER_ROW


PFR_FANTASY_URL_PREFIX = "https://www.pro-football-reference.com/years/"
PFR_FANTASY_URL_SUFFIX = "/fantasy.htm"


def get_seasonal_fantasy_stats_table(year):
    """
    Function that extracts the HTML table from PFR for the provided year
    This table contains all of the stats for all players for the desired season.

    :param year: String representing the year
    :return: The table tag object containing all of our stats
    """
    pfr_url = f"{PFR_FANTASY_URL_PREFIX}{year}{PFR_FANTASY_URL_SUFFIX}"
    response = requests.get(pfr_url)

    soup = BeautifulSoup(response.content, "html.parser")
    parsed_table = soup.find_all("table")[0]
    return parsed_table


def build_player_csv(parsed_table):
    """
    Function that creates a CSV from the PFR stats table

    :param parsed_table: Table object extracted with BeautifulSoup
    :return: None
    """
    pfr_table_rows = parsed_table.findAll("tr")
    pfr_player_rows = pfr_table_rows[2:]

    _write_row_to_csv(CSV_HEADER_ROW)
    for row in pfr_player_rows:
        player_data = _extract_data_from_row(row)
        _write_row_to_csv(player_data)


def _extract_data_from_row(row):
    """
    Function that extracts a player's stats from an HTML table row
    via BeautifulSoup4

    :param row: 'tr' or table row containing our stats
    :return: List of player stats
    """
    player_data = []
    player_name_data = row.find("td", attrs={"data-stat": "player"})

    if player_name_data is None:
        return

    player_name = player_name_data.a.get_text()
    player_data.append(player_name)

    # We want to slice the list from the first element after "player
    # until the fourth-to-last data element. The last three elements are
    # fantasy ranking related, and I do not want this data.
    remaining_cells = row.find_all("td")[1:-3]

    for cell in remaining_cells:
        player_data.append(cell.get_text())

    return player_data


def _write_row_to_csv(row):
    """
    Function that writes a row (list) of data to our player CSV

    :param row: List of player data
    :return: None
    """
    # PFR mixes in some meta-rows into their stats table, and we do not want these
    if not row:
        logging.debug("Skipping non-player data row!")
        return

    # Open the CSV file in 'append' mode
    with open(CSV_FILE, mode="a") as player_data_file:
        player_data_writer = csv.writer(
            player_data_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        player_data_writer.writerow(row)
