from football_api.resources.stats_resources import STATS_ENDPOINT


def test_get_all_stats(client):
    response = client.get(f"{STATS_ENDPOINT}")
    assert response.status_code == 200


def test_stats_post(client):
    new_stats_json = {
        "player_id": 3,
        "season": 2016,
        "team_id": 2,
        "age": 23,
        "games": 16,
        "games_started": 16,
        "completions": 308,
        "pass_attempts": 490,
        "pass_yards": 3324,
        "pass_tds": 22,
        "interceptions": 13,
        "rush_attempts": 57,
        "rush_yards": 357,
        "rush_yards_per_attempt": 6.3,
        "rush_tds": 6,
        "targets": 0,
        "receptions": 0,
        "rec_yards": 0,
        "yards_per_reception": 0.0,
        "rec_tds": 0,
        "fumbles": 4,
        "fumbles_lost": 3,
        "fantasy_points": 260.7,
    }
    response = client.post(f"{STATS_ENDPOINT}", json=new_stats_json)
    assert response.status_code == 201


def test_get_stats_for_player(client):
    response = client.get(f"{STATS_ENDPOINT}/player/3")
    stats_json = response.get_json()
    assert stats_json[0]["player"]["name"] == "Dak Prescott"


def test_get_stats_player_not_found(client):
    response = client.get(f"{STATS_ENDPOINT}/player/99")
    assert response.status_code == 404


def test_get_stats_for_season(client):
    response = client.get(f"{STATS_ENDPOINT}/season/2019")
    stats_json = response.get_json()

    for stats in stats_json:
        assert stats["season"] == 2019


def test_get_stats_season_not_found(client):
    response = client.get(f"{STATS_ENDPOINT}/season/99")
    assert response.status_code == 404
