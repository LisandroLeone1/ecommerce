from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Carro, CarroItem
from ecommerce.models import Producto
from django.contrib.auth.decorators import login_required

@login_required
def agregar_a_carro(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))
    color = request.POST.get('color', '')
    talle = request.POST.get('talle', '')

    if producto.stock >=cantidad:
        carro, _ = Carro.objects.get_or_create(user=request.user)
        carro_item, created = CarroItem.objects.get_or_create(carro=carro, producto=producto, talle=talle, color=color)
        if not created:
            carro_item.cantidad += cantidad
        else:
            carro_item.cantidad = cantidad
        
        carro_item.save()

        producto.restar_stock(cantidad)

        return redirect('carro:carro')
    
    else:
        return HttpResponse("No hay suficiente stock para esta cantidad.", status=400)

@login_required
def ver_carro(request):
    carro, _ = Carro.objects.get_or_create(user=request.user)  # Asegura que haya un carrito
    items = CarroItem.objects.filter(carro=carro)
    total = sum((item.precio_unitario_con_descuento()) for item in items) 
    #en la funcion precio_con_descuento de la clase Producto ya manejo un condicional que si el producto no esta en sale
    # entonces devolvera el precio original. Osea con "total" calculo el precio total de todos los productos del carro
    # tanto si tienen descuento como si no tienen
    cantidad_total_productos = sum(item.cantidad for item in items)
    

    return render(request, 
                'carro/carro.html', 
                {'carro': items,
                'total': total, 
                'cantidad_total_productos': cantidad_total_productos
                })

# Eliminar producto del carrito
@login_required
def eliminar_del_carro(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carro = get_object_or_404(Carro, user=request.user)
    color = request.GET.get('color', '')
    talle = request.GET.get('talle', '')
    try:
        item = CarroItem.objects.get(carro=carro, producto__id=producto_id, color=color, talle=talle)
        producto.sumar_stock(item.cantidad)
        item.delete()
    except CarroItem.DoesNotExist:
        pass  # Si el producto no existe en el carrito, no hacer nada

    return redirect('carro:carro')

# Actualizar cantidad de producto
@login_required
def actualizar_carro(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carro = get_object_or_404(Carro, user=request.user)
    nuevo_cantidad = request.POST.get('cantidad')

    if nuevo_cantidad.isdigit() and int(nuevo_cantidad) > 0:
        item = get_object_or_404(CarroItem, carro=carro, producto__id=producto_id)
        cantidad_anterior = item.cantidad
        cantidad_nueva = int(nuevo_cantidad)

        if producto.stock + cantidad_anterior >= cantidad_nueva:
            item.cantidad = cantidad_nueva
            item.save()

            diferencia_cantidad = cantidad_nueva - cantidad_anterior
            producto.restar_stock(diferencia_cantidad)
        else:
            return HttpResponse("No hay suficiente stock para esta cantidad.", status=400)

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