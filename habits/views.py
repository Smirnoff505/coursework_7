from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from habits.models import Habit
from habits.pagination import ListPagination
from habits.permissions import IsOwner, ReadOnly
from habits.serializers import HabitSerializer, HabitPublicSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        owner = self.request.user
        serializer.save(owner=owner)


class HabitListAPIView(generics.ListAPIView):
    """Просмотр всех привычек пользователя"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = ListPagination

    def get_queryset(self):
        """Получаем отсортированные по владельцу привычки"""
        return Habit.objects.filter(owner=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Обновление привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDetailAPIView(generics.RetrieveAPIView):
    """Просмотр отдельной привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitPublishedListAPIView(generics.ListAPIView):
    """Просмотр всех опубликованных привычек"""
    serializer_class = HabitPublicSerializer
    permission_classes = [IsAuthenticated, ReadOnly]
    pagination_class = ListPagination

    def get_queryset(self):
        return Habit.objects.filter(is_publish=True)


class ChangePublicHabitAPIView(APIView):
    """Переключение статуса привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    @swagger_auto_schema(
        responses={200: openapi.Response(
            description="Привычка опубликована или снята с публикации",
            examples={
                "application/json": {
                    "message": 'Привычка опубликована',
                }
            }
        )
        }
    )
    def post(self, *args, **kwargs):
        user = self.request.user
        # достаем из переданного адеса pk
        habit_id = kwargs.get('pk')
        # получаем объект или ошибку, фильтруем по полям id и owner
        habit = get_object_or_404(Habit, pk=habit_id, owner=user)

        # Переключение статуса публикации
        habit.is_publish = not habit.is_publish
        habit.save()

        message = 'Привычка снята с публикации' if habit.is_publish \
            else 'Привычка опубликована'

        return Response({"message": message})
