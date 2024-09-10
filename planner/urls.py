from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # URL for listing all tasks
    path('create/', views.task_create, name='task_create'),  # URL for creating a new task
    path('<int:task_id>/', views.task_detail, name='task_detail'),  # URL for viewing task details
    path('<int:task_id>/add-reminder/', views.add_reminder, name='add_reminder'),  # URL for adding a reminder
]