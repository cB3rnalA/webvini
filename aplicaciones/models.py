from django.db import models

# Create your models here.

REGION = [
        ("RM", "Santiago"),
        ("Bio-Bio", "Bio-Bio"),
        ("Araucania", "Araucania"),
    ]
CARGO = [
        ("Encargado ventas", "Encargado ventas"),
        ("Administrador de usuarios", "Administrador de usuarios"),
        ("Administrador de cuentas", "Administrador de cuentas"),
        ("Encargado pagina web", "Encargado pagina web"),
    ]
ESTADO =[
        ("Sin enviar","Sin enviar"),
        ("En transito","En transito"),
        ("Completado","Completado"),
]
class Cliente(models.Model):
    rut=models.CharField(primary_key=True, null=False, max_length=12)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    correo=models.CharField(max_length=100)
    contra=models.CharField(max_length=12)
    direccion=models.CharField(max_length=45)
    region=models.CharField(max_length=50,choices=REGION)
    comuna=models.CharField(max_length=40)
    telefono=models.IntegerField()
    
class Administrador(models.Model):
    rut=models.CharField(primary_key=True, null=False, max_length=12)
    nombre=models.CharField(max_length=40)
    correo=models.CharField(max_length=100)
    contra=models.CharField(max_length=12)
    telefono=models.IntegerField()
    cargo=models.CharField(max_length=100,choices=CARGO)
    
class Vinilo(models.Model):
    id=models.AutoField(primary_key=True)
    cara_delante = models.ImageField(upload_to="productos")
    cara_detras = models.ImageField(upload_to="productos")
    nombre_cantante=models.CharField(max_length=40)
    nombre_vinilo=models.CharField(max_length=40)
    estilo=models.CharField(max_length=40) #Esto se podia dejar como un choise tambien
    precio=models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre_vinilo} de {self.nombre_cantante}"

class Carrito(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=10)
    producto=models.CharField(max_length=20)
    cantidad=models.IntegerField()
    total=models.IntegerField()

class Pedido(models.Model):
    id=models.AutoField(primary_key=True)
    producto=models.CharField(max_length=2000)
    total=models.IntegerField()
    estado=models.CharField(max_length=100,choices=ESTADO)
    
    def __str__(self):
        return f"{self.id}"
    
class CliPedido(models.Model):
    id=models.AutoField(primary_key=True)
    cliente=models.CharField(max_length=2000)
    pedido=models.IntegerField()
    
    def __str__(self):
        return f"{self.id}"