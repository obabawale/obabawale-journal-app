from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

def login_view(request):
    context = dict()
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            context['error'] = "Wrong username/password"
            return render(request, 'users/login.html', context=context)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('journal:index',))
        context["error"] = "invalid credentials"
    return render(request, 'users/login.html', context=context)

def signup_view(request):
    context = dict()
    if request.method == 'POST':
        print("Using post method")
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
        except KeyError:
            context['error'] = "Invalid input"
            return render(request, 'users/signup.html', context=context)
        if password != confirm_password:
            context['message'] = "Passwords Do not match!"
            return render(request, 'users/signup.html', context=context)
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('journal:index',))
        context["error"] = "invalid credentials"
    return render(request, 'users/signup.html', context=context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("journal:index"))
