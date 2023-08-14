from django.db import models
from django.urls import reverse

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    reps = models.IntegerField()
    sets = models.IntegerField()

    # Changing this incstance method dows not impact the database, therfore
    # no makemigration is necessary
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})