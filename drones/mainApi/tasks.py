from __future__ import absolute_import, unicode_literals

from main.models import *

from celery import shared_task

from drones.celery import app as celery_app

@shared_task
def low_battery():
    queryset = Drone.objects.all()
    for drone in queryset:
        Log.objects.create(state=drone.state,drone=drone,battery_level=drone.battery_capacity)
        
        if(drone.state=="LOADING" and drone.battery_capacity<25):
            drone.state='IDLE'
            drone.save()
            Log.objects.create(state=drone.state,drone=drone,battery_level=drone.battery_capacity, state_changed=True)
        else:
            Log.objects.create(state=drone.state,drone=drone,battery_level=drone.battery_capacity, state_changed=False)


@shared_task
def battery_deplete():
    print("Depleting!!")

    queryset = Drone.objects.all()
    for drone in queryset:
        if(drone.battery_capacity>0):
            drone.battery_capacity-=1
            drone.save()
            print(drone.battery_capacity)
        else:
            drone.battery_capacity=100
            drone.save()



# @celery_app.on_after_configure.connect
# def add_periodic(**kwargs):
#     celery_app.add_periodic_task(1.0, battery_deplete(), name='add every 1')