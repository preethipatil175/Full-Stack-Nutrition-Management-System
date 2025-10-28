from django.shortcuts import render
import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Recipe
from .serializers import RecipeSerializer

openai.api_key = settings.OPENAI_API_KEY

class AIRecipeView(APIView):
    def post(self, request):
        meal_type = request.data.get('meal_type')
        diet_type = request.data.get('diet_type')
        calories = request.data.get('calories')

        if not (meal_type and diet_type and calories):
            return Response({"error": "Please provide meal_type, diet_type, and calories."},
                            status=status.HTTP_400_BAD_REQUEST)

        prompt = f"""
        Suggest a {diet_type} {meal_type} recipe under {calories} calories.
        Include:
        - Recipe name
        - Approx calories
        - Ingredients (list)
        - Instructions (steps)
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful nutrition assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7,
            )

            ai_text = response.choices[0].message["content"]

            # Parse the AI text roughly (you can refine with regex or JSON later)
            recipe_data = {
                "name": f"{diet_type} {meal_type} Recipe",
                "meal_type": meal_type,
                "diet_type": diet_type,
                "calories": int(calories),
                "ingredients": ["AI generated list"],
                "instructions": ai_text
            }

            serializer = RecipeSerializer(data=recipe_data)
            if serializer.is_valid():
                recipe = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

