




"""
def productos_lista(request):
    genero = request.GET.get('genero', None)
    color = request.GET.get('color', None)
    talle = request.GET.getlist('talle')  #  mples marcas
    if genero and genero in dict(Producto.GENERO_CHOICES).keys():
        producto = Producto.objects.filter(genero=genero)
    elif color and color in dict(Producto.COLOR_CHOICES).keys():
        producto = Producto.objects.filter(color=color)
    elif talle and talle in dict(Producto.TALLE_CHOICES).keys():
        producto = Producto.objects.filter(talle=talle)
    else:
        producto = Producto.objects.all()
    
    return render(request, 'ecommerce/index.html', {'producto': producto}) """


from django.shortcuts import render, get_object_or_404
from .models import Producto, Marca, Color, TalleCalzado, TalleIndumentaria, Categoria
from .utils import cuotas_sin_interes
from django.db.models import Q

def Home(request):
    return render(request,"ecommerce/index.html")


def obtener_filtros(request):
    return {
        'genero': request.GET.get('genero', None),
        'color_ids': request.GET.getlist('colores'),
        'talle_ids': request.GET.getlist('talles'),
        'marca_ids': request.GET.getlist('marca'),
        'categoria_id': request.GET.get('categoria', None),
        'tipo_producto': request.GET.get('tipo_producto', None),
        'estado': request.GET.get('estado', None),
    }



def filtrar_productos(queryset, genero, color_ids, talle_ids, marca_ids, categoria_id, tipo_producto):
    if genero and genero in dict(Producto.GENERO_CHOICES).keys():
        queryset = queryset.filter(genero=genero)

    if color_ids:
        queryset = queryset.filter(colores__id__in=color_ids)

    if talle_ids:
        # Aquí filtramos por talles dependiendo del tipo de producto
        if tipo_producto == 'indumentaria':
            queryset = queryset.filter(talles_indumentaria__id__in=talle_ids)
        elif tipo_producto == 'calzado':
            queryset = queryset.filter(talles_calzado__id__in=talle_ids)

    if marca_ids:
        queryset = queryset.filter(marca__id__in=marca_ids)

    if categoria_id:
        queryset = queryset.filter(categoria_id=categoria_id)

        # Con el metodo distinct evito que se dupliquen los resultados cuando aplica mas de un filtro
    queryset = queryset.distinct()

    return queryset


def construir_filtros_aplicados(genero, color_ids, talle_ids, marca_ids, categoria_id, tipo_producto):
    filtros_aplicados = {}

    if genero:
        filtros_aplicados['genero'] = genero

    if color_ids:
        colores = Color.objects.filter(id__in=color_ids)
        filtros_aplicados['Colores'] = ', '.join([color.nombre for color in colores])

    if talle_ids:
        if tipo_producto == 'indumentaria':
            talles = TalleIndumentaria.objects.filter(id__in=talle_ids)  # Filtrar talles de indumentaria
            filtros_aplicados['Talles'] = ', '.join([talle.nombre for talle in talles])
        elif tipo_producto == 'calzado':
            talles = TalleCalzado.objects.filter(id__in=talle_ids)  # Filtrar talles de calzado
            filtros_aplicados['Talles'] = ', '.join([talle.nombre for talle in talles])

    if marca_ids:
        marcas = Marca.objects.filter(id__in=marca_ids)
        filtros_aplicados['Marcas'] = ', '.join([marca.nombre for marca in marcas])

    if categoria_id:
        categoria = get_object_or_404(Categoria, id=categoria_id)
        filtros_aplicados['Categoría'] = categoria.nombre

    return filtros_aplicados


def index_list(request):
    filtros = obtener_filtros(request)
    # Filtrar productos
    productos = Producto.objects.all()

    # Manejar búsqueda
    busqueda = request.GET.get('busqueda', '')
    if busqueda:
        productos = productos.filter(
            Q(nombre__icontains=busqueda) | 
            Q(marca__nombre__icontains=busqueda) | 
            Q(genero__icontains=busqueda) |         
            Q(categoria__nombre__icontains=busqueda)  
        )

    novedades = Producto.objects.filter(estado='novedades')

    for novedad in novedades:
        novedad.cuota = cuotas_sin_interes(novedad.precio, 3)

    destacados = Producto.objects.filter(estado='destacados')

    for destacado in destacados:
        destacado.cuota = cuotas_sin_interes(destacado.precio, 3)

    sales = Producto.objects.filter(estado='sale')

    for sale in sales:
        precio_descuento = sale.precio_con_descuento()  
        sale.cuota = cuotas_sin_interes(precio_descuento, 3) 


    return render(request, 'ecommerce/index.html', {
        'productos': productos,
        'busqueda': busqueda,
        'novedades': novedades,
        'destacados': destacados,
        'sales': sales,
    })




def indumentaria_view(request, genero=None):
    filtros = obtener_filtros(request)

    # Filtrar productos de indumentaria
    indumentarias = Producto.objects.filter(tipo_producto='indumentaria')
    if genero:
        indumentarias = indumentarias.filter(genero=genero)

    # Aplicar filtro de género si se proporciona


    indumentarias = filtrar_productos(
        indumentarias,
        genero,  # Usa el género de la URL o el del formulario
        filtros['color_ids'],
        filtros['talle_ids'],
        filtros['marca_ids'],
        filtros['categoria_id'],
        'indumentaria'
    )

    # Ordenar productos
    ordenar = request.GET.get('ordenar')
    if ordenar == 'precio_asc':
        indumentarias = indumentarias.order_by('precio')
    elif ordenar == 'precio_desc':
        indumentarias = indumentarias.order_by('-precio')
    elif ordenar == 'nombre_asc':
        indumentarias = indumentarias.order_by('nombre')
    elif ordenar == 'nombre_desc':
        indumentarias = indumentarias.order_by('-nombre')
    
    for indumentaria in indumentarias:
        if indumentaria.estado == 'sale':
            precio_a_usar = indumentaria.precio_con_descuento()
        else:
            precio_a_usar = indumentaria.precio    
        indumentaria.cuota = cuotas_sin_interes(precio_a_usar, 3)

    filtros_aplicados = construir_filtros_aplicados(
        genero, 
        filtros['color_ids'],
        filtros['talle_ids'],
        filtros['marca_ids'],
        filtros['categoria_id'],
        'indumentaria'
    )

    # Obtener listas de marcas y colores para el formulario
    marcas = Marca.objects.all()
    colores = Color.objects.all()
    talles_ind = TalleIndumentaria.objects.all()

    return render(request, 'ecommerce/indumentaria.html', {
        'indumentarias': indumentarias,
        'filtros_aplicados': filtros_aplicados,
        'marcas': marcas,
        'colores': colores,
        'talles_ind': talles_ind,
        'genero': genero,
    })



def calzados_view(request, genero=None):
    filtros = obtener_filtros(request)
    
    # Filtrar productos de calzado
    calzados = Producto.objects.filter(tipo_producto='calzado') 
    if genero:
        calzados = calzados.filter(genero=genero)
    
    
    # Filtrar por tipo de producto
    calzados = filtrar_productos(calzados, genero, filtros['color_ids'], filtros['talle_ids'], filtros['marca_ids'], filtros['categoria_id'],'calzado')

    ordenar = request.GET.get('ordenar')
    if ordenar == 'precio_asc':
        calzados = calzados.order_by('precio')
    elif ordenar == 'precio_desc':
        calzados = calzados.order_by('-precio')
    elif ordenar == 'nombre_asc':
        calzados = calzados.order_by('nombre')
    elif ordenar == 'nombre_desc':
        calzados = calzados.order_by('-nombre')

    # Calcular cuotas para cada calzado
    for calzado in calzados:
        if calzado.estado == 'sale':
            precio_a_usar = calzado.precio_con_descuento()
        else:
            precio_a_usar = calzado.precio    
        calzado.cuota = cuotas_sin_interes(precio_a_usar, 3)


    filtros_aplicados = construir_filtros_aplicados(
        genero, 
        filtros['color_ids'], 
        filtros['talle_ids'], 
        filtros['marca_ids'], 
        filtros['categoria_id'], 
        'calzado'  # Pasar tipo de producto
    )

    # Obtener listas de marcas y colores para el formulario
    marcas = Marca.objects.all()
    colores = Color.objects.all()
    talles_cal = TalleCalzado.objects.all()

    return render(request, 'ecommerce/calzados.html', {
        'calzados': calzados,
        'filtros_aplicados': filtros_aplicados,
        'marcas': marcas,
        'colores': colores,
        'talles_cal': talles_cal,
        'genero': genero,
    })


def sale_view(request):
    filtros = obtener_filtros(request)
    
    # Filtrar productos de calzado
    sales = Producto.objects.filter(estado='sale') 
    

    # Filtrar por tipo de producto
    sales = filtrar_productos(sales, None, filtros['color_ids'], filtros['talle_ids'], filtros['marca_ids'], filtros['categoria_id'],'sale')

    ordenar = request.GET.get('ordenar')
    if ordenar == 'precio_asc':
        sales = sales.order_by('precio')
    elif ordenar == 'precio_desc':
        sales = sales.order_by('-precio')
    elif ordenar == 'nombre_asc':
        sales = sales.order_by('nombre')
    elif ordenar == 'nombre_desc':
        sales = sales.order_by('-nombre')

    # Calcular cuotas para los producto en sale
    for sale in sales:
        precio_descuento = sale.precio_con_descuento()  
        sale.cuota = cuotas_sin_interes(precio_descuento, 3) 

    filtros_aplicados = construir_filtros_aplicados(
        None, 
        filtros['color_ids'], 
        filtros['talle_ids'], 
        filtros['marca_ids'], 
        filtros['categoria_id'], 
        None,  # Pasar tipo de producto
    )

    # Obtener listas de marcas y colores para el formulario
    marcas = Marca.objects.all()
    colores = Color.objects.all()
    talles_cal = TalleCalzado.objects.all()

    return render(request, 'ecommerce/sale.html', {
        'sales': sales,
        'filtros_aplicados': filtros_aplicados,
        'marcas': marcas,
        'colores': colores,
        'talles_cal': talles_cal,
    })


def producto_detalle(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    colores = producto.colores.all()
    
    # Obtener talles dependiendo del tipo de producto
    if producto.tipo_producto == 'indumentaria':
        talles = producto.talles_indumentaria.all()
    elif producto.tipo_producto == 'calzado':
        talles = producto.talles_calzado.all()
    else:
        talles = []  # En caso de que no sea ni indumentaria ni calzado, se puede ajustar según necesidad
    
    cuota = cuotas_sin_interes(producto.precio, 3)

    return render(request, 'ecommerce/producto.html', {'producto': producto, 'talles': talles, 'colores': colores, 'cuota': cuota})


"""
def productos_lista(request):
    filtros = obtener_filtros(request)

    # Filtrar productos
    productos = Producto.objects.all()

    # Manejar búsqueda
    busqueda = request.GET.get('busqueda', '')
    if busqueda:
        productos = productos.filter(
            Q(nombre__icontains=busqueda) | 
            Q(marca__nombre__icontains=busqueda) | 
            Q(genero__icontains=busqueda) |         
            Q(categoria__nombre__icontains=busqueda)  
        )

    
    # Filtrar por otros filtros
    productos = filtrar_productos(
        productos,
        filtros['genero'],
        filtros['color_ids'],
        filtros['talle_ids'],
        filtros['marca_ids'],
        filtros['categoria_id'],
        None
    )
    print(f"Talle IDs en productos_lista: {filtros['talle_ids']}")

    #Ordenar productos
    ordenar = request.GET.get('ordenar')
    if ordenar == 'precio_asc':
        productos = productos.order_by('precio')
    elif ordenar == 'precio_desc':
        productos = productos.order_by('-precio')
    elif ordenar == 'nombre_asc':
        productos = productos.order_by('nombre')
    elif ordenar == 'nombre_desc':
        productos = productos.order_by('-nombre')

    # Calcular cuotas
    for producto in productos:
        producto.cuota = cuotas_sin_interes(producto.precio, 3)

    filtros_aplicados = construir_filtros_aplicados(
        filtros['genero'],
        filtros['color_ids'],
        filtros['talle_ids'],
        filtros['marca_ids'],
        filtros['categoria_id'],
        filtros['tipo_producto']
    )

    checked_marcas = request.GET.getlist('marca_ids')

    # Obtener listas de marcas y colores para el formulario
    marcas = Marca.objects.all()
    colores = Color.objects.all()
    talles_ind = TalleIndumentaria.objects.all()
    talles_cal = TalleCalzado.objects.all()

    # Combinar talles y asegurarse de que no haya duplicados
    talles_all = list(set(list(talles_ind) + list(talles_cal)))

    return render(request, 'ecommerce/index.html', {
        'productos': productos,
        'filtros_aplicados': filtros_aplicados,
        'marcas': marcas,
        'colores': colores,
        'talles_all': talles_all,
        'busqueda': busqueda,  
        'checked_marcas': checked_marcas,
    })
"""

"""
def indumentaria_view(request):
    genero = request.GET.get('genero', None)
    color_ids = request.GET.getlist('colores')
    talle_ids = request.GET.getlist('talles')
    marca_ids = request.GET.getlist('marca')
    categoria_id = request.GET.get('categoria', None)

    # Filtrar productos de indumentaria
    indumentarias = Producto.objects.filter(categoria='1')


    if genero and genero in dict(Producto.GENERO_CHOICES).keys():
        indumentarias = indumentarias.filter(genero=genero)

    if color_ids:
        indumentarias = indumentarias.filter(colores__id__in=color_ids)

    if talle_ids:
        indumentarias = indumentarias.filter(talles__id__in=talle_ids)

    if marca_ids:
        indumentarias = indumentarias.filter(marca__id__in=marca_ids)

    if categoria_id:
        indumentarias = indumentarias.filter(categoria_id=categoria_id)

    filtros_aplicados = {}

    if genero:
        filtros_aplicados['Género'] = genero

    if color_ids:
        colores = Color.objects.filter(id__in=color_ids)
        filtros_aplicados['Colores'] = ', '.join([color.nombre for color in colores])

    if talle_ids:
        talles = Talle.objects.filter(id__in=talle_ids)
        filtros_aplicados['Talles'] = ', '.join([talle.nombre for talle in talles])

    if marca_ids:
        marcas = Marca.objects.filter(id__in=marca_ids)
        filtros_aplicados['Marcas'] = ', '.join([marca.nombre for marca in marcas])

    if categoria_id:
        categoria = Categoria.objects.get(id=categoria_id)
        filtros_aplicados['Categoría'] = categoria.nombre

    # Obtener listas de marcas y colores para el formulario
    marcas = Marca.objects.all()
    colores = Color.objects.all()

    return render(request, 'ecommerce/indumentaria.html', {
        'indumentarias': indumentarias,
        'filtros_aplicados': filtros_aplicados,
        'marcas': marcas,
        'colores': colores,
    })
"""


"""
def producto_detalle(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    talles = producto.talles.all()  # Suponiendo que tienes una relación ManyToMany
    colores = producto.colores.all()
    cuota = cuotas_sin_interes(producto.precio, 3)
    return render(request, 'ecommerce/producto.html', {'producto': producto, 'talles': talles, 'colores': colores, 'cuota': cuota})
"""