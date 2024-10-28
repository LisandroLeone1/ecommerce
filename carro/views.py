from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .carro import Carro        
from ecommerce.models import Producto

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
    return redirect("tienda")