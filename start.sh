#!/bin/sh

pipenv run gunicorn app:app -k gevent -b 0.0.0.0:5555