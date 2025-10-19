"""
Serializers for Recipe Management API.

Handles data conversion between Django models and JSON:
- IngredientSerializer: Ingredient data.
- CategorySerializer: Category data.
- RecipeIngredientSerializer: Ingredient details with quantity.
- RecipeSerializer: Main recipe logic with nested category and ingredients.
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Recipe, Ingredient, Category, RecipeIngredient

User = get_user_model()


def normalize_name(name: str) -> str:
    """Helper function to normalize and format input strings."""
    return name.strip().title()


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredient model."""

    class Meta:
        model = Ingredient
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""

    class Meta:
        model = Category
        fields = ['id', 'name']


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """Serializer for RecipeIngredient model (with nested Ingredient info)."""
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']


class RecipeSerializer(serializers.ModelSerializer):
    """
    Main serializer for Recipe model.
    Includes:
    - Nested Category
    - Nested Ingredients with quantities
    - Read-only Owner field
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    category = CategorySerializer(required=False, allow_null=True)
    recipeingredient_set = RecipeIngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'instructions', 'category',
            'preparation_time', 'cooking_time', 'servings',
            'created_at', 'updated_at', 'owner', 'recipeingredient_set'
        ]

    # -----------------------
    # Helper methods
    # -----------------------
    def _get_or_create_category(self, cat_data):
        """Create or fetch an existing category by name."""
        if not cat_data or not cat_data.get('name'):
            return None
        category_name = normalize_name(cat_data['name'])
        obj, _ = Category.objects.get_or_create(name=category_name)
        return obj

    def _get_or_create_ingredient(self, name):
        """Create or fetch an existing ingredient by name."""
        ingredient_name = normalize_name(name)
        obj, _ = Ingredient.objects.get_or_create(name=ingredient_name)
        return obj

    # -----------------------
    # Core CRUD methods
    # -----------------------
    def create(self, validated_data):
        """Custom creation logic for nested category and ingredients."""
        ingredients_data = validated_data.pop('recipeingredient_set', [])
        category_data = validated_data.pop('category', None)
        category = self._get_or_create_category(category_data) if category_data else None

        recipe = Recipe.objects.create(
            owner=self.context['request'].user,
            category=category,
            **validated_data
        )

        for entry in ingredients_data:
            ingredient_info = entry.get('ingredient', {})
            ingredient_name = ingredient_info.get('name')
            if ingredient_name:
                ingredient_obj = self._get_or_create_ingredient(ingredient_name)
                RecipeIngredient.objects.create(
                    recipe=recipe,
                    ingredient=ingredient_obj,
                    quantity=entry.get('quantity', '')
                )

        return recipe

    def update(self, instance, validated_data):
        """Custom update logic that replaces ingredients and updates category."""
        ingredients_data = validated_data.pop('recipeingredient_set', None)
        category_data = validated_data.pop('category', None)

        if category_data is not None:
            instance.category = self._get_or_create_category(category_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Replace ingredients
        if ingredients_data is not None:
            instance.recipeingredient_set.all().delete()
            for entry in ingredients_data:
                ingredient_info = entry.get('ingredient', {})
                ingredient_name = ingredient_info.get('name')
                if ingredient_name:
                    ingredient_obj = self._get_or_create_ingredient(ingredient_name)
                    RecipeIngredient.objects.create(
                        recipe=instance,
                        ingredient=ingredient_obj,
                        quantity=entry.get('quantity', '')
                    )

        return instance
