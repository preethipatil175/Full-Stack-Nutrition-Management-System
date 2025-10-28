from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailsSerializer
from .models import User_Details

class BmrTdeeAPIView(APIView):
    def get(self,request):
        users=User_Details.objects.all()
        serializer=UserDetailsSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            name = data['name']
            age = data['age']
            gender = data['gender']
            weight_kg = data['weight_kg']
            height_cm = data['height_cm']
            activity_level = data['activity_level']
            goal = data['goal']

            # Step 1: BMR
            if gender == 'Male':
                bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
            else:
                bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

            # Step 2: TDEE
            activity_levels = {
                'Sedentary': 1.2,
                'Lightly Active': 1.375,
                'Moderate': 1.55,
                'Active': 1.725,
                'Very Active': 1.9,
            }
            tdee = round(bmr * activity_levels.get(activity_level, 1.2), 2)

            # Step 3: Adjust calories
            if goal == 'Loss':
                calories = tdee - 500
            elif goal == 'Gain':
                calories = tdee + 500
            else:
                calories = tdee

            # Step 4: Save data
            serializer.save(
                bmr=round(bmr, 2),
                tdee=tdee,
                calories=calories
            )

            # return values
            return Response({
                'message': 'User details saved successfully',
                'bmr': round(bmr, 2),
                'tdee': tdee,
                'calories': calories,
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Optional: Render HTML form
def user_form(request):
    return render(request, 'users/user_form.html')
