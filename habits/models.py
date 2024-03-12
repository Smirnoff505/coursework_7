from datetime import timedelta

from django.db import models

from config import settings


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              verbose_name='Пользователь',
                              related_name='owner',
                              null=True,
                              blank=True
                              )
    title = models.CharField(max_length=255,
                             verbose_name='Название привычки')
    place_of_execution = models.CharField(max_length=255,
                                          verbose_name='Место выполнения')
    time_execution = models.TimeField(
        verbose_name='Время начала выполнения привычки')
    action = models.TextField(verbose_name='Действие')
    is_pleasant_habit = models.BooleanField(
        default=False,
        blank=True,
        verbose_name='Признак приятной привычки')

    accompanying_habit = models.ForeignKey('self',
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           blank=True,
                                           verbose_name='Связанная привычка')
    periodicity = models.PositiveSmallIntegerField(default=1,
                                                   verbose_name='Периодичность')
    award = models.TextField(null=True,
                             blank=True,
                             verbose_name='Вознаграждение')
    time_to_complete = models.DurationField(
        default=timedelta(seconds=120),
        blank=True,
        verbose_name='Время на выполнение')
    is_publish = models.BooleanField(default=False,
                                     verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.owner} - {self.title}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
