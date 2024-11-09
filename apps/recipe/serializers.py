from rest_framework import serializers

from apps.recipe.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {'read_only': True}
        }
