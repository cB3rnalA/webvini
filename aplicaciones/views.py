from django.shortcuts import render,get_object_or_404,redirect
from datetime import date
from aplicaciones.carrito import Carrito
from .models import Administrador, CliPedido, Cliente, Pedido,Vinilo
from .forms import formCliPedido, formCreaC, formCrearVinilo,formCrearAdmin,formpedido,formCrearCliente,formCrearCli
from django.db.models import Q
from django.contrib.auth.decorators import login_required #obliga a que este logeado el cliente para realizar el cambio de vista
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def index(request):
    admin=Administrador.objects.all()
    
    print("a")
    contexto={
        "admins":admin,
    }
    
    return render(request,'aplicaciones/admin/index.html',contexto)

def otrawea(request):
    Vinilos=Vinilo.objects.all()

    contexto={
        "v":Vinilos,
    }

    return render(request,'aplicaciones/otrawea.html',contexto)

def agregar_Vinilo(request, Vinilo_id):
    carrito=Carrito(request)
    vinilo=Vinilo.objects.get(id=Vinilo_id)
    carrito.agregar(vinilo)
    messages.success(request, " ")
    
    return redirect(to="iniciocliente")
    
def comprarahora(request, Vinilo_id):
    carrito=Carrito(request)
    vinilo=Vinilo.objects.get(id=Vinilo_id)
    carrito.agregar(vinilo)
    total_carrito = 0
    carrito = request.session.get("carrito", {})
    
    for key, value in carrito.items():
        total_carrito += value["acumulado"]
    
    contexto = {
        'total': total_carrito,
        
    }
    
    return render(request,'aplicaciones/carrito.html',contexto)
    
def eliminar_Vinilo(request, vinilo_id):
    carrito=Carrito(request)
    vinilo=Vinilo.objects.get(id=vinilo_id)
    carrito.elminar(vinilo)
    total_carrito = 0
    carrito = request.session.get("carrito", {})
    
    for key, value in carrito.items():
        total_carrito += value["acumulado"]
    
    contexto = {
        'total': total_carrito,
        
    }
    return render(request,'aplicaciones/carrito.html',contexto)
    
def restar_Vinilo(request, Vinilo_id):
    carrito=Carrito(request)
    vinilo=Vinilo.objects.get(id=Vinilo_id)
    carrito.restar(vinilo)
    total_carrito = 0
    carrito = request.session.get("carrito", {})
    
    for key, value in carrito.items():
        total_carrito += value["acumulado"]
    
    contexto = {
        'total': total_carrito,
        
    }
    return render(request,'aplicaciones/carrito.html',contexto)
    
def limpiar_Carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    total_carrito = 0
    carrito = request.session.get("carrito", {})
    
    for key, value in carrito.items():
        total_carrito += value["acumulado"]
    total_carrito = 0
    carrito = request.session.get("carrito", {})
    
    for key, value in carrito.items():
        total_carrito += value["acumulado"]
    
    contexto = {
        'total': total_carrito,
        
    }
    contexto = {
        'total': total_carrito,
        
    }
    return render(request,'aplicaciones/carrito.html',contexto)

def carrito(request):
    total_carrito = 0
    carrito = request.session.get("carrito", {})
    
    for key, value in carrito.items():
        total_carrito += value["acumulado"]
    
    contexto = {
        'total': total_carrito,
        
    }
    return render(request,'aplicaciones/carrito.html',contexto)
def vinilos(request):
    vini=Vinilo.objects.all()
    
    contexto={
        "vini":vini,
    }
    
    return render(request,'aplicaciones/admin/vinilos.html',contexto)

def añadir(request):
    form=formCrearVinilo(request.POST,request.FILES or None)
    
    contexto={
        "form":form,
    }
    
    if request.method=="POST":

        if form.is_valid():
            form.save()
            return redirect(to="vinilos")
    
    return render(request,'aplicaciones/admin/añadirvinilo.html',contexto)

def modificarvinilo(request,id):
    Producto=get_object_or_404(Vinilo,id=id)
    
    contexto={
        'form':formCrearVinilo(instance=Producto)
    }
    
    if request.method=="POST":
        formulario=formCrearVinilo(data=request.POST,files=request.FILES ,instance=Producto)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="vinilos")
        contexto["form"]= formulario
        
    return render(request,'aplicaciones/admin/modificarvinilo.html',contexto)

def modificarestado(request,id):
    esta=get_object_or_404(Pedido,id=id)
    
    contexto={
        'form':formpedido(instance=esta)
    }
    
    if request.method=="POST":
        formulario=formpedido(data=request.POST,instance=esta)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="pedidos")
        
        
    return render(request,'aplicaciones/admin/modificarestado.html',contexto)

def eliminarvinilo(request,id):
    producto=get_object_or_404(Vinilo,id=id)

    contexto={

        "vin":producto
    }

    if request.method=="POST":
        producto.delete()
        return redirect(to="vinilos")


    return render(request,"aplicaciones/admin/eliminarvinilo.html",contexto)

def añadiradmin(request):
    form=formCrearAdmin(request.POST or None)
    
    contexto={
        "form":form,
    }
    
    if request.method=="POST":

        if form.is_valid():
            form.save()
            return redirect(to="index")
    
    return render(request,'aplicaciones/admin/añadiradmin.html',contexto)

def pedidos(request):
    pedido=Pedido.objects.all()
    clipedido=CliPedido.objects.all()
    cliente=Cliente.objects.all()
    
    contexto={
        "ped":pedido,
        "cped":clipedido,
        "cli":cliente,
    }
    
    return render(request,'aplicaciones/admin/pedidos.html',contexto)


def viniloscli(request):
    v=Vinilo.objects.all()

    contexto={
        "v":v,
    }

    return render(request,'aplicaciones/viniloscli.html', contexto)

def iniciocliente(request):
    v=Vinilo.objects.all()

    contexto={
        "v":v,
    }

    return render(request,'aplicaciones/iniciocliente.html',contexto)

def detalle(request, id):
    v=get_object_or_404(Vinilo,id=id)
    
    contexto={
        "v":v,
    }
    return render(request, 'aplicaciones/detalle.html', contexto)

def listar_vinilos(request):
    busqueda = request.GET.get("buscar")
    v=Vinilo.objects.all()
    
    if busqueda:
        v = Vinilo.objects.filter(
            Q(nombre_cantante__icontains = busqueda) |
            Q(nombre_vinilo__icontains = busqueda) |
            Q(estilo__icontains = busqueda)
            
        ).distinct()
    return render(request, 'aplicaciones/iniciocliente.html',{'v':v})

def listar_vinilos_vini(request):
    busqueda = request.GET.get("buscar")
    v=Vinilo.objects.all()
    
    if busqueda:
        v = Vinilo.objects.filter(
            Q(nombre_cantante__icontains = busqueda) |
            Q(nombre_vinilo__icontains = busqueda) |
            Q(estilo__icontains = busqueda)
            
        ).distinct()
    return render(request,'aplicaciones/viniloscli.html',{'v':v})

def cliente(request):
    cli=Cliente.objects.all()
    
    contexto={
        "cli":cli,
    }
    return render(request,'aplicaciones/admin/cliente.html',contexto)

def iniciosesion(request):
    
    return render(request,'aplicaciones/inicio_sessio.html')

def crearcuenta(request):
    
    form=formCrearCliente(request.POST or None)

    contexto={
        "form":form,
        
    }

    if form.is_valid():
        crearcli=form.save(commit=False)
        crearcli.save()
        return redirect(to="iniciosesion")
    
    return render(request,'aplicaciones/CrearCuenta.html',contexto)


def buscarapi(request):
    return render(request,'aplicaciones/buscarapi.html')

@login_required #obliga al cliente a estar registrado para comprar / se evitan pedidos y compras sin clientes registrados
def precompra(request):
    cli=Cliente.objects.all()
    
    total_carrito = 0
    carrito = request.session.get("carrito", {})
    
    for key, value in carrito.items():
        total_carrito += value["acumulado"]
    
    contexto = {
        'total_carrito': total_carrito,
        "cli":cli
    }
    return render(request,'aplicaciones/precompra.html',contexto)



def pago(request):
    total_carrito = 0
    carrito = request.session.get("carrito", {})
    
    form = formpedido()
    formcom = Pedido.objects.all()
    Fped = formCliPedido()
    cli = Cliente.objects.all()
    user = request.user.username


    product = []
    for key, value in carrito.items():
        total_carrito += value["acumulado"]
        product.append(value["nombre"])
    
    product_str = "; ".join(product)
    
    pedido = Pedido()  # Crear una instancia del modelo Pedido
    pedido.estado = "Sin enviar"
    pedido.producto = product_str
    pedido.total = total_carrito
    
    Fped.pedido = pedido.id
    Fped.cliente = user
    Fped.id = pedido.id 
    
    
    
    
    contexto = {
        'total_carro': total_carrito,
        'pedido': form,
        'ped':formcom,
        'pediCli': Fped,
        'cli': cli,
        'owo':Fped.id,
    }
    

    return render(request, 'aplicaciones/pago.html', contexto)

def registro(request):
    cliUs = formCrearCli()
    cli = formCreaC()
    contexto = {
        'form':cliUs,
        'formcli2':cli,
        
    }
    if request.method == 'POST':
        formulario = formCrearCli(request.POST)
        formulario2 = formCreaC(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario2.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to="iniciocliente")
        contexto["form"]=formulario
    return render(request, 'registration/registro.html', contexto)

""" def registroadmins(request):
    cliUs = formCrearCli()
    cli = formCreaC()
    contexto = {
        'form':cliUs,
        'formcli2':cli,
    }
    if request.method == 'POST':
        formulario = formCrearCli(request.POST)
        formulario2 = formCreaC(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario2.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to="iniciocliente")
        contexto["form"]=formulario
    return render(request, 'registration/registro.html', contexto) """

@login_required
def perfil(request):
    cli=Cliente.objects.all()
    Cped=CliPedido.objects.all()
    ped=Pedido.objects.all()
    
    contexto={
        "cli":cli,
        "Cped":Cped,
        "ped":ped,
    }
    return render(request,'aplicaciones/perfil.html',contexto)

def pagoExito(request):
    total_carrito = 0
    cant_prod = 0
    
    carrito = request.session.get("carrito", {})
    
    form = formpedido()
    formcom = Pedido.objects.all()
    Fped = formCliPedido()
    cli = Cliente.objects.all()
    user = request.user.username
    PCmodel= CliPedido()


    product = []
    for key, value in carrito.items():
        total_carrito += value["acumulado"]
        cant_prod = value["cantidad"]
        pro = value["nombre"] + ": cantidad: " + str(cant_prod)
        product.append(pro)
    
    product_str = "; ".join(product)
    
    pedido = Pedido()  # Crear una instancia del modelo Pedido
    pedido.estado = "Sin enviar"
    pedido.producto = product_str
    pedido.total = total_carrito
    pedido.save()  # Guardar la instancia en la base de datos
    
    Fped.pedido = pedido.id
    Fped.cliente = user
    Fped.id = pedido.id + 107
    
    PCmodel.pedido = Fped.pedido
    PCmodel.cliente = Fped.cliente
    PCmodel.id = Fped.id
    PCmodel.save()
    
    
    #Limpiar carro al hacer el pago
    carrito=Carrito(request)
    carrito.limpiar()
    total_carrito = 0
    carrito = request.session.get("carrito", {})
    
    for key, value in carrito.items():
        total_carrito += value["acumulado"]
    
    contexto = {
        'total_carro': total_carrito,
        'pedido': form,
        'ped':formcom,
        'pediCli': Fped,
        'cli': cli,
        'owo':Fped.id,
        'total': total_carrito,

    }
    
    
    
    return render(request,"aplicaciones/pagoExito.html",contexto)
# def vin_pop(request, estilo):
#     v=get_object_or_404(Vinilo,id=estilo)
    
#     contexto={
#         "v":v,
#     }
#     return render(request, 'aplicaciones/vin_pop.html', contexto)

""" def listar_vinilos_admin(request):
    busqueda = request.GET.get("buscar")
    v=Vinilo.objects.all()
    
    if busqueda:
        v = Vinilo.objects.filter(
            Q(nombre_cantante__icontains = busqueda) |
            Q(nombre_vinilo__icontains = busqueda) |
            Q(estilo__icontains = busqueda)
            
        ).distinct()
    return render(request,'aplicaciones/admin/vinilos.html',{'v':v}) """