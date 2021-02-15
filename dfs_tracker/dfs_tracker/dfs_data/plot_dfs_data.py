from itertools import accumulate

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from dfs_tracker.contests.sports import (
    SPORTS_ALL,
    SPORTS_MLB,
    SPORTS_NASCAR,
    SPORTS_NBA,
    SPORTS_NFL,
    SPORTS_NHL,
    SPORTS_PGA,
    SPORTS_WNBA,
)


DFS_TRACKER = "DFS Tracker"
COLOR_LOOKUP = {
    SPORTS_ALL: "navy",
    SPORTS_MLB: "red",
    SPORTS_NASCAR: "gold",
    SPORTS_NBA: "orange",
    SPORTS_NFL: "brown",
    SPORTS_NHL: "black",
    SPORTS_PGA: "green",
    SPORTS_WNBA: "purple",
}
SUBPLOT_HEIGHT = 300


def plot_dfs_results(dfs_entries, sports):
    dfs_entries.sort(key=lambda entry: entry.contest_date)
    sports_sorted = sorted(sports)

    profit_by_day = {sport: {} for sport in sports_sorted}

    for entry in dfs_entries:
        _add_profits_for_day(entry, SPORTS_ALL, profit_by_day)
        _add_profits_for_day(entry, entry.sport, profit_by_day)

    cumulative_profits = {
        sport: list(accumulate(profit_by_day[sport].values()))
        for sport in sports_sorted
    }

    # Build up a list of our subplot text titles. The
    # Plotly figure will expect a list
    subplot_titles = []
    for sport in sports_sorted:
        subplot_titles.append(f"Cumulative Profits, {sport}")

    fig = make_subplots(rows=len(sports_sorted), cols=1, subplot_titles=subplot_titles)

    for count, sport in enumerate(sports_sorted, start=1):
        # Append each subplot to our Plotly figure. If the sport we are
        # plotting is not found in our COLOR_LOOKUP we default to black.
        # Our x-axis is our unique dates played for the current sport,
        # and our y-axis is our cumulative profits over these dates.
        fig.append_trace(
            go.Scatter(
                x=list(profit_by_day[sport].keys()),
                y=list(cumulative_profits[sport]),
                name=f"{DFS_TRACKER}, {sport}",
                line=dict(
                    color=COLOR_LOOKUP.get(sport, "black"),
                    width=2,
                    shape="spline",
                    smoothing=1.2,
                ),
            ),
            row=count,
            col=1,
        )

        # This line is necessary to label our y-axis as dollars or "$"
        fig.update_yaxes(tickprefix="$", tickformat=",.", row=count)

    # Wrap up with some Plotly configuration
    fig_height = SUBPLOT_HEIGHT * len(sports_sorted)
    fig.update_layout(height=fig_height, width=1000, title_text="DFS Tracker by Sport")
    fig.update_traces(mode="markers+lines")
    fig.show()


def _add_profits_for_day(entry, sport, profit_by_day):
    if entry.contest_date in profit_by_day[sport]:
        profit_by_day[sport][entry.contest_date] += entry.winnings - entry.entry_fee
    else:
        profit_by_day[sport][entry.contest_date] = entry.winnings - entry.entry_fee
