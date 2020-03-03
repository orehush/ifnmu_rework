from django.db import models


class Faculty(models.Model):
    class Meta:
        verbose_name_plural = 'Faculties'

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class AcademicGroup(models.Model):
    name = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.course}'
