from django.db import models
from django.utils import timezone

class DuplicatorNumber(models.Model):
    number = models.BigIntegerField(1)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def create(self):
        self.number = 1
        self.save()
        
    def duplicate(self):
        self.number=self.number*2
        self.save()
        
    def __str__(self):
        return str(self.number)