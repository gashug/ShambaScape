from django.db import models # Importing Django's model library
from django.contrib.auth.models import User # Importing the User model to associate designs with users

# Model representing a garden design
class Design(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Each design belongs to a user
    name = models.CharField(max_length=100) # Name of the design
    layout_data = models.JSONField() # Stores the design layout as JSON (e.g., positions of plants)
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp when the design was created

# Model representing individual elements (like plants) within a design
class LayoutElement(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE, related_name="elements") #Each element belongs to a specific desing; deleting a design removes its elements
    plant = models.ForeignKey('plants.Plant', on_delete=models.SET_NULL, null=True) 
    # Each layout element is associated with a plant (we'll be defined later in the 'plants' app)
    # If a plant is deleted, reference is set to null.
    position_x = models.FloatField() # X-coordinate of the element on the Canvas
    position_y = models.FloatField() # Y-coordinate of the element on the Canvas
