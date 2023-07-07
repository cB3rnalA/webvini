from django import forms
from .models import CliPedido, Cliente, Pedido, Vinilo,Administrador
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

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
    
    #validar
    rut = forms.CharField(label='RUT',min_length=12, max_length=12, validators=[RegexValidator(r'^([1-9]{1}|([1-9]{1}[0-9]{1}))\.(\d{3}\.\d{3}-)([a-zA-Z]{1}$|\d{1}$)',message="Rut con punto y guion")],required=False, help_text=("FORMATO: XX.XXX.XXX-X"),widget=forms.TextInput(attrs={'placeholder':'RUT'}))
    nombre = forms.CharField(label='Nombre', min_length=3, max_length=40,validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="Solo letras en el nombre")],required=False,help_text=("FORMATO: 3 a 40 LETRAS"),widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    apellido = forms.CharField(label='Apellido', min_length=3, max_length=40,validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="Solo letras en el apellido")],required=False,help_text=("FORMATO: 3 a 40 LETRAS"),widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    correo = forms.CharField(label='Correo', min_length=5, max_length=200, validators= [RegexValidator(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',message="Solo letras en el nombre")],help_text=("FORMATO: XXXX@XXXX.XX"),required=False,widget=forms.TextInput(attrs={'placeholder': 'Correo'}))
        
    class Meta:
        model=Cliente
        fields=["rut","nombre","apellido","correo","contra","direccion","region","comuna","telefono"]
        

class formCrearCli(UserCreationForm):
    
    username = forms.CharField(label='Nombre de usuario', min_length=5, max_length=200, validators= [RegexValidator(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',message="Ingrese correo valido")],help_text=("FORMATO: XXXX@XXXX.XX"),required=False,widget=forms.TextInput(attrs={'placeholder': 'Correo'}))
    
    class Meta:
        model =User
        fields=["username","first_name","last_name","password1",'password2']
        
class formCliPedido(forms.ModelForm):
    
    class Meta:
        model=CliPedido
        fields=["id","cliente","pedido"]
        
