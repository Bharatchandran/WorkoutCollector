from django.contrib import admin
from .models import Workout, Scheduling, Equipment
# Register your models here.
admin.site.register(Workout)
admin.site.register(Scheduling)
admin.site.register(Equipment)