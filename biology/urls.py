from django.urls import path
from . import views

urlpatterns = [
    path('',views.biology,name='maths'),
    path('thank',views.thank,name='thank')
]