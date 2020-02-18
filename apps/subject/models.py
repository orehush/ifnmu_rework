from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.department.models import Department
from apps.faculty.models import Course, Faculty
from apps.subject.choices import ReworkStatus
from apps.user.models import Student, DeaneryOfficer, Teacher


class Subject(models.Model):
    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Rework(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    officer = models.ForeignKey(DeaneryOfficer, on_delete=models.SET_NULL,
                                null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,
                                null=True, blank=True)
    comment = models.TextField(max_length=500, blank=True)
    document = models.ImageField(upload_to='%Y/%m')
    status = models.PositiveSmallIntegerField(
        choices=ReworkStatus.choices, default=ReworkStatus.CREATED,
    )
