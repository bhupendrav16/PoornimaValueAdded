from django.urls import path
from .views import ClassroomListCreateView

urlpatterns = [
    path('class/', ClassroomListCreateView.as_view(), name='class'),
    # Add other URLs as needed
]
