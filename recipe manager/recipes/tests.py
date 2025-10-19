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
        """Set up test data."""
        self.client = APIClient()

        # Create test user and authenticate
        self.user = User.objects.create_user(
            username="first_tester", password="strongpassword123"
        )
        self.client.force_authenticate(user=self.user)

        # Create sample category and ingredient
        self.category = Category.objects.create(name="Dessert")
        self.ingredient = Ingredient.objects.create(name="Sugar")

        # Print debug information
        print(f"\nSetup completed:")
        print(f"User created: {self.user.username}")
        print(f"Category created: {self.category.name}")
        print(f"Ingredient created: {self.ingredient.name}")

    def test_create_recipe(self):
        """Ensure authenticated user can create a recipe."""
        url = reverse("recipe-list")
        data = {
            "title": "Chocolate Cake",
            "description": "A simple cake recipe",
            "instructions": "Mix and bake.",
            "category": {"name": self.category.name},
            "preparation_time": 10,
            "cooking_time": 30,
            "servings": 4,
            "recipeingredient_set": [
                {"ingredient": {"name": self.ingredient.name}, "quantity": "2 cups"}
            ],
        }

        print(f"\nSending POST request to: {url}")
        print(f"Request data: {data}")

        response = self.client.post(url, data, format="json")
        response_data = response.json()

        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response_data}")
        print(f"Recipe count in DB: {Recipe.objects.count()}")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
        
        recipe = Recipe.objects.first()
        self.assertIsNotNone(recipe, "Recipe was not created in database")
        if recipe:
            print(f"Created recipe title: {recipe.title}")
        
            self.assertEqual(recipe.title, "Chocolate Cake")

    def test_list_recipes(self):
        """Ensure recipes can be listed."""
        # Create a test recipe
        test_recipe = Recipe.objects.create(
            title="Test Recipe",
            description="desc",
            instructions="cook well",
            category=self.category,
            owner=self.user,
        )

        print(f"\nTest recipe created: {test_recipe.title}")

        url = reverse("recipe-list")
        print(f"Sending GET request to: {url}")

        response = self.client.get(url, format="json")
        response_data = response.json()

        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response_data}")
        print(f"Number of recipes returned: {len(response_data)}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response_data) > 0)