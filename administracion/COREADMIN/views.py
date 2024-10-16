from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'coreadmin/index.html')

def gestion_estudios(request):
    return render(request, 'coreadmin/gestion_estudios.html', 

        )