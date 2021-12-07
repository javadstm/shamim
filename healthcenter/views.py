from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateCenterform
from django.contrib import messages
from .models import HealthCenterModels, city, state
from .filters import healthfilter
from django.urls import reverse
from django.core.paginator import Paginator


# Create your views here.


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
            pk = instance.id
            return redirect(reverse("editcenter", kwargs={'pk': str(pk)}) + "?message=center succesfully submitted")

    else:
        form = CreateCenterform()

    return render(request, 'addcenter.html', {'form': form})


@login_required(login_url='login')
def centerlist(request):
    centers = HealthCenterModels.objects.all().order_by('created_by_id')
    search = healthfilter(request.GET, queryset=centers)
    centers = search.qs
    centerpaginator = Paginator(centers, 10)
    page_num = request.GET.get('page')
    page = centerpaginator.get_page(page_num)
    context = {'centers': centers, 'search': search, 'page': page}
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
            return redirect('listcenter')
    else:
        messege = request.GET.get('message')
        form = CreateCenterform(instance=center)
    return render(request, 'editcenter.html', context={'form': form, 'center': center, 'message': messege})


@login_required(login_url='login')
def DeleteCenter(request, pk):
    center = HealthCenterModels.objects.get(id=pk)
    context = {'center': center}
    if request.method == 'POST':
        center.delete()
        messages.success(request, 'center deleted')
        return redirect('listcenter')
    return render(request, 'deletecenter.html', context)
