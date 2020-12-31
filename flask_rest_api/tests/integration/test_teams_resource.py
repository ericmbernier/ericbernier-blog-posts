from football_api.resources.teams_resource import TEAMS_ENDPOINT


def test_teams_post(client):
    new_team_json = {"name": "Houston Oilers", "abbreviation": "HOU"}
    response = client.post(TEAMS_ENDPOINT, json=new_team_json)
    assert response.status_code == 201


def test_teams_post_error(client):
    duplicate_team_json = {"name": "Seattle Seahawks", "abbreviation": "SEA"}
    response = client.post(TEAMS_ENDPOINT, json=duplicate_team_json)
    assert response.status_code == 500


def test_get_all_teams(client):
    response = client.get(TEAMS_ENDPOINT)

    assert response.status_code == 200
    assert len(response.json) > 1


def test_get_single_team(client):
    response = client.get(f"{TEAMS_ENDPOINT}/1")

    assert response.status_code == 200
    assert response.json["abbreviation"] == "CAR"


def test_get_team_not_found(client):
    response = client.get(f"{TEAMS_ENDPOINT}/99")
    assert response.status_code == 404
