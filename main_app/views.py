from django.shortcuts import render
from .models import Workout
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# from django.http import HttpResponse
## Create your views here.
# def home(request):
#     path = request.path
#     return HttpResponse("this works")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def workouts_index(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/index.html', {
        'workouts' : workouts
    })

def workouts_detail(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  return render(request, 'workouts/detail.html', { 'workout': workout })

class WorkoutCreate(CreateView):
    model = Workout
    fields = '__all__'

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = ['target', 'description', 'reps']

class WorkoutDelete(DeleteView):
    model = Workout
    success_url = '/workouts'