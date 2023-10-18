FROM python:3.10.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./Docker/Django_WSGI/requirements.txt /app
COPY ./app /app

RUN pip install -r requirements.txt
