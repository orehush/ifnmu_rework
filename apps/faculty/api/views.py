from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.faculty.api.serializers import FacultySerializer, CourseSerializer
from apps.faculty.models import Faculty, Course


class FacultyViewSet(ReadOnlyModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.IsAuthenticated, )


class CourseViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated, )
