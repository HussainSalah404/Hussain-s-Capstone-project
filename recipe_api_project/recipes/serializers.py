from rest_framework import serializers
from .models import Recipe, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True
    )


    owner = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'description',
            'ingredients',
            'instructions',
            'category',
            'category_id',
            'owner',
            'created_at',
        ]
        read_only_fields = ['owner', 'created_at']