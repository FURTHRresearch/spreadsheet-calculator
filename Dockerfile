# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /app

RUN apt-get install libstdc++6 libcurl3-gnutls libc6 libxml2 libcurl3 fonts-dejavu fonts-opensymbol
RUN apt-get install fonts-liberation ttf-mscorefonts-installer fonts-crosextra-carlito

ADD https://download.onlyoffice.com/install/desktop/docbuilder/documentbuilder-x64.tar.gz documentbuilder.tar.gz
RUN documentbuilder
RUN tar -zxvf documentbuilder.tar.gz -C documentbuilder --strip-components=1
ENV PATH="${PATH}:/app/documentbuilder"

COPY Pipfile ./
RUN pip install pipenv
RUN pipenv install
RUN pipenv update

COPY . .

CMD ["sh","start.sh"]