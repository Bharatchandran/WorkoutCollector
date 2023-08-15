from django.db import models
from django.urls import reverse
from datetime import date

TIMING = (
  ('M', 'Morning'),
  ('E', 'Evening'),
  ('N', 'Night'),
)

# Create your models here.

class Equipment(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('equipments_detail', kwargs={'pk': self.id})
class Workout(models.Model):
    name = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    reps = models.CharField(max_length=100)
    sets = models.IntegerField()

    equipments = models.ManyToManyField(Equipment)
    # Changing this incstance method dows not impact the database, therfore
    # no makemigration is necessary
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})
    
    def workout_for_today(self):
        return self.scheduling_set.filter(date=date.today()).count() >= len(TIMING)
    
 
class Scheduling(models.Model):
    date = models.DateField('Workout Date')
    workout_time = models.CharField(
        max_length=2,
        choices=TIMING,
        default=TIMING[0][0]
    )
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_workout_time_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']