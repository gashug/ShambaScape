from django.urls import path
from . import views

urlpatterns = [
    path("", views.design_list, name="design_list"), # URL for the design list view
    path("create/", views.design_create, name="design_create"), # URL for creating a new design
    path("<int:design_id>/", views.design_detail, name="design_detail"), # URL for viewing a specific design
]