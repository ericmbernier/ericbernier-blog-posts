import sys
from argparse import ArgumentParser
from decimal import Decimal
from os import path


sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from dfs_tracker.dfs_data.parse_dfs_data import parse_all_csv_files
from dfs_tracker.dfs_data.plot_dfs_data import plot_dfs_results
from dfs_tracker.contests.sports import SPORTS_ALL


def track_dfs_performance(files_dir):
    dfs_entries, sports = parse_all_csv_files(files_dir)

    entry_fees = {}
    winnings = {}

    for sport in sports:
        entry_fees[sport] = 0
        winnings[sport] = 0

    for entry in dfs_entries:
        entry_fees[SPORTS_ALL] += entry.entry_fee
        entry_fees[entry.sport] += entry.entry_fee

        winnings[SPORTS_ALL] += entry.winnings
        winnings[entry.sport] += entry.winnings

    roi = {
        sport: _calculate_roi(entry_fees[sport], winnings[sport]) for sport in sports
    }

    _summarize_results(dfs_entries, sports, entry_fees, winnings, roi)
    plot_dfs_results(dfs_entries, sports)


def _calculate_roi(initial_investment, final_value):
    if initial_investment == 0 and final_value == 0:
        return 0

    if initial_investment == 0:
        return "Infinity"

    net_return = final_value - initial_investment
    roi = Decimal(net_return / initial_investment * 100)
    return "{0:.2f}".format(roi)


def _summarize_results(dfs_entries, sports, entry_fees, winnings, roi):
    sports_sorted = sorted(sports)

    print(f"Entries Recorded, All Sports: {len(dfs_entries)}\n")

    for sport in sports_sorted:
        print(f"Entry Fees, {sport}: ${entry_fees[sport]}")
        print(f"Winnings, {sport}: ${winnings[sport]}")
        print(f"ROI, {sport}: {roi[sport]}%\n")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-f",
        "--files",
        dest="files",
        help="Directory containing all of our CSV files",
        metavar="FILES",
    )
    args = parser.parse_args()

    track_dfs_performance(args.files)
