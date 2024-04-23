# classrooms/models.py
from django.db import models
from authentication.models import CustomUser
from courses.models import Course

class ClassroomModel(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(CustomUser, related_name='classrooms_students')
    faculty = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_faculty': True}, related_name='classrooms_faculty')

    def __str__(self):
        return f"{self.course.name} Classroom"
