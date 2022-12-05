# drones
Service to communicate with drones made with Django and Django-rest-framework using as database SQlite to ensure portability

Dependencies:

Python3
Django
RabbitMQ

Instalation Process:

1.- Download and Install RabbitMQ for you OS and start its service
https://www.rabbitmq.com/download.html
    "I recommend to install it with Chocolatey, the package manager as it is pretty straightforward, i you choose to do so this is te command:"
    choco install rabbitmq



2.- From the folder inside the drone project run: 
    2.1-Run: 
    
    pip install -r requirements.txt
    

to install Django and its dependencies.


    2.2-Run: 
    
    python manage.py runserver
    

to start de server



    2.3-Run:
    
    celery -A drones worker -l info -P gevent
    
it will start the Task Queue

And

    2.4-Run
    
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


