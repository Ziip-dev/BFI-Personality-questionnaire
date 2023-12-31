#!/bin/sh

set -eu

# activate virtual environment
source /opt/pysetup/.venv/bin/activate

# setup logic
# flask db upgrade

# Evaluating passed command:
# gunicorn --config ./gunicorn_config.py gunicorn_app:app
# gunicorn -b :5000 --access-logfile - --error-logfile - myapp:app
gunicorn -b :5001 wsgi \
    --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
exec "$@"
