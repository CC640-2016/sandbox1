from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from models import Numero


# Master, clase pasada

class DuplicadorView(TemplateView):
    
    def get(self, request, *k, **ka):
        return HttpResponse('hola666')
        
# Create your views here.

def show_number(request):
    num = Numero.objects.filter(number=1)
    if len(num)==0:
        num = Numero(number=1)
        num.save()
    else:
        num = num[0]
        
    context = {'numero': num}
    return render(request, 'duplicador/index.html', context)
    

def duplicate_number(request):
    num = Numero.objects.all()[0]
    num.number = num.number*2
    num.save()
    
    context = {'numero': num}
    return render(request, 'duplicador/index.html', context)
