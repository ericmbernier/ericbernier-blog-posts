from flask import Blueprint

hello_world_blueprint = Blueprint('hello_world', __name__)


@hello_world_blueprint.get("/")
def hello():
    """
    Renders a string to the user's screen

    :return: Flask response
    """
    return 'Hello there!'
