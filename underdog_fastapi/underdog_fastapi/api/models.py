from sqlalchemy import Column, Integer, Numeric, String

from underdog_fastapi.database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    first_name = Column(String)
    last_name = Column(String)
    adp = Column(Numeric)
    projected_points = Column(Numeric)
    position = Column(String)
    team_name = Column(String)
    team_abbreviation = Column(String)
