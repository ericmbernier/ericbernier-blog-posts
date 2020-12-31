import logging

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from football_api.database import db
from football_api.models.player import Player
from football_api.schemas.player_schema import PlayerSchema


PLAYERS_ENDPOINT = "/api/players"
logger = logging.getLogger(__name__)


class PlayersResource(Resource):
    def get(self, id=None):
        """
        PlayersResource GET method. Retrieves all players found in the Football
        Stats database, unless the id path parameter is provided. If this id
        is provided then the player with the associated player_id is retrieved.

        :param id: Player ID to retrieve, this path parameter is optional
        :return: Player, 200 HTTP status code
        """
        if not id:
            position = request.args.get("position")
            logger.info(
                f"Retrieving all players, optionally filtered by position={position}"
            )

            return self._get_all_players(position), 200

        logger.info(f"Retrieving player by id {id}")

        try:
            return self._get_player_by_id(id), 200
        except NoResultFound:
            abort(404, message="Player not found")

    def _get_player_by_id(self, player_id):
        player = Player.query.filter_by(player_id=player_id).first()
        player_json = PlayerSchema().dump(player)

        if not player_json:
            raise NoResultFound()

        logger.info(f"Player retrieved from database {player_json}")
        return player_json

    def _get_all_players(self, position):
        if position:
            players = Player.query.filter_by(position=position).all()
        else:
            players = Player.query.all()

        players_json = [PlayerSchema().dump(player) for player in players]

        logger.info("Players successfully retrieved.")
        return players_json

    def post(self):
        """
        PlayersResource POST method. Adds a new Player to the database.

        :return: Player.player_id, 201 HTTP status code.
        """
        player = PlayerSchema().load(request.get_json())

        try:
            db.session.add(player)
            db.session.commit()
        except IntegrityError as e:
            logger.warning(
                f"Integrity Error, this team is already in the database. Error: {e}"
            )

            abort(500, message="Unexpected Error!")
        else:
            return player.player_id, 201
