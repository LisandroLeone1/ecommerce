from django.shortcuts import render, redirect
from .models import Carro
from ecommerce.models import Producto
from django.contrib.auth.decorators import login_required

# Agregar producto al carrito
@login_required
def agregar_a_carro(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carro, created = Carro.objects.get_or_create(user=request.user, producto=producto)

    if not created:
        carro.cantidad += 1
        carro.save()

    return redirect('carro:carro')

# Ver carrito de compras
@login_required
def ver_carro(request):
    carro = Carro.objects.filter(user=request.user)
    total = sum(item.producto.precio * item.cantidad for item in carro)
    return render(request, 'carro/carro.html', {'carro': carro, 'total': total})

# Eliminar producto del carrito
@login_required
def eliminar_del_carro(request, producto_id):
    try:
        carro = Carro.objects.get(user=request.user, producto__id=producto_id)
        carro.delete()
    except Carro.DoesNotExist:
        pass
    return redirect('carro:carro')

# Actualizar cantidad de producto
@login_required
def actualizar_carro(request, producto_id):
    nuevo_cantidad = request.POST.get('cantidad')
    carro = Carro.objects.get(user=request.user, producto__id=producto_id)
    if nuevo_cantidad.isdigit() and int(nuevo_cantidad) > 0:
        carro.cantidad = int(nuevo_cantidad)
        carro.save()
    return redirect('carro:carro')










"""
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from ecommerce.models import Producto

from .carro import Carro 


def carro(request):
    carro = Carro(request)
    return render(request, 'carro/carro.html', {'carro': carro.carro})


def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.agregar(producto=producto)
    
    # Redirigir de vuelta al producto con un mensaje
    return render(request, 'tu_template_producto.html', {
        'producto': producto,
        'mensaje': 'Producto agregado al carrito!'
    })


def eliminar_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminar(producto=producto)
    return render(request,"carro/carro.html",{'carro': carro, 'producto':producto})

def restar_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.restar_producto(producto=producto)
    return render(request,"carro/carro.html",{'carro': carro, 'producto':producto})
    

def limpiar_carro(request,producto_id):
    carro = Carro(request)
    carro.limpar_carro()
    return redirect("tienda")"""