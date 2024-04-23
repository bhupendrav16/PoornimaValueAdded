from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.generics import ListCreateAPIView

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated ,AllowAny
from classroom.models import ClassroomModel
from .models import CustomUser
from authentication.serializer import UserSerializer
from .models import Timetable, Attendance, TestSchedule, StudentPerformance
from .serializer import TimetableSerializer, AttendanceSerializer, TestScheduleSerializer, StudentPerformanceSerializer

class IsFacultyOfClassroom(BasePermission):
    """
    Custom permission to only allow faculty members of the classroom to access a view.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated and is a faculty member
        if request.user.is_authenticated and request.user.is_faculty:
            # Check if the user is the faculty of the classroom associated with the attendance
            return obj.timetable.classroom.faculty == request.user
        return False

class TimetableListCreateView(APIView):
    

    def get(self, request, format=None):
        user = request.user

        if not user.is_faculty:
            # For students, filter timetables based on their enrolled courses
            classrooms = ClassroomModel.objects.filter(students=user)
            timetables = Timetable.objects.filter(classroom__in=classrooms)
            serializer = TimetableSerializer(timetables, many=True)
            return Response(serializer.data)
        elif user.is_faculty:
            # For faculty, filter timetables based on the courses they are teaching
            timetables = Timetable.objects.filter(faculty=user)
            serializer = TimetableSerializer(timetables, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "User is not a student or faculty"}, status=status.HTTP_403_FORBIDDEN)
        
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = TimetableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AttendanceListCreateView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     # permission_classes = [AllowAny]

    
#     def get(self, request, format=None):
#         # Filter attendance records for the current user
#         attendance = Attendance.objects.filter(student=self.request.user)
#         serializer = AttendanceSerializer(attendance, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = AttendanceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestScheduleListCreateView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        test_schedules = TestSchedule.objects.all()
        serializer = TestScheduleSerializer(test_schedules, many=True)
        return Response(serializer.data)

    permission_classes =[IsAuthenticated]
    def post(self, request, format=None):
        serializer = TestScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentPerformanceListCreateView(APIView):
    def get(self, request, format=None):
        student_performances = StudentPerformance.objects.all()
        serializer = StudentPerformanceSerializer(student_performances, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentPerformanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Return the currently authenticated user
        return self.request.user

class AttendanceListCreateView(ListCreateAPIView):
    
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, IsFacultyOfClassroom]
    # permission_classes = [AllowAny]
    def get_queryset(self):
    # Get the faculty user
        faculty_user = self.request.user

        # Get the classrooms associated with the faculty user
        classrooms = faculty_user.classrooms_faculty.all()

        # Extract the IDs of the classrooms
        classroom_ids = classrooms.values_list('id', flat=True)

    # Filter attendance records for the students in the classrooms associated with the faculty user
        return Attendance.objects.filter(timetable__classroom__in=classroom_ids)
    def perform_create(self, serializer):
        # Assign the faculty user as the creator of the attendance record
        serializer.save(faculty=self.request.user)
        