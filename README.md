# Python_exercises

Django + Celery + Beat

To run it you have to edit:

1. in settings.py:
            a) EMAIL params for sending email
2. in celery.py:
            a) time to run task: 'schedule': crontab(hour=12, minute=40)
            b) check your timezone: timezone='Europe/Warsaw' in two places
3. in mainapp.views.py:
            a) time to run dynamic created task: hour = 12, minute = 40

and

0. Run in console:          python3 mange.py migrate
1. Run in console:          python3 mange.py createsuperuser
                            a) don't forget to add email address - ther wil be send email from tasks
                            b) in admin panel you can also add new users with email address
2. Run in console:          python3 mange.py runserver
3. Run in new console:      celery -A django_celery_project.celery worker --pool=solo -l info
4. Run in new console:      celery -A django_celery_project.celery beat -l info
