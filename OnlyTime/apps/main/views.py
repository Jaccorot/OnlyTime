from django.shortcuts import render,render_to_response
from django.contrib.auth.models inport User
import datetime

def index_page(request):
    now = datetime.datetime.now()
    current_time = now.strftime('%Y%m%d')
    return render(request,'base.html',{'current_time':current_time})

def alogin(request):
    errors = []
    account = None
    password = None
    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('Please Enter account')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors.append('Please Enter password')
        else:
            password = request.POST.get('password')

        if account is not None and password is not None:
            user = authenticate(username=account,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    error.append('disabled account')
            else:
                errors.append('invalid user')
        return render_to_response('account/login.html',{'errors':errors})

def register(request):
    errors = []
    account = None
    password = None
    password2 = None
    email = None
    compare_flag = False

    if request.methon == 'POST':
        if not request.POST.get('account'):
            errors.append('Please Enter account')
        else:
            account = request.POST.get('account')
        
        if not request.POST.get('password'):
            errors.append('Please Enter password')
        else:
            password= request.POST.get('password')

        if not request.POST.get('password2'):
            errors.append('Please Enter password2')
        else:
            password2= request.POST.get('password2')

        if not request.POST.get('email'):
            errors.append('Please Enter email')
        else:
            email= request.POST.get('email')
        if password is not None and password2 is not None:
            if password == password2:
                compare_flag = True
            else :
                errors.append('password2 is diff password ')
        if account is not None and password is not None and password2 is not None 
            and email is not None and compare_flag :
            user = User.objects.create_user(account,email,password)
            user.is_active=True
            user.save
            return HttpResponseRedirect('/account/login')
        return render_to_response('account/register.html', {'errors': errors})
def alogout(request):
    logout(request)
    return HttpResponseRedirect('/')
