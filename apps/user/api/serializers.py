from rest_framework import serializers

from apps.faculty.api.serializers import AcademicGroupSerializer, FacultySerializer
from apps.user.models import Student, Teacher, DeaneryOfficer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'faculty', 'group', )

    group = AcademicGroupSerializer()
    faculty = FacultySerializer()


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'department', )


class DeaneryOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeaneryOfficer
        fields = ('id', 'first_name', 'last_name',)
