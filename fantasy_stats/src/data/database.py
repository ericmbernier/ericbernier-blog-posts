import csv
import sqlite3

from src.data.db_columns import (
    COLUMN_PLAYER,
    COLUMN_TEAM,
    COLUMN_FANTASY_POSITION,
    COLUMN_AGE,
    COLUMN_GAMES,
    COLUMN_GAMES_STARTED,
    COLUMN_COMPLETIONS,
    COLUMN_PASS_ATTEMPTS,
    COLUMN_PASS_YARDS,
    COLUMN_PASS_TDS,
    COLUMN_INTERCEPTIONS,
    COLUMN_RUSH_ATTEMPTS,
    COLUMN_RUSH_YARDS,
    COLUMN_RUSH_YARDS_PER_ATTEMPT,
    COLUMN_RUSH_TDS,
    COLUMN_TARGETS,
    COLUMN_RECEPTIONS,
    COLUMN_REC_YARDS,
    COLUMN_YARDS_PER_RECEPTION,
    COLUMN_REC_TDS,
    COLUMN_FUMBLES,
    COLUMN_FUMBLES_LOST,
    COLUMN_TOTAL_TDS,
    COLUMN_TWO_POINT_CON,
    COLUMN_TWO_POINT_CON_PASSING,
    COLUMN_FANTASY_POINTS_STANDARD,
    COLUMN_FANTASY_POINTS_PPR,
    COLUMN_FANTASY_POINTS_DK,
    COLUMN_FANTASY_POINTS_FD,
    CSV_HEADER_ROW,
)


def create_db_schema(schema_file, db_name):
    """
    Function that loads a database table from a schema file
    to a sqlite3 database

    :param schema_file: SQL Schema file
    :param db_name: Name of the sqlite3 database
    :return: None
    """
    with open(schema_file, "r") as schema_file:
        sql_script = schema_file.read()

    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()
    db.close()


def load_players_csv_to_db(db_name, players_csv_file):
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    # Open the CSV file in "read" "text" (rt) mode
    with open(players_csv_file, "rt") as player_table:
        dr = csv.DictReader(player_table)
        player_data = [
            (
                i[COLUMN_PLAYER],
                i[COLUMN_TEAM],
                i[COLUMN_FANTASY_POSITION],
                i[COLUMN_AGE],
                i[COLUMN_GAMES],
                i[COLUMN_GAMES_STARTED],
                i[COLUMN_COMPLETIONS],
                i[COLUMN_PASS_ATTEMPTS],
                i[COLUMN_PASS_YARDS],
                i[COLUMN_PASS_TDS],
                i[COLUMN_INTERCEPTIONS],
                i[COLUMN_RUSH_ATTEMPTS],
                i[COLUMN_RUSH_YARDS],
                i[COLUMN_RUSH_YARDS_PER_ATTEMPT],
                i[COLUMN_RUSH_TDS],
                i[COLUMN_TARGETS],
                i[COLUMN_RECEPTIONS],
                i[COLUMN_REC_YARDS],
                i[COLUMN_YARDS_PER_RECEPTION],
                i[COLUMN_REC_TDS],
                i[COLUMN_FUMBLES],
                i[COLUMN_FUMBLES_LOST],
                i[COLUMN_TOTAL_TDS],
                i[COLUMN_TWO_POINT_CON],
                i[COLUMN_TWO_POINT_CON_PASSING],
                i[COLUMN_FANTASY_POINTS_STANDARD],
                i[COLUMN_FANTASY_POINTS_PPR],
                i[COLUMN_FANTASY_POINTS_DK],
                i[COLUMN_FANTASY_POINTS_FD],
            )
            for i in dr
        ]

    # Use a list comprehension to help build the cumbersome insert statement
    insert_values = ["?" for column in CSV_HEADER_ROW]
    insert_params = ",".join(insert_values)

    cur.executemany(
        # Instead of hand-typing this insert statement I used a list comprehension
        # above to create a list of ?s for each column in our table, and joined the
        # list together, comma separated. The starting 'null' represents the
        # auto-incremented 'id' column in our database
        f"INSERT INTO players VALUES (null, {insert_params});",
        player_data,
    )
    con.commit()
    con.close()
