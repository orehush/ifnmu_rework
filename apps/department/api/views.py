from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.department.api.serializers import DepartmentSerializer
from apps.department.models import Department


class DepartmentViewSet(ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = None
