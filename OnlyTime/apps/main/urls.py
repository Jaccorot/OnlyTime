from django.conf.urls import patterns, include, url

from django.contrib import admin

from OnlyTime.apps.main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OnlyTime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/', views.IndexView.as_view(), name='index_page'),
    url(r'^login/',views.login, name='login'),
    url(r'^register/',views.register, name='register'),
)