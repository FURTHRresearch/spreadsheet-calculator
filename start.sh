#!/bin/sh

pipenv run gunicorn app:app -k gevent