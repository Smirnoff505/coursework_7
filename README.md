Полезные привычки!

Для корректной работы программы необходимо установить:
python = "^3.10"
django = "4.2"
pillow = "^10.2.0"
psycopg2-binary = "^2.9.9"
djangorestframework = "^3.14.0"
python-dotenv = "^1.0.1"
django-cors-headers = "^4.3.1"
djangorestframework-simplejwt = "^5.3.1"
coverage = "^7.4.3"
flake8 = "^7.0.0"
flake8-html = "^0.4.3"
drf-yasg = "^1.21.7"
celery = "^5.3.6"
django-celery-beat = "^2.6.0"
redis = "^5.0.2"
requests = "^2.31.0"

Выполнить миграции
Так же необходимо заполнить файл .env согласно примеру заполнения env.simple.

python manage.py createsu - создает суперпользователя.
flake8 --max-line-length 120 --exclude=*/migrations/* - команда проверки flake8 за исключением миграций.
coverage run --source='.' manage.py test - формирует отчет покрытия тестами.
coverage report - выводит отчет покрытия тестами.
celery -A config worker --loglevel=info -S django -B - запускает celery-worker и celery-beat.