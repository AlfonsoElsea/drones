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
