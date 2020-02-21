from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from model_mommy.recipe import mommy

from apps.faculty.models import Faculty, Course


class FacultyTestCase(APITestCase):
    def setUp(self):
        mommy.make(Faculty)
        token = mommy.make(Token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_list_faculties(self):
        r = self.client.get('/api/faculties/')
        body = r.json()
        self.assertEqual(r.status_code, 200, body)
        self.assertEqual(len(body), 1, body)


class CourseTestCase(APITestCase):
    def setUp(self):
        mommy.make(Course)
        token = mommy.make(Token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_list_courses(self):
        r = self.client.get('/api/courses/')
        body = r.json()
        self.assertEqual(r.status_code, 200, body)
        self.assertEqual(len(body), 1, body)
