from flask import Flask

from flask_docker.api.hello_world import hello_world_blueprint


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_pyfile("settings.py", silent=True)
    app.register_blueprint(hello_world_blueprint)
    
    return app
