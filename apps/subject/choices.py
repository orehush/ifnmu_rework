from django.db.models import Choices


class ReworkStatus(Choices):
    CREATED = 10
    APPROVED = 20
    REJECTED = 30
    REWORKED = 40
    EXPIRED = 50
