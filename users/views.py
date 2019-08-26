from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def login(request):
    context = dict()
    if request.method == 'POST':
        print("Using post method")
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            context['error'] = "Wrong username/password"
            return render(request, 'users/login.html', context=context)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return HttpResponseRedirect(reverse('contact:index'))
        context["error"] = "invalid credentials"
    return render(request, 'users/login.html', context=context)

def signup(request):
    context = dict()
    if request.method == 'POST':
        print("Using post method")
        try:
            username = request.POST['username']
            password = request.POST['password']
            confirm_password = request['confirm_password']
        except KeyError:
            context['error'] = "Wrong username/password"
            return render(request, 'users/signup.html', context=context)
        if password != confirm_password:
            context['message'] = "Passwords Do not match!"
            return render(request, 'users/signup.html', context=context)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return HttpResponseRedirect(reverse('contact:index'))
        context["error"] = "invalid credentials"
    return render(request, 'users/signup.html', context=context)

def logout(request):
    return HttpResponse("Logout here")
