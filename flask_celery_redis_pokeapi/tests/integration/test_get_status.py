def test_get_status(client):
    response = client.get("/celery/task/status/123")
    assert response.status_code == 200
