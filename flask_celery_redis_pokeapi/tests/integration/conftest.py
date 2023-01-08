import pytest
from flask_celery_redis.app import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client
