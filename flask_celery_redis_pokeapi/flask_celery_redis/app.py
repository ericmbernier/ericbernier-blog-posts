import logging

from flask import Flask

from flask_celery_redis.api.celery_status import celery_task_status_blueprint
from flask_celery_redis.api.pokemon import pokemon_blueprint
from flask_celery_redis.api.views import views_blueprint


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[
            logging.FileHandler("flask_celery_redis_api.log"),
            logging.StreamHandler(),
        ],
    )

    app = Flask(
        __name__,
        instance_relative_config=True,
    )

    app.config.from_pyfile("settings.py", silent=True)
    app.jinja_env.auto_reload = True

    app.register_blueprint(celery_task_status_blueprint)
    app.register_blueprint(views_blueprint)
    app.register_blueprint(pokemon_blueprint)

    return app
