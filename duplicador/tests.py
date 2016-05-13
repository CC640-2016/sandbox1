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
        
    def test_duplicar_valor(self):
        # Arrange
        response = self.client.get('/valor')
        self.assertEquals("1",response.content)
        
        # Act
        response2 = self.client.post('/valor', {'action': 'duplicar'})
        
        # Assert
        self.assertEquals(200, response.status_code)
        self.assertEquals('2', self.client.get('/valor').content)
        
    def test_post_n_duplicate(self):
        response = self.client.get('/valor')
        
        import random
        times = random.randint(1, 9)
        for _ in range(times):
            response = self.client.post('/valor', {'action': 'duplicar'})
        
        response2 = self.client.get('/valor')
        n = int(response2.content)
        self.assertEquals(2 ** times, n)
        
    def test_duplicate_from_vista(self):
        response = self.client.get('/valor')
        import random
        times = random.randint(1, 9)
        for _ in range(times):
            response = self.client.post('/program', {})
        response2 = self.client.get('/valor')
        n = int(response2.content)
        self.assertEquals(2 ** times, n)
        
    def test_reset_valor(self):
        # Arrange
        self.client.post('/valor', {'action': 'duplicar'})
    
        # Act
        response = self.client.post('/valor', {'action': 'reset'})
        
        # Assert
        response2=self.client.get('/valor')
        self.assertEquals(200, response2.status_code)
        self.assertEquals('1', response2.content)
