from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateCenterform
from django.contrib import messages
from .models import HealthCenterModels, city, state
from .filters import healthfilter
from django.urls import reverse

# Create your views here.


@login_required(login_url='login')
def home(requset):
    return render(requset, 'home.html')


@login_required(login_url='login')
def sign_out(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def new_Center(request):
    if request.method == 'POST':
        form = CreateCenterform(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.created_by = request.user
            instance.save()
            messages.success(request, 'creating center compeleted')
            return reverse('editcenter', pk=[instance.id])

    else:
        form = CreateCenterform()

    return render(request, 'addcenter.html', {'form': form})


@login_required(login_url='login')
def centerlist(request):
    centers = HealthCenterModels.objects.all()
    search = healthfilter(request.GET, queryset=centers)
    centers = search.qs
    context = {'centers': centers, 'search': search}
    return render(request, 'list.html', context)


def load_cities(request):
    state_id = request.GET.get('state')
    cities = city.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'hr/city_dropdown_list_options.html', {'cities': cities})


@login_required(login_url='login')
def EditCenter(request, pk):
    center = HealthCenterModels.objects.get(id=pk)

    if request.method == 'POST':
        form = CreateCenterform(request.POST, instance=center)
        if form.is_valid():
            form.save()
            messages.success(request, 'editting center compeleted')
    else:
        form = CreateCenterform(instance=center)
    return render(request, 'editcenter.html', context={'form': form, 'center': center})


def DeleteCenter(request, pk):
    center = HealthCenterModels.objects.get(id=pk)
    context = {'center': center}
    if request.method == 'POST':
        center.delete()
        messages.success(request, 'center deleted')
        return redirect('listcenter')
    return render(request, 'deletecenter.html', context)
