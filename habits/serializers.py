from rest_framework import serializers

from habits.models import Habit
from habits.validators import (PeriodicityValidator,
                               TimeToCompleteValidator,
                               AccompanyingOrAwardValidator,
                               IsPleasantHabitValidator)


class HabitSerializer(serializers.ModelSerializer):
    is_pleasant_habit = serializers.BooleanField(required=False)
    time_to_complete = serializers.DurationField(required=False)

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [PeriodicityValidator(field='periodicity'),
                      TimeToCompleteValidator(field='time_to_complete'),
                      AccompanyingOrAwardValidator(field1='accompanying_habit',
                                                   field2='award'),
                      IsPleasantHabitValidator(), ]


class HabitPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('title', 'place_of_execution', 'action',)
