from django.shortcuts import render, redirect
from .models import Workout, Equipment
from .forms import SchedulingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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
  id_list = workout.equipments.all().values_list('id')
  equipment_workout_doesnt_have = Equipment.objects.exclude(id__in = id_list)
  scheduling_form = SchedulingForm()
  return render(request, 'workouts/detail.html', {
       'workout': workout,
       'scheduling_form': scheduling_form,
       'equipments': equipment_workout_doesnt_have
   })

class WorkoutCreate(CreateView):
    model = Workout
    fields = '__all__'

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = ['target', 'description', 'reps']

class WorkoutDelete(DeleteView):
    model = Workout
    success_url = '/workouts'

def add_workout(request, workout_id):
    form = SchedulingForm(request.POST)
    if form.is_valid():
        new_workout = form.save(commit=False)
        new_workout.workout_id = workout_id
        new_workout.save()
    return redirect('detail', workout_id = workout_id)

class EquipmentList(ListView):
    model = Equipment

class EquipmentDetail(DetailView):
    model = Equipment

class EquipmentCreate(CreateView):
    model = Equipment
    fields='__all__'

class EquipmentUpdate(UpdateView):
    model = Equipment
    fields = ['name']

class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = '/equipments'

def assoc_equipment(request, workout_id, equipment_id):
    Workout.objects.get(id=workout_id).equipments.add(equipment_id)
    return redirect('detail', workout_id=workout_id)

def unassoc_equipment(request, workout_id, equipment_id):
    Workout.objects.get(id=workout_id).equipments.remove(equipment_id)
    return redirect('detail', workout_id=workout_id)
