from rest_framework import serializers

from habit.models import Habit
from habit.validators import HabitCreateValidatr


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'

        validators = [HabitCreateValidatr(field='is_pleasent')]
