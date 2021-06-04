import logging

from sqlalchemy.orm import Session

from underdog_fastapi.api.models import Player
from underdog_fastapi.underdog.stacks import generate_player_stack
from underdog_fastapi.underdog.team import Team, TEAM_NAME_TO_ABBREV


logger = logging.getLogger(__name__)


def get_player(db: Session, player_id: int):
    logger.debug(f"Retrieving data for player_id {player_id}.")
    return db.query(Player).filter(Player.id == player_id).first()


def get_players_by_team(db: Session, team: Team):
    logger.debug(f"Retrieving data for team {team}.")
    return db.query(Player).filter(Player.team_abbreviation == team.name).all()


def get_player_stack_by_team(db: Session, team: Team):
    logger.debug(f"Retrieving player stack data for team {team}.")
    players = get_players_by_team(db, team)
    return generate_player_stack(players)


def get_all_player_stacks(db: Session):
    logger.debug("Retrieving all player stacks, sorted by projected points per week.")
    player_stacks = []

    for team_name in TEAM_NAME_TO_ABBREV.values():
        player_stack = get_player_stack_by_team(db, Team(team_name))
        player_stacks.append(player_stack)

    player_stacks.sort(key=lambda stack: stack.projected_points_per_week, reverse=True)

    logger.debug(
        "Successfully retrieved all player stacks, and sorted by projected points per week."
    )
    return player_stacks
