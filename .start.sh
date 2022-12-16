#!/bin/bash
# source venv/bin/activate
# export FLASK_APP=app
# EXPORT FLASK_ENV=development
# flask run
gunicorn -w 4 'wsgi:app' --access-logfile=access.log --log-file=errors.log

# deactivate