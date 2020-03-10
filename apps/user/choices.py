from django.db import models


class UserType(models.IntegerChoices):
    STUDENT = 10
    OFFICER = 20
    TEACHER = 40
