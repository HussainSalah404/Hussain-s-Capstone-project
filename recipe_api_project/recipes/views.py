from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from .models import Recipe, Category
from .serializers import RecipeSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework.response import Response

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-created_at')
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'ingredients__name', 'category__name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Filter by category name
    @action(detail=False, url_path='category/(?P<name>[^/.]+)')
    def by_category(self, request, name=None):
        recipes = self.queryset.filter(category__name__iexact=name)
        serializer = self.get_serializer(recipes, many=True)
        return Response(serializer.data)

    # Filter by ingredient name
    @action(detail=False, url_path='ingredient/(?P<name>[^/.]+)')
    def by_ingredient(self, request, name=None):
        recipes = self.queryset.filter(ingredients__icontains=name)
        serializer = self.get_serializer(recipes, many=True)
        return Response(serializer.data)