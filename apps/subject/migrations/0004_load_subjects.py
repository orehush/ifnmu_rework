# Generated by Django 3.0.3 on 2020-03-03 08:54

import csv
import os
from collections import defaultdict

from django.db import migrations

from apps.department.models import Department
from apps.faculty.models import Faculty, Course
from apps.subject.models import Subject


def load_data(*args):
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'subjects.csv'
    )

    faculties = {}
    departments = {}
    courses = {
        '1': Course.objects.get_or_create(name='1')[0],
        '2': Course.objects.get_or_create(name='2')[0],
        '3': Course.objects.get_or_create(name='3')[0],
        '4': Course.objects.get_or_create(name='4')[0],
        '5': Course.objects.get_or_create(name='5')[0],
        '6': Course.objects.get_or_create(name='6')[0],
    }

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in list(csv_reader)[1:]:
            faculty_name, department_name, subject_name, courses_name = row

            if faculty_name not in faculties:
                faculties[faculty_name] = Faculty.objects.get_or_create(
                    name=faculty_name
                )[0]
            faculty = faculties[faculty_name]

            if department_name not in departments:
                departments[department_name] = Department.objects.get_or_create(
                    name=department_name
                )[0]
            department = departments[department_name]

            subject = Subject.objects.get_or_create(
                faculty=faculty,
                department=department,
                name=subject_name
            )[0]

            for course in courses_name.split(','):

                subject.courses.add(courses[course])


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_auto_20200303_0854'),
    ]

    operations = [
        migrations.RunPython(load_data, lambda *args: None)
    ]