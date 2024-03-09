from datetime import timedelta

from celery import shared_task
from django_celery_beat.utils import now

from habits.models import Habit
from habits.services import my_bot_send_message


@shared_task
def check_time_execution():
    """Отложенная задача для отправки сообщения в телеграм за 10 минут до начала события"""
    time_item = now() + timedelta(minutes=10)
    time_plus_ten_minutes = time_item.time().replace(second=0, microsecond=0)
    habits = Habit.objects.all()
    for habit in habits:
        if habit.time_execution.replace(second=0) == time_plus_ten_minutes:
            my_bot_send_message(habit.owner.telegram, habit.title)
