from django.test import TestCase
from django.test.client import RequestFactory
from django.test.testcases import TransactionTestCase
from django.test import Client

from .views import DuplicatorView
from sandboxcc6401.models import DuplicatorNumber


class TestDuplicatorView(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        DuplicatorNumber.objects.all().delete()

    def test_check_200(self):
        response = self.client.get('/duplicator')
        self.assertEquals(200, response.status_code)
        
    def test_number_exists(self):
        response = self.client.get('/duplicator')
        n = DuplicatorNumber.objects.first()
        self.assertEquals(1, n.number)
        
    def test_duplicate(self):
        response = self.client.get('/duplicator')
        n = DuplicatorNumber.objects.first()
        n.duplicate()
        self.assertNotEquals(1, n.number)
        
    def test_post_duplicate(self):
        response = self.client.get('/duplicator')
        response = self.client.post('/duplicator')
        
        n = DuplicatorNumber.objects.first()
        self.assertEquals(2, n.number)
        
    def test_post_n_duplicate(self):
        response = self.client.get('/duplicator')
        
        import random
        times = random.randint(1, 9)
        for _ in range(times):
            response = self.client.post('/duplicator')
        
        n = DuplicatorNumber.objects.first()
        self.assertEquals(2 ** times, n.number)
        
    def test_parallel_access(self):
        # they should see the number at 1
        r1 = self.client.get('/duplicator')
        n1 = DuplicatorNumber.objects.first()
        self.assertEquals(1, n1.number)
        
        r2 = self.client.get('/duplicator')
        n2 = DuplicatorNumber.objects.first()
        self.assertEquals(1, n2.number)
        
        # both users duplicate their numbers
        self.client.post('/duplicator')
        self.client.post('/duplicator')
        
        # check that the number is 4 now
        r1 = self.client.get('/duplicator')
        n1 = DuplicatorNumber.objects.first()
        self.assertEquals(4, n1.number)
        
        r2 = self.client.get('/duplicator')
        n2 = DuplicatorNumber.objects.first()
        self.assertEquals(4, n2.number)