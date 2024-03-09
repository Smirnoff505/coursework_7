from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitUpdateAPIView,
                          HabitDetailAPIView, HabitListAPIView,
                          HabitDeleteAPIView, HabitPublishedListAPIView,
                          ChangePublicHabitAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    # habit
    path('create/', HabitCreateAPIView.as_view(), name='create'),
    path('list/', HabitListAPIView.as_view(), name='list'),
    path('<int:pk>/update/', HabitUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/detail/', HabitDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/delete/', HabitDeleteAPIView.as_view(), name='delete'),
    path('habits/list/', HabitPublishedListAPIView.as_view(),
         name='habits-list-published'),
    path('habits/<int:pk>/change/', ChangePublicHabitAPIView.as_view(),
         name='habits-change-status'),

]
