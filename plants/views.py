from django.shortcuts import render
from .models import Plant, PlantCategory
from django.db.models import Q

# View to list all plants, optionally filter by category and search by name
def plant_list(request):
    category_id = request.GET.get('category')  # Get the selected category from the query string
    search_query = request.GET.get('search')  # Get the search query from the query string
    
    plants = Plant.objects.all()

    if category_id:
        plants = plants.filter(category_id=category_id)  # Filter by category
    
    if search_query:
        plants = plants.filter(Q(name__icontains=search_query))  # Filter by search query
    
    categories = PlantCategory.objects.all()  # Get all plant categories
    return render(request, 'plants/plant_list.html', {'plants': plants, 'categories': categories})

# View to display the details of a single plant
def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)  # Fetch plant by ID
    return render(request, 'plants/plant_detail.html', {'plant': plant})