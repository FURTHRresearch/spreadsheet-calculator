# syntax=docker/dockerfile:1

FROM python:3.11-slim

WORKDIR /app

RUN apt-get -y update
RUN apt-get -y install libstdc++6 libcurl3-gnutls libc6 libxml2 libcurl4 fonts-dejavu fonts-opensymbol
RUN apt-get -y install fonts-liberation fonts-crosextra-carlito

ADD https://download.onlyoffice.com/install/desktop/docbuilder/linux/onlyoffice-documentbuilder_amd64.deb docbuilder.deb
RUN dpkg -i docbuilder.deb

COPY Pipfile ./
RUN pip install pipenv
RUN pipenv install
RUN pipenv update

COPY . .

CMD ["sh","start.sh"]