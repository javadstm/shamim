from django.urls import path
from .views import login_request

urlpatterns = [
    path('login/', login_request, name='login'),
]
