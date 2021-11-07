from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, DateTimeField, IntegerField


sexo_choice =(
    ('M','MASCULINO'),
    ('F','FEMININO')

)
# Create your models here.
class Cliente(models.Model):
    nome = CharField(max_length=15)
    sobre_nome = CharField(max_length=20)
    dt_nasc = DateField(null=False)
    cpf = IntegerField(max_length=11,primary_key=True)
    email = CharField(max_length=50)
    sexo = CharField(max_length=1,choices=sexo_choice)
    dt_cadastro = DateTimeField(auto_now_add=True)
    dt_alteracao = DateTimeField()
    sn_ativo = BooleanField(null=False, default=True)



