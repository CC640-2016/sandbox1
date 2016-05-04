from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_number, name='index'),
    url(r'^duplicar/', views.duplicate_number, name='duplicate_number')
]