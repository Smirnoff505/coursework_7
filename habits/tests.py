from datetime import time, timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            id=1,
            email='test@test.ru',
            password='test'

        )

        self.habit = Habit.objects.create(
            id=25,
            title='test1',
            time_execution=time(11, 30, 0),
            action='test1',
            is_pleasant_habit=True,
            accompanying_habit='test1',
            time_to_complete=timedelta(seconds=120),
            owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        """Тестирование создания привычки"""
        data = {
            'title': 'test',
            'place_of_execution': 'test',
            'time_execution': '21:30:00',
            'action': 'тест гулять',
            'is_pleasant_habit': True,
            'accompanying_habit': 'тест мыться',
            'time_to_complete': 75
        }
        response = self.client.post(
            reverse('habits:create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 1,
                'title': 'test',
                'place_of_execution': 'test',
                'time_execution': '21:30:00',
                'action': 'тест гулять',
                'is_pleasant_habit': True,
                'accompanying_habit': 'тест мыться',
                'periodicity': 1,
                'award': None,
                'time_to_complete': '00:01:15',
                'is_publish': False,
                'owner': self.user.pk
            }

        )

    def test_habit_detail(self):
        """Тестирование просмотра одной сущности"""

        response = self.client.get(
            reverse('habits:detail', kwargs={'pk': 25})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 25,
             'is_pleasant_habit': True,
             'title': 'test1',
             'place_of_execution': '',
             'time_execution': '11:30:00',
             'action': 'test1',
             'accompanying_habit': 'test1',
             'periodicity': 1,
             'award': None,
             'time_to_complete': '00:02:00',
             'is_publish': False,
             'owner': 1}

        )

    def test_habit_list(self):
        """Тестирование просмотра списка привычек"""

        response = self.client.get(
            reverse('habits:list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None,
             'results': [
                 {'id': 25,
                  'is_pleasant_habit': True,
                  'title': 'test1',
                  'place_of_execution': '',
                  'time_execution': '11:30:00',
                  'action': 'test1',
                  'accompanying_habit': 'test1',
                  'periodicity': 1,
                  'award': None,
                  'time_to_complete': '00:02:00',
                  'is_publish': False,
                  'owner': 1}
             ]
             }
        )

    def test_habit_update(self):
        """Тестирование внесения изменений в привычку"""

        data = {
            'id': 25,
            'title': 'test update'
        }

        response = self.client.patch(
            reverse('habits:update', kwargs={'pk': 25}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': 25,
                'is_pleasant_habit': True,
                'time_to_complete': '00:02:00',
                'title': 'test update',
                'place_of_execution': '',
                'time_execution': '11:30:00',
                'action': 'test1',
                'accompanying_habit': 'test1',
                'periodicity': 1,
                'award': None,
                'is_publish': False,
                'owner': 1
            }
        )

    def test_habit_delete(self):
        """Тестирование удаления привычки"""

        response = self.client.delete(
            reverse('habits:delete', kwargs={'pk': 25})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_habit_change_status(self):
        """Тестирование изменения статуса опубликовано/не опубликовано"""

        response = self.client.post(
            reverse('habits:habits-change-status', kwargs={'pk': 25})
        )

        self.assertEqual(
            response.json(),
            {
                'message': 'Привычка снята с публикации'
            }

        )

    def tearDown(self):
        pass
