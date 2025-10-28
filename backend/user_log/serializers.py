from rest_framework import serializers
from .models import User_Log

class UserLogSerializer(serializers.Serializer):
    MEAL_TYPE=[('Breakfast','Breakfast'),('Lunch','Lunch'),('Dinner','Dinner'),('Snacks','Snacks')]
    user_id=serializers.IntegerField()
    user_name=serializers.CharField()
    date=serializers.DateField()
    meal_type=serializers.CharField()
    food_name=serializers.CharField()
    quantity_in_grams=serializers.IntegerField()
    calories=serializers.IntegerField()
    
    def create(self, validated_data):
        user_log = User_Log(**validated_data)
        user_log.save()
        return user_log