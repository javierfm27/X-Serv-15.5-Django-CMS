from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pepito', views.pepito, name='Prueba de una pagina pedida llamada pepito guardada en la base'),
    url(r'^(.+App$)', views.base, name='Pagina que accede a los datos'),
    url(r'^admin/', include(admin.site.urls)),
)
