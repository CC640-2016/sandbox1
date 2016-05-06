from django.test import TestCase
from django.test.client import RequestFactory
from django.test.testcases import TransactionTestCase
from django.test import Client

# from .views import DuplicatorView


class TestDuplicator(TransactionTestCase):

    def setUp(self):
        self.client = Client()

    def test_get_valor(self):
        response = self.client.get('/valor')
        self.assertEquals(200, response.status_code)
        self.assertEquals("1",response.content)
        
    