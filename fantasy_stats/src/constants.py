"""
constants.py
File contains some constants shared across our modules
If you move this file the PROJECT_ROOT var needs fixing.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

CSV_FILE = f"{PROJECT_ROOT}/player_data.csv"
DB_FILE = f"{PROJECT_ROOT}/football.db"
SCHEMA_FILE = f"{PROJECT_ROOT}/players.sql"
