from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),  # URL for the plant list
    path('<int:plant_id>/', views.plant_detail, name='plant_detail'),  # URL for a plant's detail view
]