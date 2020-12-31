from football_api.resources.seasons_resource import SEASONS_ENDPOINT


def test_seasons_post(client):
    new_season_json = {"year": 2016}
    response = client.post(f"{SEASONS_ENDPOINT}", json=new_season_json)
    assert response.status_code == 201


def test_seasons_post_error(client):
    new_season_json = {"year": 2018}
    response = client.post(f"{SEASONS_ENDPOINT}", json=new_season_json)
    assert response.status_code == 500


def test_seasons_get(client):
    response = client.get(f"{SEASONS_ENDPOINT}")
    assert response.status_code == 200
