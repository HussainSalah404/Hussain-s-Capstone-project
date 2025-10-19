"""
Automated tests for the Recipe Management API.
Covers:
- Recipe creation and retrieval.
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from recipes.models import Category, Ingredient, Recipe


class RecipeAPITests(APITestCase):
    """Test suite for Recipe API endpoints."""

    def setUp(self):
        self.client = APIClient()

        # Create test user and authenticate
        self.user = User.objects.create_user(
            username="first_tester", password="strongpassword123"
        )
        self.client.force_authenticate(user=self.user)

        # Create sample category and ingredient
        self.category = Category.objects.create(name="Dessert")
        self.ingredient = Ingredient.objects.create(name="Sugar")

    def test_create_recipe(self):
        """Ensure authenticated user can create a recipe."""
        url = reverse("recipe-list")  # Provided by router
        data = {
            "title": "Chocolate Cake",
            "description": "A simple cake recipe",
            "instructions": "Mix and bake.",
            "category": self.category,
            "preparation_time": 10,
            "cooking_time": 30,
            "servings": 4,
            "ingredients": [self.ingredient],
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Recipe.objects.first(), "Chocolate Cake")

    def test_list_recipes(self):
        """Ensure recipes can be listed."""
        Recipe.objects.create(
            title="Test Recipe",
            description="desc",
            instructions="cook well",
            category=self.category,
            owner=self.user,
        )

        url = reverse("recipe-list")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.json()) > 0)
