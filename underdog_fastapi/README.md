#### Intro to FastAPI - Create a Best Ball Projections API using FastAPI, SQLAlchemy and Pandas
---

This is the source-code for my [Intro to FastAPI - Create a Best Ball Projections API using FastAPI, SQLAlchemy and Pandas](https://ericbernier.com/intro-fast-api) blog post. This post assumes you have [Python 3 installed](https://realpython.com/installing-python/), as well as [pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv). Please read the post for further details.

To start the FastAPI application simply execute the following from the command line once all dependencies are installed and you have started your virtualenv via pipenv:
```bash
$ uvicorn underdog_fastapi.api.main:app --reload
```