from django.shortcuts import render
from .models import Plant, PlantCategory

# View to list all plants and optionally filter by category
def plant_list(request):
    category_id = request.GET.get('category')  # Get the selected category from the query string
    if category_id:
        plants = Plant.objects.filter(category_id=category_id)  # Filter by category
    else:
        plants = Plant.objects.all()  # Show all plants if no filter is applied
    categories = PlantCategory.objects.all()  # Get all plant categories
    return render(request, 'plants/plant_list.html', {'plants': plants, 'categories': categories})

# View to display the details of a single plant
def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)  # Fetch plant by ID
    return render(request, 'plants/plant_detail.html', {'plant': plant})
