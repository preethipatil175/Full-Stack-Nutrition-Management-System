# serializers.py
from rest_framework import serializers
from .models import User_Details

class UserDetailsSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=['Male', 'Female'])
    height_cm = serializers.FloatField()
    weight_kg = serializers.FloatField()
    activity_level = serializers.ChoiceField(choices=[
        'Sedentary', 'Lightly Active', 'Moderate', 'Active', 'Very Active'
    ])
    goal = serializers.ChoiceField(choices=['Loss', 'Maintain', 'Gain'])
    bmr = serializers.FloatField(read_only=True)
    tdee = serializers.FloatField(read_only=True)
    calories = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        user = User_Details(**validated_data)
        user.save()
        return user



        