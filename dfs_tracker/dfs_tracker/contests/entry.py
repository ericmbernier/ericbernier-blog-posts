from datetime import datetime
from decimal import Decimal
from re import sub


SITE_DRAFTKINGS = "DraftKings"
SITE_FANDUEL = "FanDuel"

DRAFTKINGS_SPORT_COLUMN = "Sport"
DRAFTKINGS_CONTEST_NAME_COLUMN = "Entry"
DRAFTKINGS_CONTEST_DATE_COLUMN = "Contest_Date_EST"
DRAFTKINGS_WINNINGS_COLUMN = "Winnings_Non_Ticket"
DRAFTKINGS_ENTRY_FEE_COLUMN = "Entry_Fee"

FANDUEL_SPORT_COLUMN = "Sport"
FANDUEL_CONTEST_NAME_COLUMN = "Title"
FANDUEL_DATE_COLUMN = "Date"
FANDUEL_ENTRY_FEE_COLUMN = "Entry ($)"
FANDUEL_WINNINGS_COLUMN = "Winnings ($)"


class Entry:
    def __init__(self, site, sport, entry_fee, winnings, contest_name, contest_date):
        self.site = site
        self.sport = sport
        self.contest_name = contest_name
        self.contest_date = contest_date
        self.entry_fee = entry_fee
        self.winnings = winnings


def get_entry_from_csv_row(csv_row):
    if DRAFTKINGS_WINNINGS_COLUMN in csv_row:
        return parse_draftkings_entry(csv_row)
    elif FANDUEL_WINNINGS_COLUMN in csv_row:
        return parse_fanduel_entry(csv_row)


def parse_fanduel_entry(csv_entry_row):
    return Entry(
        site=SITE_FANDUEL,
        sport=csv_entry_row[FANDUEL_SPORT_COLUMN].upper(),
        contest_name=csv_entry_row[FANDUEL_CONTEST_NAME_COLUMN],
        contest_date=datetime.strptime(
            csv_entry_row[FANDUEL_DATE_COLUMN], "%Y/%m/%d"
        ).date(),
        entry_fee=_convert_currency_to_decimal(csv_entry_row[FANDUEL_ENTRY_FEE_COLUMN]),
        winnings=_convert_currency_to_decimal(csv_entry_row[FANDUEL_WINNINGS_COLUMN]),
    )


def parse_draftkings_entry(csv_entry_row):
    return Entry(
        site=SITE_DRAFTKINGS,
        sport=csv_entry_row[DRAFTKINGS_SPORT_COLUMN].upper(),
        contest_name=csv_entry_row[DRAFTKINGS_CONTEST_NAME_COLUMN],
        contest_date=datetime.strptime(
            csv_entry_row[DRAFTKINGS_CONTEST_DATE_COLUMN], "%Y-%m-%d %H:%M:%S"
        ).date(),
        entry_fee=_convert_currency_to_decimal(
            csv_entry_row[DRAFTKINGS_ENTRY_FEE_COLUMN]
        ),
        winnings=_convert_currency_to_decimal(csv_entry_row[DRAFTKINGS_WINNINGS_COLUMN]),
    )


def _convert_currency_to_decimal(currency_val):
    return Decimal(sub(r"[^\d.]", "", currency_val))
