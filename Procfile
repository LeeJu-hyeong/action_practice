web: gunicorn pythonide.wsgi:application --log-file --log-level debug
web: gunicore --bind 0.0.0.0:8000 pythonide:app
python manage.py collectstatic --noinput
manage.py migrate
