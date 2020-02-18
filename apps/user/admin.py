from django.contrib import admin

from apps.user.models import Student, Teacher, DeaneryOfficer

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(DeaneryOfficer)
