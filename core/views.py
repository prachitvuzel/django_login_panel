from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 != pass2:
            return HttpResponse("Password Mismatched, Please Try Again")
        else:
            user = User.objects.create_user(
                username=username, email=email, password=pass1)
            user.save()
            return redirect('login')

    else:
        return render(request, 'signup.html')


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Password or Username is incorrect")
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')