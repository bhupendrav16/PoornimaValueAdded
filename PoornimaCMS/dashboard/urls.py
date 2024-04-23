from django.urls import path
from .views import TimetableListCreateView, AttendanceListCreateView, TestScheduleListCreateView, StudentPerformanceListCreateView,UserProfileAPIView

urlpatterns = [
    path('timetables/', TimetableListCreateView.as_view(), name='timetable-list-create'),
    path('attendance/', AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('testschedules/', TestScheduleListCreateView.as_view(), name='testschedule-list-create'),
    path('studentperformances/', StudentPerformanceListCreateView.as_view(), name='studentperformance-list-create'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
    # Add URLs for update, retrieve, or delete if needed
    # path('markattendance/', MarkAttendance.as_view(), name='mark-attendance'),
    
]