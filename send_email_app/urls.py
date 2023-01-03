from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('send_mail/', views.send_mail_to_all, name="test_send_mail"),
    path('schedule_mail/', views.schedule_mail, name="test_schedule_mail"),
]