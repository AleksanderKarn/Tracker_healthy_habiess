from django.conf import settings
from django.db import models

from user.models import NULLABLE


class Habit(models.Model):
    RUN = "run"
    ENDED = 'executed'
    PROCESSED = 'processed'

    STATUS_HABIT = (
        ('run', 'в процессе'),
        ('ended', 'выполнена'),
        ('processed', 'в ожидании начала')
    )

    ONE_HOUR = 'one_hour'
    ONE_DAY = 'one_day'
    ONE_WEEK = 'one_week'

    PERIODS = (
        ('one_hour', 'раз в час'),
        ('one_day', 'раз в день'),
        ('one_week', 'раз в неделю'),
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    location_action = models.CharField(max_length=150, verbose_name='Место для выполнения привычки')
    time_action = models.TimeField(verbose_name='время, когда необходимо выполнять привычку')
    action = models.CharField(max_length=150, verbose_name='действие, которое представляет из себя привычка')

    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    pleasant_habit = models.ForeignKey('self', related_name='pleasant_habi', on_delete=models.SET_NULL, **NULLABLE)

    period = models.CharField(max_length=20, choices=PERIODS, default=ONE_DAY, verbose_name='периодичность')
    award = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности привычки')

    status = models.CharField(choices=STATUS_HABIT, max_length=20, default=PROCESSED, verbose_name='Статус привычки')

    def __str__(self):
        return f'Привычка {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
