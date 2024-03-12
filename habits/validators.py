import datetime

from rest_framework.serializers import ValidationError


class PeriodicityValidator:
    """Проверяет выбор периода от 1 до 7"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        my_lst = [1, 2, 3, 4, 5, 6, 7]
        item = dict(value).get(self.field)
        if item:
            if item not in my_lst:
                raise ValidationError('Диапазон выбора от 1 до 7')


class TimeToCompleteValidator:
    """Время на выполнение привычки """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        item = dict(value).get(self.field)
        if item is not None:
            if item > datetime.timedelta(seconds=120):
                raise ValidationError(
                    'Время выполнение не может быть больше 120 секунд'
                )


class AccompanyingOrAwardValidator:
    """Проверяет не заполнены поля связанной
    привычки и вознаграждения одновременно"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        field_accompany = dict(value).get(self.field1)
        field_award = dict(value).get(self.field2)
        field_is_pleasant_habit = value.get('is_pleasant_habit')

        if field_award is not None or field_accompany is not None:

            if field_award and field_accompany:
                raise ValidationError(
                    'Не должно быть заполнено одновременно и '
                    'поле вознаграждения, и поле связанной привычки'
                )
            elif field_award and field_is_pleasant_habit:
                raise ValidationError(
                    'При указании вознаграждения(award) нельзя указывать признак приятной привычки')

        elif not field_award and not field_accompany and field_is_pleasant_habit:
            raise ValidationError(
                'При включенном признаке приятной привычки необходимо заполнить поле - Связанная привычка'
            )


class IsPleasantHabitValidator:

    def __call__(self, value):
        field_is_pleasant = dict(value).get('is_pleasant_habit')
        field_accompany = dict(value).get('accompanying_habit')
        if (field_is_pleasant
                is not True and field_accompany):
            raise ValidationError('Связанная привычка должна иметь признак приятной привычки')
