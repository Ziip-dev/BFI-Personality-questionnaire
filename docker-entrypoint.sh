#!/bin/sh

set -eu

# activate virtual environment
source /opt/pysetup/.venv/bin/activate

# setup logic
# flask db upgrade

# Evaluating passed command:
# flask run --host=0.0.0.0
# gunicorn --config ./gunicorn_app/conf/gunicorn_config.py gunicorn_app:app
# gunicorn -b :5000 --access-logfile - --error-logfile - myapp:app
gunicorn -b :5001 wsgi
exec "$@"
