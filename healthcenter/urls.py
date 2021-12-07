from django.urls import path
from .views import sign_out, new_Center, centerlist, load_cities, EditCenter, DeleteCenter

urlpatterns = [
    path('logout', sign_out, name='logout'),
    path('addcenter', new_Center, name='addcenter'),
    path('', centerlist, name='listcenter'),
    path('editcenter/<str:pk>', EditCenter, name='editcenter'),
    path('deletecenter/<str:pk>', DeleteCenter, name='deletecenter'),

    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]
