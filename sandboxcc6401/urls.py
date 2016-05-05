from django.conf.urls import include, url
from django.contrib import admin

from sandboxcc6401.views import DuplicatorView

urlpatterns = [
    # Examples:
    # url(r'^$', 'sandboxcc6401.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^duplicator$', DuplicatorView.as_view(), name='duplicator'),
    # url(r'',DuplicatorView.as_view())

]
