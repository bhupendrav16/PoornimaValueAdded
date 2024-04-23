from rest_framework import serializers
from .models import Timetable, Attendance, TestSchedule, StudentPerformance
from authentication.serializer import UserSerializer

class TimetableSerializer(serializers.ModelSerializer):
    course_name = serializers.SerializerMethodField()
    faculty_name = serializers.SerializerMethodField()

    class Meta:
        model = Timetable
        fields = ['id', 'day', 'start_time', 'end_time', 'course', 'faculty', 'course_name', 'faculty_name','created_at']

    def get_course_name(self, obj):
        return obj.course.name if obj.course else None

    def get_faculty_name(self, obj):
        return obj.faculty.name if obj.faculty else None

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()
    start_time = serializers.SerializerMethodField()
    timetable = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'course', 'timetable', 'date', 'status', 'student_name', 'course_name', 'start_time', 'end_time']

    def get_student_name(self, obj):
        return obj.student.name if obj.student else None

    def get_timetable(self,obj):
        return obj.timetable.start_time if obj.timetable else None
    
    def get_course_name(self, obj):
        return obj.course.name if obj.course else None

    def get_start_time (self,obj):
        return obj.timetable.start_time if obj.timetable else None
    def get_end_time (self,obj):
        return obj.timetable.end_time if obj.timetable else None
    
    def create(self, validated_data):
        timetable_data = validated_data.get('timetable')  # Extract timetable data
        print(timetable_data)
        timetable_id = timetable_data.pop('id')  # Extract timetable ID

        # Create the Attendance object without the timetable field
        attendance = Attendance.objects.create(**validated_data)

        # Associate the timetable with the Attendance object
        timetable = Timetable.objects.get(id=timetable_id)
        attendance.timetable = timetable
        attendance.save()

        return attendance

class TestScheduleSerializer(serializers.ModelSerializer):
    faculty_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()
    students = UserSerializer(many=True, read_only=True, source='classroom.students')


    class Meta:
        model = TestSchedule
        fields = ['id', 'faculty', 'course', 'date', 'start_time' , 'end_time','faculty_name', 'course_name','students'] 

    def get_faculty_name(self, obj):
        return obj.faculty.name if obj.faculty else None

    def get_course_name(self, obj):
        return obj.course.name if obj.course else None

class StudentPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPerformance
        fields = '__all__'

    