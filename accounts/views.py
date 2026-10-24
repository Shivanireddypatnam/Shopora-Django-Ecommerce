from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_protect
# Create your views here.

def sign_up(request):
    if request.method=='POST':
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            # Username already exists, render form with error
            return render(request, 'accounts/signup.html', {"error": "Usename already exists. Please choose a different one."}) 
        user = User.objects.create_user(
            username=username,
            password=request.POST['password']
        )                                                  

        Profile.objects.create(
            name=request.POST["name"],
            user=user,
            phone_no=request.POST['phone_no'],
            country=request.POST['country']
        )
        return redirect('login')
    return render(request, 'accounts/signup.html')


def login(request):
    if request.method=='POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {"error": "Invalid username or password."})
    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect("login")



