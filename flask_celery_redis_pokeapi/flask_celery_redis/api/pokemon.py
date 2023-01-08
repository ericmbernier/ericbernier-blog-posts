import logging

from flask import Blueprint, send_file, jsonify
from flask_celery_redis.celery.tasks.download_pokemon_sprite import (
    download_pokemon_sprite_task,
)

logger = logging.getLogger(__name__)
pokemon_blueprint = Blueprint("pokemon", __name__)


@pokemon_blueprint.get("/pokemon/<pokemon_name>")
def download_pokemon_sprite(pokemon_name):
    """
    Goes out to the third-party PokeAPI and downloads a sprite

    :param str pokemon_name: Name of the pokemon to download the sprite for
    :return: Task Id working on sprite retrieval, 202 status code
    """
    task = download_pokemon_sprite_task.delay(pokemon_name)
    logger.info(f"Celery task created! Task ID: {task!r}")

    return jsonify({"taskId": task.id}), 202
