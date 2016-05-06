from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from . import models

# int valor = 1


class Numero(View):
    def get(self,request):
        (valor, created) = models.ValorModel.objects.get_or_create(pk=1)
        return HttpResponse(str(valor.valor))

    def post(self,request):
        action = request.POST.get("action")
        if action == 'duplicar':
            (valor, created) = models.ValorModel.objects.get_or_create(pk=1)
            valor.valor=(2*valor.valor)
            valor.save()
        return HttpResponse()
    

    
    
