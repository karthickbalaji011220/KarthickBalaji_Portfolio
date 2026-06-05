#!/usr/bin/env bash
set -o errexit   # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Auto-create superuser on first deploy using env vars
# Set DJANGO_SUPERUSER_* in Render environment variables
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    python manage.py createsuperuser \
        --noinput \
        --username "$DJANGO_SUPERUSER_USERNAME" \
        --email "$DJANGO_SUPERUSER_EMAIL" \
    2>/dev/null || echo "Superuser already exists, skipping."
fi

echo "Build complete."
