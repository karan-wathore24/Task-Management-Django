from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('tasks/', views.tasks, name="tasks"),
    path('addtask/', views.addtask, name="addtask"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('mark_done/<int:id>/', views.mark_done, name="mark_done"),
]
