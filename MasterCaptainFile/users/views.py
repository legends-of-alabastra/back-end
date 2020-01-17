from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)

        if user is not None:
            messages.info(request, "Success!")
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
            
            

    else:
        return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username Taken")
            print('Username taken')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email Taken")
            print('Email taken')
        else:
            user = User.objects.create_user(username=username, email = email, password = password)
            user.save()
            print('user created')
            return redirect('login')
    else:
        return render(request, 'users/register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')