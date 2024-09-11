from django.shortcuts import render, redirect
from .models import Design

# View to display design homepage
def design_home(request):
    return render(request, 'design/design_home.html')

# View to display all designs
def design_list(request):
    designs = Design.objects.all()  # Get all designs
    return render(request, 'design/design_list.html', {'designs': designs})
                  
# View to create a new design)
def design_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        # Create a new design object and save it to the database
        new_design = Design.objects.create(name=name, description=description)
        new_design.save()
        
        # Redirect to the list of designs or the new design's detail page
        return redirect('design_list')
    
    return render(request, 'design/design_create.html')

# View to display a specific design (the drag-and-drop canvas)
def design_detail(request, design_id):
    design = Design.objects.get(id=design_id)
    return render(request, "design/design_detail.html", {"design": design})