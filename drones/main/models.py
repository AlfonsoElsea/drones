from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def upload_to_medication(instance, filename):
    return 'medication/{filename}'.format(filename=filename)


#Model that represents each Medication
class Medication(models.Model):
    
    name = models.CharField(max_length=25, validators=[RegexValidator("^[-a-zA-Z0-9_]+\Z","Incorrect name format")])
    weight = models.IntegerField(validators=[MinValueValidator(0)])
    code = models.CharField(max_length=25,validators=[RegexValidator("^[A-Z0-9_]+\Z","Incorrect name format")])
    image = models.ImageField(upload_to=upload_to_medication, blank=True, null= True)

    class Meta:
        """Meta definition for Medication."""

        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'

    def __str__(self):
        return self.name+' '+str(self.weight)+"mg"

#Model that represents each drone
class Drone(models.Model):

    model_drone={
        ('Lightweight','Lightweight'),
        ('Middleweight','Middleweight'),
        ('Cruiseweight','Cruiseweight'),
        ('Heavyweight','Heavyweight'),

    }
    drones_state={
        ('IDLE','IDLE'),
        ('LOADING','LOADING'),
        ('LOADED','LOADED'),        
        ('DELIVERING','DELIVERING'),
        ('DELIVERED','DELIVERED'),
        ('RETURNING','RETURNING')
    }
   
    serial_number       = models.CharField(max_length=100, validators=[ RegexValidator("^-?\d+\Z","Serial Number must contain only numbers")])
    drone_model         = models.CharField(max_length=25, choices=model_drone)
    weight_limit        = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    battery_capacity    = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)] )
    state               = models.CharField(max_length=25, choices=drones_state) 
    load                = models.ManyToManyField(Medication, through='Load')

    class Meta:
        """Meta definition for Drone."""

        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'

    def __str__(self):
        return str(self.drone_model)+ " "+str(self.serial_number)


#Model That represents a drone loaded with a madication
class Load(models.Model):
    drone                 = models.ForeignKey(Drone, models.DO_NOTHING,related_name='drone',verbose_name='Drone', db_column='id_drone', null=True, blank=True)
    medication            = models.ForeignKey(Medication, models.DO_NOTHING,related_name='medication',verbose_name='Medication', db_column='id_medication', null=True, blank=True)

    def __str__(self):
        return self.drone+" has a "+ self.medication+" loaded " 

#Model that allow to log and audit when the drone state and battery level is chacked to see if the battery level is below 25% and the state is loading
class Log(models.Model):
    drone          = models.CharField(max_length=100)
    battery_level       = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)] )
    state               = models.CharField(max_length=25) 
    state_changed       = models.BooleanField(default=False)