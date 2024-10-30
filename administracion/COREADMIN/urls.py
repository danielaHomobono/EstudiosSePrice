from django.urls import include
from django.contrib import admin
from django.urls import path
from coreadmin import views

urlpatterns = [
    path('admin/', views.index),
    path('gestion_estudios', views.gestion_estudios),
]