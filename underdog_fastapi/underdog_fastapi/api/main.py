import logging
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from underdog_fastapi.api import crud, models, schemas
from underdog_fastapi.database import engine, get_db, create_database
from underdog_fastapi.underdog.team import Team

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[logging.FileHandler("football_api.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)
create_database()
app = FastAPI()


@app.get("/players/{player_id}", response_model=schemas.Player)
def get_player(player_id: int, db: Session = Depends(get_db)):
    logger.info(f"Retrieving player by id {id}.")
    player = crud.get_player(db, player_id=player_id)

    if player is None:
        logger.warning(f"Player not found by id {id}.")
        raise HTTPException(status_code=404, detail="Player not found.")

    logger.info(f"Successfully retrieved player by id {id}.")
    return player


@app.get("/players/teams/{team}", response_model=List[schemas.Player])
def get_player(team: str, db: Session = Depends(get_db)):
    logger.info(f"Retrieving players for team {team}.")
    players = crud.get_players_by_team(db, team=Team(team))

    if players is None:
        logger.warning(f"Players not found by team {team}.")
        raise HTTPException(status_code=404, detail="Players not found.")

    logger.info(f"Successfully retrieved players for team {team}.")
    return players


@app.get("/stacks/{team}", response_model=schemas.PlayerStack)
def get_player_stack(team: str, db: Session = Depends(get_db)):
    logger.info(f"Retrieving player stack for team {team}.")
    player_stack = crud.get_player_stack_by_team(db, team=Team(team))

    if player_stack is None:
        logger.warning(f"Player stack not found by team {team}.")
        raise HTTPException(
            status_code=404, detail=f"Player stack not found by team {team}"
        )

    logger.info(f"Successfully retrieved player stack for team {team}.")
    return player_stack


@app.get("/stacks/", response_model=List[schemas.PlayerStack])
def get_player_stack(db: Session = Depends(get_db)):
    logger.info(f"Retrieving all player stacks")
    player_stacks = crud.get_all_player_stacks(db)

    if player_stacks is None:
        logger.warning(f"Player stacks not retrieved.")
        raise HTTPException(status_code=500, detail=f"Internal server error.")

    logger.info(f"Successfully retrieved all player stacks.")
    return player_stacks
