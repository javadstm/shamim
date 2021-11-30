from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def home(requset):
    return render(requset, 'home.html')


def sign_out(request):
    logout(request)
    return redirect('/')
