import logging

from celery import states
from celery.exceptions import Ignore
import requests

from flask_celery_redis.celery.celery_app import celery_app


logger = logging.getLogger(__name__)
POKEMON_GET_SPRITE_TASK = "download_pokemon_sprite_task"


@celery_app.task(name=POKEMON_GET_SPRITE_TASK, bind=True)
def download_pokemon_sprite_task(self, pokemon_name):
    logger.info(
        f"Attempting to download sprite from PokeAPI. pokemon_name:{pokemon_name}"
    )
    pokeapi_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    logger.info(f"PokeAPI response received. Response: {pokeapi_response.status_code}")

    if not pokeapi_response.ok:
        logger.warning(f"Updating Celery task to FAILED state!")

        self.update_state(
            state=states.FAILURE,
            meta=f"PokeAPI response not OK. Status Code: {pokeapi_response.status_code}",
        )

        raise Exception("Pokemon not found!")

    pokemon_json = pokeapi_response.json()
    pokemon_sprites = pokemon_json.get("sprites")
    pokemon_sprite_url = pokemon_sprites.get("front_default")

    with open(f"flask_celery_redis/static/pokemon/{pokemon_name}.png", "wb") as f:
        f.write(requests.get(pokemon_sprite_url).content)
