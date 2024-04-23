from rest_framework import serializers
from .models import ClassroomModel
from authentication.serializer import UserSerializer
from  courses.serializer import CourseSerializer

class ClassroomSerializer(serializers.ModelSerializer):
    students = UserSerializer(many=True)
    faculty = UserSerializer()
    course = CourseSerializer() 

    class Meta:
        model = ClassroomModel
        fields = '__all__'