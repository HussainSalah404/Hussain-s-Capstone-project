"""
Admin registration for Recipe, Ingredient, Category, and RecipeIngredient.

Provides list views, search fields, and ordering to manage data easily from the admin panel.
"""
from django.contrib import admin
from .models import Recipe, Ingredient, Category, RecipeIngredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'created_at')
    search_fields = ('title', 'owner__username', 'category__name')
    list_filter = ('category',)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity')
    search_fields = ('recipe__title', 'ingredient__name')
