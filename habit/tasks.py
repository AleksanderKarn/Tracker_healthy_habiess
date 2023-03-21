from datetime import timedelta, datetime

from habit.bot import notification
from habit.models import Habit
from tracker_healthy_habies.celery import app


@app.task
def check_start_habit():
    filter_cond = {"status": "processed"}
    habit_list = Habit.objects.filter(**filter_cond)
    if habit_list.exists():
        for habit in habit_list:
            if habit.time_action <= datetime.now().time():
                owner = habit.owner
                chat_id = owner.chat_id
                message = f"Выполнить привычку {habit.action} за {habit.time_to_complete} минут, чтобы получить награду {habit.award}"
                notification(chat_id, message)
                habit.time_action = datetime.now().time()
                habit.status = 'run'
                habit.save()


@app.task
def setup_default_status_one_hour():
    '''задача для изменения статуса каждый час '''
    filter_cond = {"status": "ended"}
    habit_list = Habit.objects.filter(**filter_cond)
    if habit_list.exists():
        for habit in habit_list:
            t = datetime.now() - timedelta(hours=1)
            if habit.period == 'one_hour' and habit.time_action <= t.time():
                habit.time_action = datetime.now().time()
                habit.status = 'processed'
                habit.save()


@app.task
def setup_default_status_one_day():
    '''раз в день'''
    filter_cond = {"status": "ended"}
    habit_list = Habit.objects.filter(**filter_cond)
    if habit_list.exists():
        for habit in habit_list:
            if habit.period == 'one_day' and habit.time_action > datetime.now().time():
                habit.status = 'processed'
                habit.save()




# celery -A tracker_healthy_habies worker -l INFO -P eventlet

# celery -A tracker_healthy_habies beat -l info -S django
