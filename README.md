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
allow to register a drone and show a list of drones /api/drones/
show the specified drone /api/drones/<drone_id>
show a list of available drones /api/available-drones/
show the load of specified drone /api/check-load-drones/<drone_id>
show battery level of specified drone /api/check-battery-drones/<drone_id>
allow to register a medication and show a list of medications /api/medication/
show the specified medication /api/medication/<medication_id>
allow to load a drone with a medication and show the list of loads /api/load/
show the specified load /api/load/<load_id>


