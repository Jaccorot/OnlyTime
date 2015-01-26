#!/usr/local/bin/python
#coding=utf-8

import datetime

from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.views.generic import TemplateView, CreateView
from django.utils import timezone
from django.core.urlresolvers import reverse

from .froms import CreateUserForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['current_time'] = timezone.localtime(timezone.now())
        return context


class RegisterView(TemplateView):
    template_name = 'register.html'
    form_class = CreateUserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.clean_data['password'])
        self.object = form.save()
        return super(RegisterView, self).form_valid(form)

    def get_success_url(self):
        return reverse('login')


def register(request):
    if request.method == 'POST':
        userName = request.POST['name']  
        passWord = request.POST['password']  
        #user = User(name=userName, password=passWord)
        user = User.objects.create_user(username= userName, password= passWord)
        user.save()  
        return render_to_response("register_result.html", { "user": user})  
    return render_to_response("register.html", context_instance=RequestContext(request))


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
