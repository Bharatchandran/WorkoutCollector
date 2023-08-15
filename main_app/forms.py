from django.forms import ModelForm
from .models import Scheduling

class SchedulingForm(ModelForm):
    class Meta:
        model = Scheduling
        fields = ['date', 'workout_time']
    