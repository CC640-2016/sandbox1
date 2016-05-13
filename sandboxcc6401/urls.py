from django.conf.urls import include, url
from django.contrib import admin
from duplicador.views import Numero
from duplicador.views import Vista
urlpatterns = [
    # Examples:
    # url(r'^$', 'sandboxcc6401.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^valor$', Numero.as_view()),
    url(r'^program$', Vista.as_view()),
]