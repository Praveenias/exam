from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('newuser',views.newuser,name='newuser'),
    path('login',views.login,name='login')
]