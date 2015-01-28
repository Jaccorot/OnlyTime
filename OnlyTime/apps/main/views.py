#!/usr/local/bin/python
#coding=utf-8

import datetime

from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.views.generic import TemplateView, CreateView
from django.utils import timezone
from django.core.urlresolvers import reverse


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['current_time'] = timezone.localtime(timezone.now())
        return context


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')


def login(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            return HttpResponseRedirect("/register")

        else:
            userName = request.POST['name'] 
            passWord = request.POST['password']  
            user = authenticate(username = userName, password = passWord)
            if not user: 
                return render_to_response("login_result.html", {"msg":"用户名或者密码错误哦~~"})
            return render_to_response("login_result.html", { "user": user})
    return render_to_response('login.html', context_instance=RequestContext(request)) 


def alogout(request):
    logout(request)
    return HttpResponseRedirect('/register')
