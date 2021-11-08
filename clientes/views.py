from django.shortcuts import redirect, render
import datetime
from clientes.models import Cliente
from .form import ClienteForm,ClienteUpdateForm
# Create your views here.

def home (request):
    now_tiem  = datetime.datetime.now()
    return render(request,'clientes/home.html')

def list (request):
    data = {}
    data['clientes'] = Cliente.objects.all()
    return render(request,'clientes/list.html', data)


def create(request):
    data = {}
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista')
    data['form'] = form
    return render(request,'clientes/form.html',data)


def update(request,pk):
    data = {}
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteUpdateForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('lista')
    data['form'] = form
    data['cliente'] = cliente
    return render(request,'clientes/form.html',data)

def delete (request,pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('lista')