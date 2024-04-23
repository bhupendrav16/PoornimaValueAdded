from django.urls import path
from .views import BranchListCreateView, SemesterListCreateView, SubjectListCreateView, CourseListCreateView

urlpatterns = [
    path('branches/', BranchListCreateView.as_view(), name='branch-list-create'),
    path('semesters/', SemesterListCreateView.as_view(), name='semester-list-create'),
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    
    # Add URLs for update, retrieve, or delete if needed
]