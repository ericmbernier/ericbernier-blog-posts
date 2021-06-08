import logging
import os

import pandas
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from underdog_fastapi.constants import DB_FILE, PROJECT_ROOT
from underdog_fastapi.underdog.team import TEAM_NAME_TO_ABBREV

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

UNDERDOG_CSV = f"{PROJECT_ROOT}/data/underdog.csv"

# We rename the columns in the CSV to match our players table
DB_COLUMNS = [
    "first_name",
    "last_name",
    "adp",
    "projected_points",
    "position",
    "team_name",
    "team_abbreviation",
]
logger = logging.getLogger(__name__)


def get_db():
    """
    Function used to get a SQLAlchemy Session

    :return: SQLAlchemy Session
    """
    logger.debug("Getting db session.")

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database():
    """
    Function that creates a new SQLite database from the Underdog CSV
    data file. This file implicitly uses the file referenced
    in the UNDERDOG_CSV constant

    :return: None
    """
    logger.info("Creating new players database from Underdog CSV file.")

    if os.path.exists(DB_FILE):
        # Remove any old DB files, as this allows us to
        # start the API up with a new projections file.
        # The API itself is read-only, thus this is fine.
        os.remove(DB_FILE)

    Base.metadata.create_all(bind=engine)
    df = _get_dataframe_for_db()

    try:
        with engine.begin() as connection:
            df.to_sql("players", con=connection, index=False, if_exists="append")
    except SQLAlchemyError as e:
        logger.error("The database creation failed!")
        raise
    else:
        logger.info("Players database successfully created.")


def _get_dataframe_for_db():
    """
    Function that reads the UNDERDOG_CSV file, parses it to a
    Pandas dataframe, and massages the dataframe to our desired
    data model

    :return: Pandas DataFrame
    """
    logger.debug("Parsing Underdog CSV with Pandas.")

    df = pandas.read_csv(UNDERDOG_CSV)
    df["teamAbbreviation"] = df["teamName"].map(TEAM_NAME_TO_ABBREV)

    # Some of the ADPs in the Underdog CSV are set to "-".
    # We want to set this value to None, instead.
    df.loc[df["adp"] == "-", "adp"] = None

    # Delete the CSV data we do not want to persist in our database.
    # We can delete ID here, as our database table will autoincrement
    # its ID, starting from 1.
    del df["id"]
    del df["lineupStatus"]
    del df["byeWeek"]

    # Rename the Underdog CSV column headers with our table column names
    df.columns = DB_COLUMNS

    logger.debug("Successfully parsed Underdog CSV.")
    return df
