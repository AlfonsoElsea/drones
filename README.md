# drones
Service to communicate with drones made with Django and Django-rest-framework using as database SQlite to ensure portability

Dependencies:
Python3
Django
RabbitMQ

Install RabbitMQ and start its service
https://www.rabbitmq.com/download.html


From the folder inside de project run: 

pip install -r requirements.txt

to install Django and its dependencies.


Run:

python manage.py runserver

to start de server



Run

celery -A drones worker -l info -P gevent
it will start the Task Queue

And

celery -A drones beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

that runs the Task Scheduler



ENDPOINTS
api/drones/
api/available-drones/
api/check-load-drones/'drone id'
api/check-battery-drones/'drone id'
api/medication/
api/medication/'medication id'
api/load/
api/load/'load id'


