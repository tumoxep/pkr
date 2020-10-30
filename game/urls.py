from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('auth/', auth_views.LoginView.as_view(), name='auth'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('list_rooms/', views.list_rooms, name='list_rooms'),
]
