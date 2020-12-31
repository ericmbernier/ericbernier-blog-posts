from shutil import copy


import pytest
from football_api.api import create_app
from football_api.constants import FANTASY_FOOTBALL_DATABASE, PROJECT_ROOT


@pytest.fixture
def client(tmpdir):
    copy(f"{PROJECT_ROOT}/{FANTASY_FOOTBALL_DATABASE}", tmpdir.dirpath())

    temp_db_file = f"sqlite:///{tmpdir.dirpath()}/{FANTASY_FOOTBALL_DATABASE}"

    app = create_app(temp_db_file)
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client
