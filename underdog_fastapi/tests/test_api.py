from fastapi.testclient import TestClient

from underdog_fastapi.api.main import app
from underdog_fastapi.underdog.team import TEAM_NAME_TO_ABBREV

client = TestClient(app)


def test_get_player():
    response = client.get("/api/players/1")
    assert response.status_code == 200


def test_get_players_by_team():
    response = client.get("/api/players/teams/ARI")
    assert response.status_code == 200


def test_get_player_stack():
    for team in TEAM_NAME_TO_ABBREV.values():
        response = client.get(f"/api/stacks/{team}")
        assert response.status_code == 200


def test_get_all_player_stacks():
    response = client.get("/api/stacks")
    assert response.status_code == 200
