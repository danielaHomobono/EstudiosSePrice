from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("Hello, world. You're at the login.")

def gestion_estudios(request):
    return HttpResponse("Hello, world. You're at the gestion_estudios.")