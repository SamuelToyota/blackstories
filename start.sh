#!/usr/bin/env bash
set -o errexit

export DATA_DIR="${DATA_DIR:-/opt/render/project/src/data}"
export SQLITE_PATH="${SQLITE_PATH:-$DATA_DIR/db.sqlite3}"
export MEDIA_ROOT="${MEDIA_ROOT:-$DATA_DIR/media}"

mkdir -p "$DATA_DIR" "$MEDIA_ROOT"

if [ ! -f "$SQLITE_PATH" ] && [ -f "/opt/render/project/src/stories/seed.sqlite3" ]; then
    cp "/opt/render/project/src/stories/seed.sqlite3" "$SQLITE_PATH"
fi

if [ -d "/opt/render/project/src/media" ] && [ -z "$(find "$MEDIA_ROOT" -mindepth 1 -maxdepth 1 -print -quit 2>/dev/null)" ]; then
    cp -R /opt/render/project/src/media/. "$MEDIA_ROOT"/
fi

python manage.py migrate --no-input

if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
    python manage.py createsuperuser --no-input 2>/dev/null || true
fi

exec gunicorn black_stories.wsgi:application \
    --workers "${WEB_CONCURRENCY:-2}" \
    --threads 2 \
    --timeout 60 \
    --access-logfile - \
    --error-logfile -
