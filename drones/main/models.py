from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

# Create your models here.

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
   
    serial_number       = models.IntegerField(max_length=100, validators=[MinValueValidator(0), MaxLengthValidator(100)])
    drone_model         = models.CharField(choices=type_drone)
    weight_limit        = models.PositiveIntegerField()
    battery_capacity    = models.PositiveIntegerField()
    sate                = models.CharField(choices=drones_state) 

    class Meta:
        """Meta definition for Drone."""

        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'

    def __str__(self):
        return str(drone_model)+ " "+str(serial_number)



class Medication(models.Model):
    
    name = models.CharField()
    weight = models.IntegerField(validators=[MinValueValidator(0)])
    code = models.CharField()
    image = models.ImageField()

    class Meta:
        """Meta definition for Medication."""

        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'

    def __str__(self):
        return name
