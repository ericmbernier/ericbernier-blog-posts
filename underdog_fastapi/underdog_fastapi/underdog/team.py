from enum import Enum


class Team(Enum):
    ARI = "ARI"
    ATL = "ATL"
    BAL = "BAL"
    BUF = "BUF"
    CAR = "CAR"
    CHI = "CHI"
    CIN = "CIN"
    CLE = "CLE"
    DAL = "DAL"
    DEN = "DEN"
    DET = "DET"
    GB = "GB"
    HOU = "HOU"
    IND = "IND"
    JAX = "JAX"
    KC = "KC"
    LV = "LV"
    LAC = "LAC"
    LAR = "LAR"
    MIA = "MIA"
    MIN = "MIN"
    NE = "NE"
    NO = "NO"
    NYG = "NYG"
    NYJ = "NYJ"
    PHI = "PHI"
    PIT = "PIT"
    SF = "SF"
    SEA = "SEA"
    TB = "TB"
    TEN = "TEN"
    WAS = "WAS"


TEAM_NAME_TO_ABBREV = {
    "Arizona Cardinals": Team.ARI.name,
    "Atlanta Falcons": Team.ATL.name,
    "Baltimore Ravens": Team.BAL.name,
    "Buffalo Bills": Team.BUF.name,
    "Carolina Panthers": Team.CAR.name,
    "Chicago Bears": Team.CHI.name,
    "Cincinnati Bengals": Team.CIN.name,
    "Cleveland Browns": Team.CLE.name,
    "Dallas Cowboys": Team.DAL.name,
    "Denver Broncos": Team.DEN.name,
    "Detroit Lions": Team.DET.name,
    "Green Bay Packers": Team.GB.name,
    "Houston Texans": Team.HOU.name,
    "Indianapolis Colts": Team.IND.name,
    "Jacksonville Jaguars": Team.JAX.name,
    "Kansas City Chiefs": Team.KC.name,
    "Las Vegas Raiders": Team.LV.name,
    "Los Angeles Chargers": Team.LAC.name,
    "Los Angeles Rams": Team.LAR.name,
    "Miami Dolphins": Team.MIA.name,
    "Minnesota Vikings": Team.MIN.name,
    "New England Patriots": Team.NE.name,
    "New Orleans Saints": Team.NO.name,
    "NY Giants": Team.NYG.name,
    "NY Jets": Team.NYJ.name,
    "Philadelphia Eagles": Team.PHI.name,
    "Pittsburgh Steelers": Team.PIT.name,
    "San Francisco 49ers": Team.SF.name,
    "Seattle Seahawks": Team.SEA.name,
    "Tampa Bay Buccaneers": Team.TB.name,
    "Tennessee Titans": Team.TEN.name,
    "Washington Football Team": Team.WAS.name,
}
