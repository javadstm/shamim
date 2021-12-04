from django.urls import path
from .views import home, sign_out, new_Center,centerlist

urlpatterns = [
    path('', home, name='home'),
    path('logout', sign_out, name='logout'),
    path('addcenter', new_Center, name='addcenter'),
    path('listcenter',centerlist,name='listcenter')
]
