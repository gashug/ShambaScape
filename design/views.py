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
    if request.method == "POST":
        # Create a new design
        name = request.POST.get("name")
        design = Design.objects.create(name=name, layout_data={}) # Create a design without a user association
        return redirect("design_detail", design_id=design.id)
    return render(request, "design/design_create.html")

# View to display a specific design (the drag-and-drop canvas)
def design_detail(request, design_id):
    design = Design.objects.get(id=design_id)
    return render(request, "design/design_detail.html", {"design": design})