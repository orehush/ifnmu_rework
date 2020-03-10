from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.department.models import Department
from apps.faculty.models import Faculty, AcademicGroup
from apps.user.choices import UserType


class User(AbstractUser):
    type = models.PositiveSmallIntegerField(
        choices=UserType.choices, null=True, blank=True)

    # student's fields
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(
        AcademicGroup, on_delete=models.CASCADE, null=True, blank=True)

    # teacher's fields
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.get_full_name() or self.get_username()

    def is_student(self):
        return self.type == UserType.STUDENT.value

    def is_officer(self):
        return self.type == UserType.OFFICER.value

    def is_teacher(self):
        return self.type == UserType.TEACHER.value
