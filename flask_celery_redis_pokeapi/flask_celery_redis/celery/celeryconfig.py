DOWNLOAD_POKEMON_SPRITE_QUEUE = "download_pokemon_sprite_queue"


broker_url = "redis://redis:6379/0"
imports = ["flask_celery_redis.celery.tasks.download_pokemon_sprite"]
result_backend = "db+sqlite:///results.db"
task_default_queue = DOWNLOAD_POKEMON_SPRITE_QUEUE
