from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Recipe, Ingredient, Category
from .serializers import RecipeSerializer, IngredientSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly
from .filters import RecipeFilter

# Create your views here.
"""
Defines API views for managing recipes, ingredients, and categories.

Includes:
- RecipeViewSet: CRUD + filtering + search + custom endpoints
- IngredientViewSet: CRUD for ingredients
- CategoryViewSet: CRUD for categories
"""
class RecipeViewSet(viewsets.ModelViewSet):
    """Main viewset for recipes with search, filter, and custom category/ingredient endpoints."""
    queryset = Recipe.objects.all().select_related('category', 'owner').prefetch_related('ingredients')
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RecipeFilter
    search_fields = ['title', 'description', 'ingredients__name', 'category__name']
    ordering_fields = ['preparation_time', 'cooking_time', 'servings']

    def perform_create(self, serializer):
        """Associate the logged-in user as recipe owner."""
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'], url_path='by-category/(?P<category_name>[^/.]+)')
    def by_category(self, request, category_name=None):
        """Custom endpoint to fetch recipes by category name."""
        queryset = self.get_queryset().filter(category__name__iexact=category_name)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page or queryset, many=True)
        return self.get_paginated_response(serializer.data) if page else Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='by-ingredient/(?P<ingredient_name>[^/.]+)')
    def by_ingredient(self, request, ingredient_name=None):
        """Custom endpoint to fetch recipes containing a specific ingredient."""
        queryset = self.get_queryset().filter(ingredients__name__icontains=ingredient_name).distinct()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page or queryset, many=True)
        return self.get_paginated_response(serializer.data) if page else Response(serializer.data)

class IngredientViewSet(viewsets.ModelViewSet):
    """CRUD for ingredients."""
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD for categories."""
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]