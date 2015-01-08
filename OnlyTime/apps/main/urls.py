from django.conf.urls import patterns, include, url

from django.contrib import admin

from OnlyTime.apps.main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OnlyTime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index_page, name ='index_page'),
)
