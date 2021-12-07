from django.urls import path
from .views import login_request, AddUser, UserList, EditUser

urlpatterns = [
    path('login/', login_request, name='login'),
    path('add/', AddUser, name='adduser'),
    path('list/', UserList, name='userlist'),
    path('edit/<str:pk>', EditUser, name='edituser'),
    path('delete/<str:pk>', UserList, name='userlist'),

]
