#!/bin/bash

source venv/bin/activate
python3 init_db.py
# export FLASK_APP=app
# EXPORT FLASK_ENV=development
# flask run
gunicorn -w 2 'wsgi:app' --access-logfile=access.log --log-file=errors.log

# deactivate