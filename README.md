# Полезные привычки!

## Установка зависимостей

Для корректной работы программы необходимо установить:

`python = "^3.10"`

`django = "4.2"`

`pillow = "^10.2.0"`

`psycopg2-binary = "^2.9.9"`

`djangorestframework = "^3.14.0"`

`python-dotenv = "^1.0.1"`

`django-cors-headers = "^4.3.1"`

`djangorestframework-simplejwt = "^5.3.1"`

`coverage = "^7.4.3"`

`flake8 = "^7.0.0"`

`flake8-html = "^0.4.3"`

`drf-yasg = "^1.21.7"`

`celery = "^5.3.6"`

`django-celery-beat = "^2.6.0"`

`redis = "^5.0.2"`

`requests = "^2.31.0"`

## Миграции

Перед запуском приложения выполните миграции

`python manage.py migrate`

## Создание суперпользователя

Чтобы создать суперпользователя, выполните следующую команду: 

`python manage.py createsu`

## Проверка кода с помощью Flake8

`flake8 --max-line-length 120 --exclude=*/migrations/*`

## Покрытие тестами

Для формирования отчета покрытия тестами используйте следующие команды:

`coverage run --source='.' manage.py test`

`coverage report`

## Запуск Celery

Чтобы запустить Celery worker и Celery beat, используйте следующую команду:

`celery -A config worker --loglevel=info -S django -B`

## Заполнение файла .env

Заполните файл `.env` согласно примеру заполнения `env.simple`.
