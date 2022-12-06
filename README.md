# drones
Service to communicate with drones made with Django and Django-rest-framework using as database SQlite to ensure portability

Dependencies:

Python3

Django

RabbitMQ

Instalation Process:

1.- Download and Install RabbitMQ for you OS and start its service
https://www.rabbitmq.com/download.html
    "I recommend to install it with Chocolatey, the package manager as it is pretty straightforward, if you choose to do so this is the command:"
    
    choco install rabbitmq



2.- From the folder inside the drone project:

    2.1.-Run: 
    
        pip install -r requirements.txt
    

to install Django and its dependencies.


    2.2.-Run:
        
        python manage.py runserver
    

to start de server



    2.3.-Run:
        
        celery -A drones worker -l info -P gevent
    
it will start the Task Queue

And

    2.4.-Run
        
        celery -A drones beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
    

that runs the Task Scheduler


The aplication server runs in:
http://127.0.0.1:8000/

I have included and export of a POSTMAN Collection in a folder named 'Tools' inside the project, it have all the endpints ready to taste.


API ENDPOINTS.

POST

/api/drones/

Allow to register a drone and show a list of drones.


/api/medication/

Allow to register a medication and show a list of medications.


/api/load/

Allow to load a drone with a medication and show the list of loads.


PUT

/api/drones/<drone_id>

Allow to edit a drone.


/api/medication/<medication_id>

Allow to edit a medication.


/api/load/<load_id>

Allow to edit a load.


GET

/api/available-drones/

Show a list of available drones


/api/check-load-drones/<drone_id>

Show the load of specified drone


/api/check-battery-drones/<drone_id>

Show battery level of specified drone




