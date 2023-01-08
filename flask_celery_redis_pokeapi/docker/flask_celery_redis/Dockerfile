FROM python:3.11-slim-buster

ENV INSTALL_PATH /flask_celery_redis
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

ADD Pipfile .
RUN mkdir -p .venv

RUN pip install pipenv==2022.11.30
RUN pipenv lock --dev && pipenv requirements --dev > requirements.txt
RUN pip install -r requirements.txt

COPY . .