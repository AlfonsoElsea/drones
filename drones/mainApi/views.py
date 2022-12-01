from django.shortcuts import render
from rest_framework import generics, filters, viewsets,views, status
from main.models import *
from .serializers import *
from .tasks import battery_deplete,low_battery


class DroneView(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class= DroneSerializer
   


class GetDroneView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

class GetAvailableDrones(generics.ListAPIView):
    queryset= Drone.objects.filter( battery_capacity__gt=25,state='IDLE'
    # ,weight_limit__gt=Sum('load__weight')
    )
    serializer_class= DroneSerializer

class GetDronesLoad(generics.RetrieveAPIView):
    queryset= Drone.objects.all()
    serializer_class= DroneLoadSerializer

class GetDronesBatteryLevel(generics.RetrieveAPIView):
    queryset= Drone.objects.all()
    serializer_class= DroneBatteryCapacitySerializer

class MedicationView(generics.ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class= MedicationSerializer

class GetMedicationView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class LoadView(generics.ListCreateAPIView):
    queryset = Load.objects.all()
    serializer_class= LoadSerializer

class GetLoadView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
