from django.db import models
from django.contrib.auth.models import User

# Create your models here.

""" 
Category model - e.g. Breakfast, Lunch, Dessert (the type or group the recipe belongs to)
The Category model contains only one field:
- name: A unique name for each category, with a maximum of 100 characters.
"""
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

""" 
Recipe model - stores the details of each recipe created by a user.

Fields:
- title: The name of the recipe (max 200 characters).
- description: A short overview of what the recipe is about.
- ingredients: A text field listing ingredients, separated by commas.
- instructions: Step-by-step directions on how to prepare the recipe.
- cooking_time: Time (in minutes) required to cook the recipe.
- category: A ForeignKey link to the Category model, showing what type of recipe it is.
- created_by: A ForeignKey link to the User who created the recipe.
- created_at: Automatically stores the date and time the recipe was created.
"""
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(help_text="List ingredients separated by commas")
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text="Time in minutes")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title