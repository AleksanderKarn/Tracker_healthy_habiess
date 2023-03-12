from datetime import datetime

from habit.models import Habit
from habit.tg_bot import funk
from tracker_healthy_habies.celery import app


@app.task
def check_start_habit():
    filter_cond = {"status": "processed"}
    habit_list = Habit.objects.filter(**filter_cond)
    if habit_list.exists():
        for habit in habit_list:
            if habit.time_action <= datetime.now().time():
                m = f"Выполнить привычку {habit.action} за {habit.time_to_complete} минут, чтобы получить награду {habit.award}"
                funk(m)
                habit.status = 'run'
                habit.save()





@app.task
def setup_default_status_one_hour():
    filter_cond = {"status": "ended"}
    habit_list = Habit.objects.filter(**filter_cond)
    if habit_list.exists():
        for habit in habit_list:
            if habit.period == 'one_hour':
                habit.status = 'processed'
                habit.save()


@app.task
def setup_default_status_one_day():
    filter_cond = {"status": "ended"}
    habit_list = Habit.objects.filter(**filter_cond)
    if habit_list.exists():
        for habit in habit_list:
            if habit.period == 'one_day':
                habit.status = 'processed'
                habit.save()


@app.task
def setup_default_status_one_week():
    filter_cond = {"status": "ended"}
    habit_list = Habit.objects.filter(**filter_cond)
    if habit_list.exists():
        for habit in habit_list:
            if habit.period == 'one_week':
                habit.status = 'processed'
                habit.save()


@app.task
def setup_default_status_one_month():
    filter_cond = {"status": "ended"}
    habit_list = Habit.objects.filter(**filter_cond)
    if habit_list.exists():
        for habit in habit_list:
            if habit.period == 'one_month':
                habit.status = 'processed'
                habit.save()

# celery -A tracker_healthy_habies worker -l INFO -P eventlet

# celery -A tracker_healthy_habies beat -l info -S django
