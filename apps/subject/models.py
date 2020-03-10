from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.department.models import Department
from apps.faculty.models import Course, Faculty
from apps.subject.choices import ReworkStatus


class Subject(models.Model):
    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.name} - {self.department}'


class Rework(TimeStampedModel):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='my_reworks'
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    officer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='approved_reworks'
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='accepted_reworks',
    )
    comment = models.TextField(max_length=500, blank=True)
    document = models.ImageField(upload_to='%Y/%m')
    status = models.PositiveSmallIntegerField(
        choices=ReworkStatus.choices,
        default=ReworkStatus.CREATED.value,
    )
