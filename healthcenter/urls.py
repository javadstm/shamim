from django.urls import path
from .views import home, sign_out

urlpatterns = [
    path('', home, name='home'),
    path('logout', sign_out, name='logout'),
]
