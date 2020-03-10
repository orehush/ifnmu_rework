from django.contrib import admin

from apps.faculty.models import Faculty, Course, AcademicGroup

admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(AcademicGroup)
