from django.shortcuts import render, redirect, get_object_or_404
from .models import Plant, PlantCategory
from django.db.models import Q
from .forms import PlantForm

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

# View to create a new plant
def plant_create(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
    return render(request, 'plants/plant_form.html', {'form': form})

# View to edit an existing plant
def plant_edit(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plants/plant_form.html', {'form': form})

# View to delete a plant
def plant_delete(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('plant_list')
    return render(request, 'plants/plant_confirm_delete.html', {'plant': plant})