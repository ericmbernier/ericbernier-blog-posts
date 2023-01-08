def test_download_pokemon_sprite(client):
    response = client.get("/pokemon/charizard")
    assert response.status_code == 202
