from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as l
from django.http import HttpResponse, HttpResponseNotFound
from .models import User


def register(request):
    template_name = '../templates/newlogin.html'

    context = {
    }
    if request.user.is_authenticated:
        return HttpResponseForbidden('User is already loged in')

    if request.method == 'POST':
        firstname = request.POST['firstname']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        avatar = request.FILES.get('avatar')
        user = User.objects.create(firstname=firstname, surname=surname, email=email, password=password, avatar=avatar)
        login(user=user, request=request)
        return redirect('/account/')

    return render(request, template_name, context)


def new_login(request):
    template_name = '../templates/login.html'

    context = {
    }

    if request.user.is_authenticated:
        return HttpResponseForbidden('User is already loged in')

    if request.method == 'POST':
        print(request.POST)
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.get(email=email, password=password)
        login(user=user, request=request)
        if user:
            login(user=user, request=request)
            return redirect('/account/')

    return render(request, template_name, context)
    

def logout(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden('User is not loged in')
    l(request)
    return redirect('/')


def change(request):
    template_name = '../templates/accountchange.html'

    context = {
    }

    if not request.user.is_authenticated:
        return HttpResponseForbidden('User is not loged in')

    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        user.firstname = request.POST['firstname']
        user.surname = request.POST['surname']
        user.email = request.POST['email']
        user.set_password(request.POST['password'])
        user.avatar = request.FILES.get('avatar')
        user.save()
        login(user=user, request=request)

    return render(request, template_name, context)


def account(request):
    template_name = '../templates/account.html'

    context = {
        'user': request.user,}

    if not request.user.is_authenticated:
        return HttpResponseForbidden('User is not loged in')


    return render(request, template_name, context)