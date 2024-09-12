from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),  # URL for the plant list
    path('<int:plant_id>/', views.plant_detail, name='plant_detail'),  # URL for a plant's detail view
    path('create/', views.plant_create, name='plant_create'),  # URL to create a plant
    path('<int:plant_id>/edit/', views.plant_edit, name='plant_edit'),  # URL to edit a plant
    path('<int:plant_id>/delete/', views.plant_delete, name='plant_delete'),  # URL to delete a plant
]