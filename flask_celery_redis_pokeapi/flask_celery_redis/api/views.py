from flask import render_template, Blueprint


views_blueprint = Blueprint("views", __name__)


@views_blueprint.get("/")
def home():
    return render_template("index.html")
