from django.urls import path, include
from .views import *

app_name = 'mainApi'

urlpatterns = [
    path('drones/', DroneView.as_view()),
    path('drones/<int:pk>', GetDroneView.as_view()),
    path('medication/', MedicationView.as_view()),
    path('medication/<int:pk>', GetMedicationView.as_view()),    
    path('load/', LoadView.as_view()),
    path('load/<int:pk>', GetLoadView.as_view()),
    
]