from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.Serializer):
    name = serializers.CharField()
    meal_type = serializers.CharField()
    diet_type = serializers.CharField()
    calories = serializers.IntegerField()
    ingredients = serializers.ListField(child=serializers.CharField())
    instructions = serializers.CharField()

    def create(self, validated_data):
        return Recipe(**validated_data).save()
