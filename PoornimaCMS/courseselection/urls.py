from django.urls import path
from .views import UserCourseSelectionCreateView,UserCourseSelectionGetView

urlpatterns = [
    path('user-course-selection/', UserCourseSelectionCreateView.as_view(), name='user-course-selection'),
    path('user-selected-course/', UserCourseSelectionGetView.as_view(), name='user-selected-course'),
]
