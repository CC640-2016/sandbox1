from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Numero(models.Model):
    number = models.IntegerField(default=1)
