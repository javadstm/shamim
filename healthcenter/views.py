from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateCenterform
from django.contrib import messages
from .models import HealthCenterModels
from .filters import healthfilter


# Create your views here.

@login_required(login_url='login')
def home(requset):
    return render(requset, 'home.html')


def sign_out(request):
    logout(request)
    return redirect('/')


def new_Center(request):
    if request.method == 'POST':
        form = CreateCenterform(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.manager = request.user
            instance.save()
            messages.success(request, 'creating center compeleted')
            return redirect('home')

    else:
        form = CreateCenterform()

    return render(request, 'addcenter.html', {'form': form})


def centerlist(request):
    centers = HealthCenterModels.objects.all()
    search = healthfilter(request.GET, queryset=centers)
    centers = search.qs
    context = {'centers': centers, 'search': search}
    return render(request, 'list.html', context)
