from django.db import models
from courses.models import Course
from authentication.models import CustomUser
from classroom.models import ClassroomModel

# Create your models here.
class Timetable(models.Model):
    day = models.CharField(max_length=20)
    
    created_at = models.DateTimeField( auto_now_add = True,blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassroomModel, on_delete=models.CASCADE)
    faculty = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_faculty': True},related_name='timetables')

    def __str__(self):
        return self.course.name
class Attendance(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    timetable = models.ForeignKey(Timetable,on_delete=models.CASCADE)
    status = models.CharField(max_length=10)  

class TestSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    faculty = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_faculty': True}, related_name='test_schedules')
    classroom = models.ForeignKey(ClassroomModel, on_delete=models.CASCADE, null=True, blank=True)

class StudentPerformance(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    test = models.ForeignKey(TestSchedule, on_delete=models.CASCADE)
    score = models.FloatField()
    date = models.DateField()
    
    
    

