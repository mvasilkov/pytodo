from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('pytodo.main.views',
    url(r'^$', 'home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
