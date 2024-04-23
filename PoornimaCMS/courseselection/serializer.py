from rest_framework import serializers
from .models import UserCourseSelection
from courses.models import Course
from courses.serializer import CourseSerializer

class UserCourseSelectionSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    course_name = serializers.SerializerMethodField()
    def get_course_name(self, obj):
        return obj.course.name


    class Meta:
        model = UserCourseSelection
        fields = ['id', 'user', 'course', 'course_name']
        
