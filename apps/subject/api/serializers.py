from rest_framework import serializers

from apps.subject.models import Subject, Rework
from apps.user.api.serializers import (
    StudentSerializer, DeaneryOfficerSerializer, TeacherSerializer,
)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', )


class ReworkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rework
        fields = ('student', 'subject', 'document', )


class ReworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rework
        fields = '__all__'

    subject = SubjectSerializer()
    student = StudentSerializer()
    officer = DeaneryOfficerSerializer()
    teacher = TeacherSerializer()
