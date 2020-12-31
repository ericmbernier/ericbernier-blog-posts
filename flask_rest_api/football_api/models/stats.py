from football_api.database import db


class Stats(db.Model):
    """
    Stats Flask-SQLAlchemy Model

    Represents objects contained in the stats table
    """

    stat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(
        db.Integer, db.ForeignKey("players.player_id"), nullable=False
    )
    season = db.Column(db.Integer, db.ForeignKey("seasons.year"), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.team_id"), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    games_started = db.Column(db.Integer, nullable=False)
    completions = db.Column(db.Integer)
    pass_attempts = db.Column(db.Integer)
    pass_yards = db.Column(db.Integer)
    pass_tds = db.Column(db.Integer)
    interceptions = db.Column(db.Integer)
    rush_attempts = db.Column(db.Integer)
    rush_yards = db.Column(db.Integer)
    rush_yards_per_attempt = db.Column(db.Float)
    rush_tds = db.Column(db.Integer)
    targets = db.Column(db.Integer)
    receptions = db.Column(db.Integer)
    rec_yards = db.Column(db.Integer)
    yards_per_reception = db.Column(db.Float)
    rec_tds = db.Column(db.Integer)
    fumbles = db.Column(db.Integer)
    fumbles_lost = db.Column(db.Integer)
    fantasy_points = db.Column(db.Float)

    player = db.relationship("Player", back_populates="stats")
    team = db.relationship("Team", back_populates="stats")

    def __repr__(self):
        return (
            f"**Stats** "
            f"stat_id: {self.stat_id} "
            f"player_id: {self.player_id} "
            f"season: {self.season} "
            f"team_id: {self.team_id} "
            f"age: {self.age} "
            f"games: {self.games} "
            f"games_started: {self.games_started} "
            f"completions: {self.completions} "
            f"pass_attempts: {self.pass_attempts} "
            f"pass_yards: {self.pass_yards} "
            f"pass_tds: {self.pass_tds} "
            f"interceptions: {self.interceptions} "
            f"rush_attempts: {self.rush_attempts} "
            f"rush_yards: {self.rush_yards} "
            f"rush_yards_per_attempt: {self.rush_yards_per_attempt} "
            f"rush_tds: {self.rush_tds} "
            f"targets: {self.targets} "
            f"receptions: {self.receptions} "
            f"rec_yards: {self.rec_yards} "
            f"yards_per_reception: {self.yards_per_reception} "
            f"rec_tds: {self.rec_tds} "
            f"fumbles: {self.fumbles} "
            f"fumbles_lost: {self.fumbles_lost} "
            f"fantasy_points: {self.fantasy_points} "
            f"**Stats** "
        )
