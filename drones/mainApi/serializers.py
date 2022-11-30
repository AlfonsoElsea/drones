from rest_framework import serializers
from main.models import *
from django.db.models import Count, Q, Sum,Subquery,ExpressionWrapper,IntegerField,F, Case, When,FloatField



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
        if(data['state']=='LOADING' and data['battery_capacity']<25):             
             raise serializers.ValidationError({'battery_capacity':"Battery to low, please recharge first!!"})

        return data
    


    

class LoadSerializer(serializers.ModelSerializer):
    # drone      = DroneSerializer(required=False)
    # medication = MedicationSerializer(required=False)
    
    class Meta:
        model = Load
        fields = '__all__'

    

