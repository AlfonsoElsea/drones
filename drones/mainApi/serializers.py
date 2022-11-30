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
#     slug_re = _lazy_re_compile(r"^[-a-zA-Z0-9_]+\Z")
# validate_slug = RegexValidator(
#     slug_re,
#     # Translators: "letters" means latin letters: a-z and A-Z.
#     _("Enter a valid “slug” consisting of letters, numbers, underscores or hyphens."),
#     "invalid",
# )
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
            ret['drone']=instance.id_drone.serial_number
        except Drone.DoesNotExist:
            ret['drone']= None
        except AttributeError:
            pass

        try:
            ret['medication']=instance.id_medication.name
        except Medication.DoesNotExist:
            ret['medication']= None
        except AttributeError:
            pass
        
        return ret

