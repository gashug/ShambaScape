from django.shortcuts import render

# View for the home page
def home(request):
    return render(request, 'home.html')  # Render the home template