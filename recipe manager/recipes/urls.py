"""
URL routing for the `recipes` app.

Routes:
- /api/recipes/            -> RecipeViewSet (list, create)
- /api/recipes/{id}/       -> RecipeViewSet (retrieve, update, delete)
- /api/recipes/by-category/{name}/  -> custom action: recipes by category
- /api/recipes/by-ingredient/{name}/ -> custom action: recipes by ingredient
- /api/ingredients/        -> IngredientViewSet
- /api/categories/         -> CategoryViewSet
- /api/auth/token/         -> SimpleJWT token obtain
- /api/auth/token/refresh/ -> SimpleJWT token refresh
"""
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RecipeViewSet, IngredientViewSet, CategoryViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('recipes', RecipeViewSet, basename='recipe')
router.register('ingredients', IngredientViewSet, basename='ingredient')
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
