from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.db import transaction

from sandboxcc6401.models import DuplicatorNumber


class DuplicatorView(TemplateView):
    
    @transaction.atomic
    def get(self, request, *k, **ka):
        n = DuplicatorNumber.objects.filter(pk=1)
        if not n:
            n = DuplicatorNumber()
            n.pk = 1
            n.number = 1
            n.save()
        else:
            n = n[0]
            
        return render(request, 'sandboxcc6401/duplic.html', {"number_project": n})
        
    @transaction.atomic
    def post(self, request, *k, **ka):
        n = DuplicatorNumber.objects.filter(pk=1)
        n = n[0]
        n.duplicate()
            
        return render(request, 'sandboxcc6401/duplic.html', {"number_project": n})