from django.db import models

# Model for categories of plants (e.g., shrubs, veggies ...)
class PlantCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # Optional description of the plant
    category = models.ForeignKey(PlantCategory, on_delete=models.SET_NULL, null=  True) # Each plant belongs to a category
    sun_exposure = models.CharField(max_length=50, choices=[
        ('full_sun', 'Full Sun'),
        ('partial_shade', 'Partial Shade'),
        ('full_shade', 'Full Shade'),
    ])  # Sunlight requirements (e.g., full sun, partial shade)
    water_requirements = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ])  # Watering needs (e.g., frequent, moderate)
    soil_requirements = models.CharField(max_length=100)
    bloom_time = models.CharField(max_length=50, choices=[
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall'),
        ('winter', 'Winter'),
    ], blank=True, null=True)  # Flowering time for plants which is optional for some plants
    harvest_time = models.CharField(max_length=50, blank=True, null=True)  # Optional harvest time for vegetables and fruit-bearing plants


    def __str__(self):
        return self.name