from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path('workouts/', views.workouts_index, name='index'),
    path('workouts/<int:workout_id>/', views.workouts_detail, name='detail'),
    path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
    path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workouts_update'),
    path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workouts_delete'),
    path('workouts/<int:workout_id>/add_workout/', views.add_workout, name='add_workout'),
    path('workouts/<int:workout_id>/assoc_equipment/<int:equipment_id>', views.assoc_equipment, name='assoc_equipment'),
    path('workouts/<int:workout_id>/unassoc_equipment/<int:equipment_id>', views.unassoc_equipment, name='unassoc_equipment'),
    path('equipments/', views.EquipmentList.as_view(), name= 'equipments_index'),
    path('equipments/<int:pk>/', views.EquipmentDetail.as_view(), name= 'equipments_detail'),
    path('equipments/create/', views.EquipmentCreate.as_view(), name= 'equipments_create'),
    path('equipments/<int:pk>/update/', views.EquipmentUpdate.as_view(), name= 'equipments_update'),
    path('equipments/<int:pk>/delete', views.EquipmentDelete.as_view(), name= 'equipments_delete'),
]