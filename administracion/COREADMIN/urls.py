from django.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login (name= 'login')),
    path('gestion/estudios', views.gestion_estudios (name= 'gestion_estudios'))
]