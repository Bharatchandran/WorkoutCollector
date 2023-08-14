from django.db import models

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # Changing this incstance method dows not impact the database, therfore
    # no makemigration is necessary
    def __str__(self):
        return f'{self.name} ({self.id})'