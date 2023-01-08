#### Flask and Asynchronous Tasks with Celery and Redis

This is the Dockerized Flask application project for my [Flask and Asynchronous Tasks with Celery and Redis](https://ericbernier.com/flask-celery-redis) blog post. This post assumes you have [Docker](https://docs.docker.com/engine/install/) installed. Please read the post for further details.

Build all services:
```bash
docker-compose build
```

Start all serivces:
```bash
docker-compose up
```

Stop all serivces:
```bash
docker-compose stop
```

Once everything is up and running navigate to `http://127.0.0.1:8000 to test out the application in a browser!
