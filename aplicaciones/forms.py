from django import forms
from .models import CliPedido, Cliente, Pedido, Vinilo,Administrador
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class formCrearVinilo(forms.ModelForm):
    
    class Meta:
        model=Vinilo
        fields=["cara_delante","cara_detras", "nombre_cantante", "nombre_vinilo", "estilo","precio"]

class formCrearAdmin(forms.ModelForm):
    
    class Meta:
        model=Administrador
        fields='__all__'

class formpedido(forms.ModelForm):
    
    class Meta:
        model=Pedido
        fields=["estado"]

class formCrearCliente(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields='__all__'
        

class formCreaC(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields=["rut","nombre","apellido","correo","contra","direccion","region","comuna","telefono"]
        

class formCrearCli(UserCreationForm):
    
    class Meta:
        model =User
        fields=["username","first_name","last_name","password1",'password2']
        
class formCliPedido(forms.ModelForm):
    
    class Meta:
        model=CliPedido
        fields=["id","cliente","pedido"]
        
