from rest_framework import serializers
from datetime import time
from habit.models import Habit


class HabitCreateValidatr:
    pleasant_habit_id = Habit.objects.all().filter(is_pleasant=True)

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        is_pleasant = value.get('is_pleasant')
        pleasant_habit = value.get('pleasant_habit')
        award = value.get('award')
        period = value.get('period')
        time_to_complete = value.get('time_to_complete')

        if is_pleasant == True:  # если привычка приятная
            if award or pleasant_habit:
                raise serializers.ValidationError("У приятной привычки не может быть вознаграждения")
            elif period:
                raise serializers.ValidationError("у приятной привычки не может быть периодичности выполнения")
            elif time.fromisoformat(str(time_to_complete)) > time.fromisoformat("00:02:00"):
                raise serializers.ValidationError("время выполнения должно быть не больше 120 секунд")

        else:  # если привычка полезная
            if award and pleasant_habit:
                raise serializers.ValidationError("Может быть или вознаграждение или приятная привычка!")
            elif not award and not pleasant_habit:
                raise serializers.ValidationError(
                    "нельзя, чтобы связанная привычка и вознаграждение были одновременно пустые")
            elif pleasant_habit and pleasant_habit not in self.pleasant_habit_id:
                raise serializers.ValidationError(
                    "в связанные привычки могут попадать только привычки с признаком приятной привычки")
