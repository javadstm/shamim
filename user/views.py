from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import AddUserForm


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('listcenter')
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)


def AddUser(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'creating user compeleted')
            return redirect(reverse("edituser", ) + "?message=user succesfully created")
    else:
        form =AddUserForm()
    return render(request, 'adduser.html', {'form': form})


def UserList(request):
    users = User.objects.all()
    messege = request.GET.get('message')
    context = {'users': users, 'message': messege}

    return render(request, 'userlist.html', context)


@login_required(login_url='login')
def EditUser(request, pk):
    user = User.objects.get(id=pk)

    if request.method == 'POST':
        form = AddUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'editting user compeleted')
            return redirect(reverse("userlist", ) + "?message=changes done successfully")
    else:
        messege = request.GET.get('message')
        form = AddUserForm(instance=user)
    return render(request, 'edituser.html', context={'form': form, 'user': user, 'message': messege})


@login_required(login_url='login')
def DeleteUser(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    if request.method == 'POST':
        User.delete()
        messages.success(request, 'user deleted')
        return redirect('userlist')
    return render(request, 'deleteuser.html', context)
