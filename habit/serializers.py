from rest_framework import serializers

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        #    (
        #    'action',
        #    'is_pleasant',
        #    'location_action',
        #    'time_action',
        #    'period',
        #    'time_to_complete',
        #    'award',
        #    'is_public'
        #)