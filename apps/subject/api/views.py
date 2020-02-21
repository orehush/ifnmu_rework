from rest_framework import permissions, mixins
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.subject.api.serializers import (
    SubjectSerializer, ReworkCreateSerializer, ReworkSerializer,
)
from apps.subject.models import Subject, Rework
from apps.subject.api.permissions import ReworkPermission


class SubjectViewSet(ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (permissions.IsAuthenticated, )
    # TODO add filters


class ReworkViewSet(ReadOnlyModelViewSet, mixins.CreateModelMixin):
    queryset = Rework.objects.all()
    serializer_class = ReworkSerializer
    permission_classes = (ReworkPermission, )
    # TODO add filters

    def get_serializer_class(self):
        if self.action == 'create':
            return ReworkCreateSerializer
        return self.serializer_class
