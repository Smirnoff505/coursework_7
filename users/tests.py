from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            id=10,
            email='admin@test.ru',
            password='test'

        )

        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """Тестирование создания пользователя"""

        data = {
            'email': 'test@test.ru',
            'password': 'test'
        }

        response = self.client.post(
            reverse('users:user-register'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'email': 'test@test.ru',
                'telegram': None
            }

        )

    def test_user_update(self):
        """Тестирование обновления пользователя"""

        data = {
            'telegram': '@telega'
        }

        response = self.client.patch(
            reverse('users:user-update', kwargs={'pk': 10}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': 10,
                'email': 'admin@test.ru',
                'telegram': '@telega'
            }

        )

    def test_user_profile(self):
        """Просмотр детальной информации о пользователе"""

        response = self.client.get(
            reverse('users:user-profile', kwargs={'pk': 10})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': 10,
                'first_name': '',
                'last_name': '',
                'email': 'admin@test.ru',
                'phone': None,
                'telegram': None,
                'avatar': None
            }

        )

    def tearDown(self):
        pass


class CommandsTestCase(APITestCase):
    def setUp(self):
        pass

    def test_createsu(self):
        """Тестирование создания superuser"""

        call_command('createsu')

        self.assertTrue(
            User.objects.all().exists
        )
