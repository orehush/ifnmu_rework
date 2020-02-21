from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from model_mommy.recipe import mommy

from apps.department.models import Department


class DepartmentTestCase(APITestCase):
    def setUp(self):
        mommy.make(Department)
        token = mommy.make(Token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_list_departments(self):
        r = self.client.get('/api/departments/')
        body = r.json()
        self.assertEqual(r.status_code, 200, body)
        self.assertEqual(len(body), 1, body)
