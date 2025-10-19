"""
This module defines all database models for the Recipe Management API.

Models:
- Category: Represents a recipe category (e.g., Dessert, Breakfast).
- Ingredient: Represents an ingredient that can be reused across recipes.
- Recipe: Represents a complete recipe created by a user.
- RecipeIngredient: Through-model that connects recipes and ingredients with quantities.
"""

from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    """Stores recipe categories like 'Dessert', 'Main Course', etc.'"""
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Stores unique ingredients that can be shared between recipes."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Represents a recipe created by a user.
    Each recipe includes:
    - Basic info: title, description, instructions.
    - Timings: preparation and cooking time.
    - Relations: category, owner, ingredients (through RecipeIngredient).
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructions = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    preparation_time = models.PositiveIntegerField(help_text="in minutes", default=0)
    cooking_time = models.PositiveIntegerField(help_text="in minutes", default=0)
    servings = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='RecipeIngredient',
        related_name='recipes'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    """
    Intermediary table linking Recipe and Ingredient.
    Includes an optional 'quantity' field (e.g., "1 tsp", "2 cups").
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ('recipe', 'ingredient')
        verbose_name = 'Recipe Ingredient'
        verbose_name_plural = 'Recipe Ingredients'

    def __str__(self):
        qty = f" ({self.quantity})" if self.quantity else ""
        return f"{self.ingredient.name}{qty} in {self.recipe.title}"
