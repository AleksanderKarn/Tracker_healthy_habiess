import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracker_healthy_habies.settings')

app = Celery('tracker_healthy_habies')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "status_check_1_minut": {
        "task": "habit.tasks.check_start_habit",
        "schedule": crontab(minute='*/1'),
    },
    "status_change_one_hour": {
        "task": "habit.tasks.setup_default_status_one_hour",
        "schedule": crontab(minute='*/1'),
    },
    "status_change_one_day": {
        "task": "habit.tasks.setup_default_status_one_day",
        "schedule": crontab(minute='*/1'),
    },

}
