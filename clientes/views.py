from django.shortcuts import render
import datetime
from clientes.models import Cliente
# Create your views here.

def home (request):
    now_tiem  = datetime.datetime.now()

    return render(request,'clientes/home.html')

def list (request):
    data = {}
    data['clientes'] = Cliente.objects.all()
    return render(request,'clientes/list.html', data)
