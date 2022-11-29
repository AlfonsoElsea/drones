from rest_framework import serializers
from main.models import *



class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class DroneSerializer(serializers.ModelSerializer):
    # medication = MedicationSerializer(required=False, many=True)
    class Meta:
        model=Drone
        fields='__all__'

    def validate(self, data):
        if len(str(data['serial_number'])) >100:
            raise serializers.ValidationError({'serial_number':"Serial Number must be less than 100 long"})
        return data

class LoadSerializer(serializers.ModelSerializer):
    drone      = DroneSerializer(required=False)
    medication = MedicationSerializer(required=False)
    
    class Meta:
        model = Load
        fields = '__all__'

