from football_api.database import db


class Team(db.Model):
    """
    Team Flask-SQLAlchemy Model

    Represents objects contained in the teams table
    """

    __tablename__ = "teams"

    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    abbreviation = db.Column(db.String(), unique=True, nullable=False)

    stats = db.relationship("Stats", back_populates="team")

    def __repr__(self):
        return (
            f"**Team** "
            f"team_id: {self.team_id} "
            f"name: {self.name} "
            f"abbreviation: {self.abbreviation}"
            f"**Team** "
        )
