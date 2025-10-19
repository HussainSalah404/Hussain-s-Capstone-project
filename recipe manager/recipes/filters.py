"""
Implements custom filters using django-filters.

- Allows filtering recipes by category, ingredient, and cooking/preparation time.
"""
import django_filters
from .models import Recipe

class RecipeFilter(django_filters.FilterSet):
    """Custom filters for the Recipe model."""
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    ingredient = django_filters.CharFilter(method='filter_by_ingredient')
    ingredients = django_filters.CharFilter(method='filter_by_multiple_ingredients')

    max_cooking_time = django_filters.NumberFilter(field_name='cooking_time', lookup_expr='lte')
    min_cooking_time = django_filters.NumberFilter(field_name='cooking_time', lookup_expr='gte')
    max_preparation_time = django_filters.NumberFilter(field_name='preparation_time', lookup_expr='lte')
    min_preparation_time = django_filters.NumberFilter(field_name='preparation_time', lookup_expr='gte')
    servings = django_filters.NumberFilter(field_name='servings', lookup_expr='exact')

    class Meta:
        model = Recipe
        fields = []

    def filter_by_ingredient(self, queryset, name, value):
        """Filter recipes that include a specific ingredient."""
        return queryset.filter(ingredients__name__icontains=value).distinct()

    def filter_by_multiple_ingredients(self, queryset, name, value):
        """Filter recipes containing multiple comma-separated ingredients."""
        parts = [p.strip() for p in value.split(',') if p.strip()]
        for p in parts:
            queryset = queryset.filter(ingredients__name__icontains=p)
        return queryset.distinct()