FROM python:3.10.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./Docker/Django_WSGI/requirements.txt /app
COPY ./open_pycab /app

RUN pip install -r requirements.txt
