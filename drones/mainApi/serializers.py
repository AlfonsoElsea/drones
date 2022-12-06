from rest_framework import serializers
from main.models import *
from django.db.models import Count, Q, Sum,Subquery,ExpressionWrapper,IntegerField,F, Case, When,FloatField



class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


# class DroneDetailSerializer(serializers.ModelSerializer):
#     drone = serializers.ReadOnlyField(source='drone.serial_number')

#     class Meta:
#         model= Load
#         fields =['drone','medication']

class DroneLoadSerializer(serializers.ModelSerializer):
    load = serializers.StringRelatedField(many=True)
    class  Meta:
        model= Drone
        fields=['load',]

class DroneBatteryCapacitySerializer(serializers.ModelSerializer):
    class  Meta:
        model= Drone
        fields=['battery_capacity',]

class DroneSerializer(serializers.ModelSerializer):
    # medication = MedicationSerializer(required=False, many=True)
    load = serializers.StringRelatedField(many=True)
    # load = DroneDetailSerializer(source='load_set', many=True)
    # load = serializers.SlugRelatedField(
    #     many=True,
    #     queryset= Load.objects.all(),
    #     slug_field='medication'
    # )
    class Meta:
        model=Drone
        fields='__all__'
        
    


    def validate(self, data):
        if(data['state']=='LOADING' and data['battery_capacity']<25):             
             raise serializers.ValidationError({'battery_capacity':"Battery to low, please recharge first!!"})

        return data
   

       
        
    #     return ret

    

class LoadSerializer(serializers.ModelSerializer):
    # drone      = serializers.StringRelatedField(many=True)
    # medication      = serializers.StringRelatedField(many=True)

    # medication = MedicationSerializer(required=False)

    class Meta:
        model = Load
        fields = '__all__'

    def validate(self, data):

        loaded= Load.objects.filter(drone_id=data['drone'].id).aggregate(load=Sum('medication__weight'))['load']
        medication = Medication.objects.get(pk=data['medication'].id).weight
        weight_limit= Drone.objects.get(pk=data['drone'].id).weight_limit
        
        if(loaded):
            if(loaded+medication >weight_limit):       
                raise serializers.ValidationError({'drone':"Weight exceded!!"})
        return data


        

    def to_representation(self, instance):
        ret =super().to_representation(instance)
        try:
            ret['drone']=instance.drone.drone_model +" Drone "+instance.drone.serial_number 
        except Drone.DoesNotExist:
            ret['drone']= None
        except AttributeError:
            pass

        try:
            ret['medication']=instance.medication.name + " "+str(instance.medication.weight)+"mg"
        except Medication.DoesNotExist:
            ret['medication']= None
        except AttributeError:
            pass
        
        return ret

