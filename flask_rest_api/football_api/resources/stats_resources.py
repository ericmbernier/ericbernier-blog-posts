import logging

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError

from football_api.database import db
from football_api.models.stats import Stats
from football_api.schemas.stats_schema import StatsSchema


STATS_ENDPOINT = "/api/stats"
STATS_PLAYER_ENDPOINT = f"{STATS_ENDPOINT}/player/<player_id>"
STATS_SEASON_ENDPOINT = f"{STATS_ENDPOINT}/season/<season>"

logger = logging.getLogger(__name__)


class StatsResource(Resource):
    def get(self):
        logger.info("Retrieving all stats.")
        stats = Stats.query.all()

        logger.info("All stats retrieved from database.")
        return _dump_stats(stats), 200

    def post(self):
        """
        StatsResource POST method. Adds a new Object to the database.

        :return: Stats.stat_id, 201 HTTP status code.
        """
        logger.info(f"Adding new stats {request.data}.")
        stats = StatsSchema().load(request.get_json())

        try:
            db.session.add(stats)
            db.session.commit()
        except IntegrityError as e:
            logger.warning(
                f"Integrity Error, this  is already in the database. Error: {e}."
            )

            abort(500, message="Unexpected Error!")
        else:
            logger.info(f"Successfully added new stats: {stats}.")
            return stats.stat_id, 201


class StatsPlayerResource(Resource):
    def get(self, player_id):
        """
        StatsPlayerResource GET method

        Retrieves stats for an individual player, for a provided player_id

        :param player_id: Path parameter, id of the player
        :return: Player Stats
        """
        logger.info(f"Retrieving stats for individual player, player_id={player_id}.")

        player_stats = Stats.query.filter_by(player_id=player_id).all()
        if not player_stats:
            logger.warning(f"No stats found for player, player_id={player_id}")
            abort(404, message="Player not found")

        return _dump_stats(player_stats), 200


class StatsSeasonResource(Resource):
    def get(self, season):
        """
        StatsSeasonResource GET method

        Retrieves all stats for a given Season

        :param season: Path parameter, season to get stats for
        :return: List of Stats for Season
        """
        logger.info(f"Retrieving stats for entire season={season}")

        season_stats = Stats.query.filter_by(season=season).all()
        if not season_stats:
            logger.warning(f"No stats found for season, season={season}.")
            abort(404, message="Season not found.")

        return _dump_stats(season_stats), 200


def _dump_stats(retrieved_stats):
    return [
        StatsSchema(exclude=["player_id", "team_id"]).dump(stats)
        for stats in retrieved_stats
    ]
