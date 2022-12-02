# drones
Service to communicate with drones made with Django and Django-rest-framework
From the folder inside de project run: 

pip install -r requirements.txt

to install Django and dependencies used.


Run:

python manage.py runserver

to start de server

Install RabbitMQ and start its service
https://www.rabbitmq.com/download.html

Run

celery -A drones worker -l info -P gevent
celery -A drones beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

to start the task queue.

ENDPOINTS
api/drones/
api/available-drones/
api/check-load-drones/'drone id'
api/check-battery-drones/'drone id'
api/medication/
api/medication/'medication id'
api/load/
api/load/'load id'


