from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')
app = Celery('django_celery_project')

app.conf.update(
    broker_url = "redis://127.0.0.1:6379",
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Warsaw',
    enable_utc=False,
    result_backend = 'redis://localhost:6379', #"django-db",
)
app.config_from_object(settings, namespace='CELERY')

# Celery Best Settings
app.conf.beat_schedule ={
    'send-mail-every-day-at-8': {
        'task': 'send_email_app.task.send_mail_func',
        'schedule': crontab(hour=12, minute=40),
        'args' : ('dodatkowe dane z schedule',),
        'timezone':'Europe/Warsaw',
    }
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Requset: {self.request!r}')

