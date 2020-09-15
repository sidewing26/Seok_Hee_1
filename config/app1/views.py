from django.shortcuts import render, redirect
from .models import Myuser
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password # 자동 암호화, 비밀번호 체크 기능
from .forms import LoginForm


# Create your views here.

def index(request):

    return render(request, 'index.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        password_confirm = request.POST.get('password_confirm', None)

        res_data = {}

        if not (username and password and password_confirm):
            res_data['error']='모두 입력해주세요'
        elif password != password_confirm:
            res_data['error']='비밀번호 불일치'
        else:
            myuser = Myuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            myuser.save()
            return render(request, 'signup_done.html')
        return render(request, 'signup.html', res_data)


def signup_done(request):

    return render(request, 'signup_done.html')

def login(request):
    if request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form=LoginForm()
    return render(request, 'login.html', {'form':form})

def logout(request):
    if request.session.get('user'): 
        del(request.session['user']) 
    return redirect('/')