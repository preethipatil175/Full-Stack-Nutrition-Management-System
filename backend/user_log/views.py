from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLogSerializer
from .models import User_Log

class UserLogView(APIView):
    def post(self, request):
        """Create a new food log entry"""
        serializer = UserLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLogDetailView(APIView):
    def get_object(self, log_id):
        try:
            return User_Log.objects.get(id=log_id)
        except User_Log.DoesNotExist:
            return None

    def put(self, request, log_id):
        """Full update (replace all fields)"""
        log = self.get_object(log_id)
        if not log:
            return Response({"error": "Log not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserLogSerializer(log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, log_id):
        """Partial update (update some fields only)"""
        log = self.get_object(log_id)
        if not log:
            return Response({"error": "Log not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserLogSerializer(log, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, log_id):
        """Delete a log"""
        log = self.get_object(log_id)
        if not log:
            return Response({"error": "Log not found"}, status=status.HTTP_404_NOT_FOUND)
        
        log.delete()
        return Response({"message": "Log deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
