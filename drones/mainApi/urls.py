from django.urls import path, include
from .views import *

app_name = 'mainApi'

urlpatterns = [
    path('drones/', DroneView.as_view(),name='drones'),
    path('available-drones/', GetAvailableDrones.as_view()),
    path('check-load-drones/<int:pk>', GetDronesLoad.as_view()),
    path('check-battery-drones/<int:pk>', GetDronesBatteryLevel.as_view()),
    path('drones/<int:pk>', GetDroneView.as_view()),
    path('medication/', MedicationView.as_view()),
    path('medication/<int:pk>', GetMedicationView.as_view()),    
    path('load/', LoadView.as_view()),
    path('load/<int:pk>', GetLoadView.as_view()),
    
]