from django.contrib import admin

# Register your models here.
from main.models import *
admin.site.register(Drone)
# admin.site.register(Load)
admin.site.register(Medication)
admin.site.register(Log)
