import logging

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError


from football_api.database import db
from football_api.models.season import Season
from football_api.schemas.season_schema import SeasonSchema


SEASONS_ENDPOINT = "/api/seasons"
logger = logging.getLogger(__name__)


class SeasonsResource(Resource):
    def get(self):
        """
        SeasonsResource GET method. Returns all seasons
        found in the Football Stats database.

        :return: List of seasons, 200 HTTP status code
        """
        logger.info("Retrieving all seasons.")

        seasons = Season.query.all()
        seasons_json = [SeasonSchema().dump(season) for season in seasons]

        logger.info("All seasons retrieved from database.")
        return seasons_json, 200

    def post(self):
        """
        SeasonsResource POST method. Adds a new season to the database.

        :return: Season ID (year), 201 HTTP status code
        """
        logger.info(f"Adding new season {request.data}.")
        season = SeasonSchema().load(request.get_json())

        try:
            db.session.add(season)
            db.session.commit()
        except IntegrityError as e:
            logger.warning(
                f"Integrity Error, this season is already in the database. Error: {e}."
            )

            abort(500, message="Unexpected Error!")
        else:
            logger.info(f"Successfully added new season: {season}.")
            return season.year, 201
