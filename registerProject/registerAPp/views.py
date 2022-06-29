from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Person

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')

        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if password == confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist.')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already in use.')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        elif (password and confirmPassword) < 8:
                messages.error(request, 'Password must be at least 8 characters long.')
                return redirect('signup')
        else:
            messages.error(request, 'Passwords does not match.')
            return redirect('signup')

    return render(request, 'signup.html')


def dashboard(request):
    messages.success(request, "Login successful.")
    return render(request, 'dashboard.html')


def logout(request):
    return render(request, 'logout.html')
