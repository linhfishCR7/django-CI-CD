release: python manage.py makemigrations --noinput && python manage.py migrate --noinput
web: gunicorn api.wsgi --log-file -