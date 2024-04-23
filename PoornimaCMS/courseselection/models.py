from django.db import models

# Create your models here.
from django.db import models
from authentication.models import CustomUser
from courses.models import Course

class UserCourseSelection(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user.name}  {self.course.name}"