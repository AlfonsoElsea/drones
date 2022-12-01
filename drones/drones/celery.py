from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','drones.settings')

app = Celery('drones')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.beat_schedule ={
#    'battery_depleting':{
#     'task': 'mainApi.tasks.battery_deplete',
#     'schedule': 1
    
#    }   
# }

app.autodiscover_tasks()
