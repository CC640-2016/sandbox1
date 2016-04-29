from django.shortcuts import render

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse



class DuplicadorView(TemplateView):
    
    def get(self, request, *k, **ka):
        return HttpResponse('hola666')
