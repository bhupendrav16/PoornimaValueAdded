from django.contrib import admin
from .models import Attendance, Timetable ,TestSchedule,StudentPerformance
# Register your models here.
admin.site.register(Attendance)
admin.site.register(Timetable)
admin.site.register(TestSchedule)
admin.site.register(StudentPerformance)