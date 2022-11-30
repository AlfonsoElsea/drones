from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def upload_to_medication(instance, filename):
    return 'medication/{filename}'.format(filename=filename)

class Medication(models.Model):
    
    name = models.CharField(max_length=25)
    weight = models.IntegerField(validators=[MinValueValidator(0)])
    code = models.CharField(max_length=25)
    image = models.ImageField(upload_to=upload_to_medication)

    class Meta:
        """Meta definition for Medication."""

        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'

    def __str__(self):
        return self.name


class Drone(models.Model):

    type_drone={
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
   
    serial_number       = models.IntegerField( validators=[MinValueValidator(0)])
    drone_model         = models.CharField(max_length=25, choices=type_drone)
    weight_limit        = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    battery_capacity    = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)], )
    state               = models.CharField(max_length=25, choices=drones_state) 
    # load                = models.ManyToManyField(Medication)

    class Meta:
        """Meta definition for Drone."""

        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'

    def __str__(self):
        return str(self.drone_model)+ " "+str(self.serial_number)

class Load(models.Model):
    medication            = models.ForeignKey(Medication, models.DO_NOTHING,related_name='medication',verbose_name='Medication', db_column='id_medication', null=True, blank=True)
    drone                 = models.ForeignKey(Drone, models.DO_NOTHING,related_name='drone',verbose_name='Drone', db_column='id_drone', null=True, blank=True)




