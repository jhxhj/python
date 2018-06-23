from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

def index(request):
    return  HttpResponse('Hello This is polls.')

def hello(request):
    return  HttpResponse('This is hello world')


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include("polls.urls")),
    url(r'^$', index),
    url(r'^hello/$', hello),
    url(r'^admin/', include(admin.site.urls)),
]
