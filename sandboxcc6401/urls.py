from django.conf.urls import include, url
from django.contrib import admin

from duplicador.views import DuplicadorView


urlpatterns = [
    # Examples:
    # url(r'^$', 'sandboxcc6401.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^duplicador/', include('duplicador.urls')),
    url(r'^duplicador$', DuplicadorView.as_view(), name='duplicador'),
    url(r'^$', include('duplicador.urls')),
]
