from django.conf.urls import patterns, include, url

from django.contrib import admin

from OnlyTime.apps.main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OnlyTime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/', views.IndexView.as_view(), name='index_page'),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^relogin/', 'django.contrib.auth.views.logout_then_login', name='relogin'),
    url(r'^register/', views.RegisterView.as_view(), name='register'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),    
)