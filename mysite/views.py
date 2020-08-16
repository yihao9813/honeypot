from django.shortcuts import render, redirect
from django.contrib import auth

def index(request):
    context = {}
    response = render(request, 'index.html', context)
    return response

def login(request):
    # ''代表若获取不到username则默认为空
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return render(request, 'success.html', {'message':'登陆成功'})
    else:
        return render(request, 'error.html', {'message':'用户名或密码不正确'})

def error(request):
    context = {}
    response = render(request, 'index.html', context)
    return response