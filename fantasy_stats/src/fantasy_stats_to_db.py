import logging
import os
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from src.constants import CSV_FILE, DB_FILE, SCHEMA_FILE
from src.data.database import create_db_schema, load_players_csv_to_db
from src.stats.fantasy_stats import (
    build_player_csv,
    get_seasonal_fantasy_stats_table,
)


logging.basicConfig(level=logging.INFO)


def cleanup_old_files(files):
    for file in files:
        try:
            os.remove(file)
        except OSError:
            logging.debug(f"File does not exist: {file}")


if __name__ == "__main__":
    cleanup_old_files([CSV_FILE, DB_FILE])

    # Feel free to change the year "2019" to any year you desire
    parsed_table = get_seasonal_fantasy_stats_table("2019")
    logging.info("Extracted HTML table from PFR...")

    build_player_csv(parsed_table)
    logging.info("Successfully built player CSV...")

    create_db_schema(SCHEMA_FILE, DB_FILE)
    logging.info("Created DB schema...")

    load_players_csv_to_db(DB_FILE, CSV_FILE)
    logging.info("Loaded data to sqlite3 successfully!")
