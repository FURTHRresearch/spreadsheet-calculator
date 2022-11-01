# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /app

COPY Pipfile ./
RUN pip install pipenv
RUN pipenv install
RUN pipenv update

COPY . .

CMD ["sh","start.sh"]