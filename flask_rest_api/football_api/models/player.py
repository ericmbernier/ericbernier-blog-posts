from football_api.database import db


class Player(db.Model):
    """
    Player Flask-SQLAlchemy Model

    Represents objects contained in the players table
    """

    __tablename__ = "players"

    player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    position = db.Column(db.String(), nullable=False)

    stats = db.relationship("Stats", back_populates="player")

    def __repr__(self):
        return (
            f"**Player** "
            f"player_id: {self.player_id} "
            f"name: {self.name} "
            f"position: {self.position}"
            f"**Player** "
        )
