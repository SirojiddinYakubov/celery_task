FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y netcat vim

WORKDIR /code

COPY deploy/requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code
COPY deploy/entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]

