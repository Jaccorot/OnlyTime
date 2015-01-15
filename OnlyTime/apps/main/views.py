#!/usr/local/bin/python
#coding=utf-8

from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.template.context import RequestContext

import datetime

def index_page(request):
    now = datetime.datetime.now()
    current_time = now.strftime('%Y%m%d')
    return render(request,'base.html',{'current_time':current_time})

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
