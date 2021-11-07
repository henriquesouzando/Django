from django.shortcuts import render
import datetime
# Create your views here.

def home (request):
    now_tiem  = datetime.datetime.now()

    return render(request,'clientes/home.html')