from django.contrib.auth.models import User
from django.db import models

from apps.department.models import Department
from apps.faculty.models import Faculty, AcademicGroup


class Student(User):
    class Meta:
        verbose_name = 'Student'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)


class DeaneryOfficer(User):
    class Meta:
        verbose_name = 'Officer'


class Teacher(User):
    class Meta:
        verbose_name = 'Teacher'

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
