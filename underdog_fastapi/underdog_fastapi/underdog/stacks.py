import logging
import statistics

from underdog_fastapi.api.schemas import PlayerBase, PlayerStack

PLAYER_POINT_CUTOFF = 100.0
NUM_GAMES = 17
logger = logging.getLogger(__name__)


def generate_player_stack(db_players):
    players = []
    logger.debug(f"Building player stack for {len(db_players)} players.")

    for db_player in db_players:
        if db_player.adp and _valid_projected_points(db_player.projected_points):
            player = {
                "first_name": db_player.first_name,
                "last_name": db_player.last_name,
                "adp": db_player.adp,
                "projected_points": db_player.projected_points,
                "team_name": db_player.team_name,
                "team_abbreviation": db_player.team_abbreviation,
            }

            players.append(PlayerBase(**player))

    player_adps = [player.adp for player in players]
    average_adp = statistics.mean(player_adps)
    median_adp = statistics.median(player_adps)
    projected_points_per_weak = (
        sum(player.projected_points for player in players) / NUM_GAMES
    )

    player_stack = {
        "players": players,
        "average_adp": average_adp,
        "median_adp": median_adp,
        "projected_points_per_week": projected_points_per_weak,
    }

    logger.info("Successfully built player stack.")
    return PlayerStack(**player_stack)


def _valid_projected_points(projected_points):
    if projected_points and projected_points >= PLAYER_POINT_CUTOFF:
        return True

    return False
