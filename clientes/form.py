from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','sobre_nome','dt_nasc','cpf','email','sexo'] 


class ClienteUpdateForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','sobre_nome','dt_nasc','cpf','email','sexo','dt_alteracao','sn_ativo']
        