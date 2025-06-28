import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remind_me.settings')

app = Celery('remind_me')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
