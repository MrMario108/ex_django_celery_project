from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from .task import test_func
from send_email_app.task import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 12, minute = 40)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"14", task='send_email_app.task.send_mail_func')#, args = json.dumps([[2,3]]))
    return HttpResponse("Done -schedule")