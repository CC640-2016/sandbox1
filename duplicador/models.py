from __future__ import unicode_literals

from django.db import models

class ValorModel(models.Model):
    valor = models.IntegerField(default=1)
    