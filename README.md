# README celery_task #

# This is Celery Task Project

### How to install this project ###

* create deploy/.env file
* copy deploy/env.md to deploy/.env
* python -m venv venv
* source venv/bin/activate
* pip install poetry
* poetry install
* python manage.py runserver

### start celery and flower monitoring ###
* celery -A conf worker -l INFO --detach
* celery -A conf beat -l INFO --detach
* celery -A conf flower

### create task http://127.0.0.1:8000/api/v1/task/message/create/
### open flower http://127.0.0.1:5555 ###


