from django.test import TestCase
from django.test.client import RequestFactory
from django.test.testcases import TransactionTestCase
from django.test import Client

from .views import DuplicadorView


class TestLoginFormView(TransactionTestCase):

    def setUp(self):
        self.client = Client()

    def test_check_200(self):
        response = self.client.get('/duplicador')
        self.assertEquals(200, response.status_code)
        self.assertEquals('hola666', response.content)
