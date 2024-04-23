from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import UserCourseSelection
from .serializer import UserCourseSelectionSerializer
from classroom.models import ClassroomModel
from courses.models import Course
from dashboard.models import TestSchedule

class UserCourseSelectionCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        user = request.user
        course_id = request.data.get('course')
        try:
            course = Course.objects.get(id=course_id)
            faculty = course.faculty
        except Course.DoesNotExist:
            return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
        except CustomUser.DoesNotExist:
            return Response({"error": "Faculty not found for the course."}, status=status.HTTP_404_NOT_FOUND)

        if UserCourseSelection.objects.filter(user=user, course=course).exists():
            return Response({"error": "Course selection already exists for the user."}, status=status.HTTP_400_BAD_REQUEST)
        user_course_selection = UserCourseSelection.objects.create(user=user, course=course)
        classroom, created = ClassroomModel.objects.get_or_create(course=course, defaults={'faculty': faculty})
        if not created and faculty != classroom.faculty:
            classroom.faculty = faculty
            classroom.save()
        classroom.students.add(user)

        serializer = UserCourseSelectionSerializer(user_course_selection)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserCourseSelectionGetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user  # Assuming user is authenticated

        # Retrieve selected courses for the user
        selected_courses = UserCourseSelection.objects.filter(user=user)

        # Serialize the selected courses data
        serializer = UserCourseSelectionSerializer(selected_courses, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)