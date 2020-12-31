import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from flask import Flask
from flask_restful import Api

from football_api.constants import PROJECT_ROOT, FANTASY_FOOTBALL_DATABASE
from football_api.database import db
from football_api.resources.players_resource import PlayersResource, PLAYERS_ENDPOINT
from football_api.resources.seasons_resource import SeasonsResource, SEASONS_ENDPOINT
from football_api.resources.stats_resources import (
    StatsResource,
    StatsPlayerResource,
    StatsSeasonResource,
    STATS_ENDPOINT,
    STATS_PLAYER_ENDPOINT,
    STATS_SEASON_ENDPOINT,
)
from football_api.resources.teams_resource import TeamsResource, TEAMS_ENDPOINT


def create_app(db_location):
    """
    Function that creates our Flask application.
    This function creates the Flask app, Flask-Restful API,
    and Flask-SQLAlchemy connection

    :param db_location: Connection string to the database
    :return: Initialized Flask app
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("football_api.log"), logging.StreamHandler()],
    )

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    db.init_app(app)

    api = Api(app)
    api.add_resource(PlayersResource, PLAYERS_ENDPOINT, f"{PLAYERS_ENDPOINT}/<id>")
    api.add_resource(SeasonsResource, SEASONS_ENDPOINT)
    api.add_resource(StatsResource, STATS_ENDPOINT)
    api.add_resource(StatsPlayerResource, STATS_PLAYER_ENDPOINT)
    api.add_resource(StatsSeasonResource, STATS_SEASON_ENDPOINT)
    api.add_resource(TeamsResource, TEAMS_ENDPOINT, f"{TEAMS_ENDPOINT}/<id>")
    return app


if __name__ == "__main__":
    app = create_app(f"sqlite:////{PROJECT_ROOT}/{FANTASY_FOOTBALL_DATABASE}")
    app.run(debug=True)
