from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject)
    faculty = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE, related_name='courses_taught')

    
    
    def __str__(self):
        return self.name
