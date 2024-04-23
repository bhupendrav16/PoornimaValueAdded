from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClassroomModel
from .serializer import ClassroomSerializer
from rest_framework.permissions import AllowAny

class ClassroomListCreateView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        classrooms = ClassroomModel.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
