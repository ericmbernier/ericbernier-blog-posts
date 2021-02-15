import csv
import os

from dfs_tracker.contests.entry import get_entry_from_csv_row
from dfs_tracker.contests.sports import SPORTS_ALL


def parse_all_csv_files(files_dir):
    dfs_entries = []
    sports = {SPORTS_ALL}

    for file in os.listdir(files_dir):
        csv_file = os.path.join(files_dir, file)
        cur_dfs_entries, cur_sports = _parse_csv_file(csv_file)

        dfs_entries += cur_dfs_entries
        sports = sports | cur_sports

    return dfs_entries, sports


def _parse_csv_file(csv_file):
    cur_entries = []
    cur_sports = set()

    with open(csv_file, "r") as f:
        csv_reader = csv.DictReader(f)

        for dfs_entry_row in csv_reader:
            cur_entry = get_entry_from_csv_row(dfs_entry_row)
            cur_entries.append(cur_entry)
            cur_sports.add(cur_entry.sport)

    return cur_entries, cur_sports
