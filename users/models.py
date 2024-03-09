from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=35,
        verbose_name='телефон',
        blank=True, null=True)
    telegram = models.CharField(
        max_length=100,
        verbose_name='телеграмм',
        blank=True, null=True)
    avatar = models.ImageField(
        upload_to='users/',
        verbose_name='Аватар',
        blank=True,
        null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'
