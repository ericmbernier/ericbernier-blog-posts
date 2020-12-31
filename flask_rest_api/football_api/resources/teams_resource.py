import logging

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from football_api.database import db
from football_api.models.team import Team
from football_api.schemas.team_schema import TeamSchema


logger = logging.getLogger(__name__)


TEAMS_ENDPOINT = "/api/teams"


class TeamsResource(Resource):
    def get(self, id=None):
        """
        TeamsResource GET method. Returns all teams found in the Football Stats
        database, unless the id path parameter is provided. If this id is
        provided then the team with the associated team_id is retrieved.

        :param id: Team ID to retrieve, this path parameter is optional
        :return: Team, 200 HTTP status code
        """
        if not id:
            logger.info("Retrieving all teams.")
            return self._get_all_teams(), 200

        logger.info(f"Retrieving team by id {id}.")

        try:
            return self._get_team_by_id(id), 200
        except NoResultFound:
            abort(404, message="Team not found.")

    def _get_all_teams(self):
        teams = Team.query.all()
        teams_json = [TeamSchema().dump(team) for team in teams]

        logger.info("All teams successfully retrieved.")
        return teams_json

    def _get_team_by_id(self, id):
        team = Team.query.filter_by(team_id=id).first()
        team_json = TeamSchema().dump(team)

        if not team_json:
            logger.warning(f"No team found, team_id={id}.")
            raise NoResultFound()

        logger.info(f"Team successfully retrieved from database {team_json}.")
        return team_json

    def post(self):
        """
        TeamsResource POST method. Adds a new Team to the database.

        :return: Team.team_id, 201 HTTP status code.
        """
        logger.info(f"Adding new team {request.data}")
        team = TeamSchema().load(request.get_json())

        try:
            db.session.add(team)
            db.session.commit()
        except IntegrityError as e:
            logger.warning(
                f"Integrity Error, this team is already in the database. Error: {e}."
            )

            abort(500, message="Unexpected Error!")
        else:
            logger.info(f"Successfully added new team {team}.")
            return team.team_id, 201
