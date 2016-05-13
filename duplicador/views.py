from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template import loader
from django.test import Client

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
    

class Vista(View):
    def get(self,request):
        self.client = Client()
        actual_number = self.client.get('/valor').content
        template = loader.get_template('Vista/duplicator.html')
        context = {
            'numero': actual_number,
        }
        return HttpResponse(template.render(context, request))
        
    def post(self,request):
        self.client = Client()
        response = self.client.post('/valor', {'action': 'duplicar'})
        actual_number = self.client.get('/valor').content
        template = loader.get_template('Vista/duplicator.html')
        context = {
            'numero': actual_number,
        }
        return HttpResponse(template.render(context, request))
        

        
        
    
    
