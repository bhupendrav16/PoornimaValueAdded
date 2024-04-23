from django.contrib import admin
from .models import Subject,Branch,Semester, Course

admin.site.register(Subject)
admin.site.register(Branch)
admin.site.register(Course)
admin.site.register(Semester)