
from django.shortcuts import render, get_object_or_404
from .models import Producto, Marca, Color, TalleCalzado, TalleIndumentaria, Categoria
from .utils import cuotas_sin_interes
from django.db.models import Q
from django.urls import reverse

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



def filtrar_productos(queryset, color_ids, talle_ids, marca_ids, genero, tipo_producto):

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

    if genero:
        if genero == 'hombre':
            queryset = queryset.filter(genero__in = ['hombre', 'unisex'])
        elif genero == 'mujer':
            queryset = queryset.filter(genero__in = ['mujer', 'unisex'])
        else:
            queryset = queryset.filter(genero=genero)

    if tipo_producto:
        queryset = queryset.filter(tipo_producto=tipo_producto)
        # Con el metodo distinct evito que se dupliquen los resultados cuando aplica mas de un filtro
    queryset = queryset.distinct()

    return queryset.order_by('-created')


def construir_filtros_aplicados(color_ids, talle_ids, marca_ids, tipo_producto):
    filtros_aplicados = {}

    # Filtrar por colores
    if color_ids:
        colores = Color.objects.filter(id__in=color_ids)
        filtros_aplicados['Colores'] = [color.nombre for color in colores]

    # Filtrar por talles dependiendo del tipo de producto
    if talle_ids:
        if tipo_producto == 'indumentaria':
            talles = TalleIndumentaria.objects.filter(id__in=talle_ids)  # Filtrar talles de indumentaria
            filtros_aplicados['Talles'] = [talle.nombre for talle in talles]
        elif tipo_producto == 'calzado':
            talles = TalleCalzado.objects.filter(id__in=talle_ids)  # Filtrar talles de calzado
            filtros_aplicados['Talles'] = [talle.nombre for talle in talles]

    # Filtrar por marcas
    if marca_ids:
        marcas = Marca.objects.filter(id__in=marca_ids)
        filtros_aplicados['Marcas'] = [marca.nombre for marca in marcas]


    return filtros_aplicados


# Funcion para ordenar productos
def ordenar_productos(ordenar, productos):
    if ordenar == 'precio_asc':
        productos = productos.order_by('precio')
    elif ordenar == 'precio_desc':
        productos = productos.order_by('-precio')
    elif ordenar == 'nombre_asc':
        productos = productos.order_by('nombre')
    elif ordenar == 'nombre_desc':
        productos = productos.order_by('-nombre')
    return productos

# Funcion darle a cada producto el precio con descuento y calcular las cuotas
def calcular_cuotas(productos):
    for producto in productos:
        precio_descuento = producto.precio_con_descuento()  
        producto.cuota = cuotas_sin_interes(precio_descuento, 3)


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

    novedades = Producto.objects.order_by('-created')[:8] # los ultimos 8 productos cargados en la BD son las novedades
    destacados = Producto.objects.filter(estado='destacados').order_by('-created')[:8] # ultimos 8 productos cargados con estado "destacados"
    sales = Producto.objects.filter(estado='sale').order_by('-created')

    calcular_cuotas(novedades)
    calcular_cuotas(destacados)
    calcular_cuotas(sales)

    marcas = Marca.objects.all()

    return render(request, 'ecommerce/index.html', {
        'productos': productos,
        'busqueda': busqueda,
        'novedades': novedades,
        'destacados': destacados,
        'sales': sales,
        'marcas': marcas,
    })




def indumentaria_view(request, genero=None):
    filtros = obtener_filtros(request)

    # Filtrar productos de indumentaria
    indumentarias = Producto.objects.filter(tipo_producto='indumentaria').order_by('-created')

    indumentarias = filtrar_productos(
        indumentarias,   
        filtros['color_ids'],
        filtros['talle_ids'],
        filtros['marca_ids'],
        genero,
        'indumentaria'
    )
    ordenar = request.GET.get('ordenar')
    indumentarias = ordenar_productos(ordenar, indumentarias)
    
    calcular_cuotas(indumentarias)

    filtros_aplicados = construir_filtros_aplicados(
        filtros['color_ids'],
        filtros['talle_ids'],
        filtros['marca_ids'],
        'indumentaria'
    )

    # Obtener listas de marcas y colores para el formulario
    marcas_disponibles = indumentarias.values_list('marca', flat= True).distinct()
    marcas_disponibles = Marca.objects.filter(id__in=marcas_disponibles)
    marcas_con_cantidad = []
    for marca in marcas_disponibles:
        cantidad = indumentarias.filter(marca=marca).count()
        marcas_con_cantidad.append({'marca': marca, 'cantidad': cantidad})

    colores_disponibles = indumentarias.values_list('colores', flat= True).distinct()
    colores_disponibles = Color.objects.filter(id__in=colores_disponibles)
    colores_con_cantidad = []
    for color in colores_disponibles:
        cantidad = indumentarias.filter(colores=color).count()
        colores_con_cantidad.append({'color': color, 'cantidad': cantidad})

    talles_ind_disponibles = indumentarias.values_list('talles_indumentaria', flat=True).distinct()
    talles_ind_disponibles = TalleIndumentaria.objects.filter(id__in=talles_ind_disponibles)
    talles_con_cantidad = []
    for talle in talles_ind_disponibles:
        cantidad = indumentarias.filter(talles_indumentaria=talle).count()
        talles_con_cantidad.append({'talle': talle, 'cantidad': cantidad})


    #Migas de pan
    breadcrumbs = [
        {'name': 'Inicio', 'url': reverse('ecommerce:index')},
        {'name': 'Indumentaria', 'url': reverse('ecommerce:lista_indumentaria')}
    ]
    if genero:
        breadcrumbs.append({'name': genero.capitalize(), 'url': None })

    return render(request, 'ecommerce/indumentaria.html', {
        'indumentarias': indumentarias,
        'filtros_aplicados': filtros_aplicados,
        'marcas_con_cantidad': marcas_con_cantidad,
        'colores_con_cantidad': colores_con_cantidad,
        'talles_con_cantidad': talles_con_cantidad,
        'genero': genero,
        'breadcrumbs': breadcrumbs,
    })



def calzados_view(request, genero=None):
    filtros = obtener_filtros(request)
    
    # Filtrar productos de calzado
    calzados = Producto.objects.filter(tipo_producto='calzado').order_by('-created')

    # Filtrar por tipo de producto
    calzados = filtrar_productos(calzados, filtros['color_ids'], filtros['talle_ids'], filtros['marca_ids'], genero, 'calzado')

    ordenar = request.GET.get('ordenar')
    calzados = ordenar_productos(ordenar, calzados)

    calcular_cuotas(calzados)

    filtros_aplicados = construir_filtros_aplicados(
        filtros['color_ids'], 
        filtros['talle_ids'], 
        filtros['marca_ids'], 
        'calzado'  # paso el tipo de producto
    )

    # Obtener listas de marcas y colores para el formulario
    marcas_disponibles = calzados.values_list('marca', flat= True).distinct()
    marcas_disponibles = Marca.objects.filter(id__in=marcas_disponibles)
    marcas_con_cantidad = []
    for marca in marcas_disponibles:
        cantidad = calzados.filter(marca=marca).count()
        marcas_con_cantidad.append({'marca': marca, 'cantidad': cantidad})

    colores_disponibles = calzados.values_list('colores', flat= True).distinct()
    colores_disponibles = Color.objects.filter(id__in=colores_disponibles)
    colores_con_cantidad = []
    for color in colores_disponibles:
        cantidad = calzados.filter(colores=color).count()
        colores_con_cantidad.append({'color': color, 'cantidad': cantidad})

    talles_cal_disponibles = calzados.values_list('talles_calzado', flat=True).distinct()
    talles_cal_disponibles = TalleCalzado.objects.filter(id__in=talles_cal_disponibles)
    talles_con_cantidad = []
    for talle in talles_cal_disponibles:
        cantidad = calzados.filter(talles_calzado=talle).count()
        talles_con_cantidad.append({'talle': talle, 'cantidad': cantidad})


    breadcrumbs = [
        {'name': 'Inicio', 'url': reverse('ecommerce:index')},
        {'name': 'Calzados', 'url': reverse('ecommerce:lista_calzados')}
    ]

    if genero:
        breadcrumbs.append({'name': genero.capitalize(), 'url': None})

    return render(request, 'ecommerce/calzados.html', {
        'calzados': calzados,
        'filtros_aplicados': filtros_aplicados,
        'marcas_con_cantidad':  marcas_con_cantidad,
        'colores_con_cantidad': colores_con_cantidad,
        'talles_con_cantidad': talles_con_cantidad,
        'genero': genero,
        'breadcrumbs': breadcrumbs,
    })



def accesorios_view(request, genero=None):
    filtros = obtener_filtros(request)
    
    accesorios = Producto.objects.filter(tipo_producto='accesorios').order_by('-created')
    
    accesorios = filtrar_productos(accesorios, filtros['color_ids'], filtros['talle_ids'], filtros['marca_ids'], genero, 'accesorios')

    ordenar = request.GET.get('ordenar')
    accesorios = ordenar_productos(ordenar, accesorios)

    calcular_cuotas(accesorios)

    filtros_aplicados = construir_filtros_aplicados(
        filtros['color_ids'], 
        filtros['talle_ids'], 
        filtros['marca_ids'], 
        'accesorios'  
    )

    marcas_disponibles = accesorios.values_list('marca', flat= True).distinct()
    marcas_disponibles = Marca.objects.filter(id__in=marcas_disponibles)
    marcas_con_cantidad = []
    for marca in marcas_disponibles:
        cantidad = accesorios.filter(marca=marca).count()
        marcas_con_cantidad.append({'marca': marca, 'cantidad': cantidad})

    colores_disponibles = accesorios.values_list('colores', flat= True).distinct()
    colores_disponibles = Color.objects.filter(id__in=colores_disponibles)
    colores_con_cantidad = []
    for color in colores_disponibles:
        cantidad = accesorios.filter(colores=color).count()
        colores_con_cantidad.append({'color': color, 'cantidad': cantidad})


    talles_cal_disponibles = accesorios.values_list('talles_calzado', flat=True).distinct()
    talles_cal_disponibles = TalleCalzado.objects.filter(id__in=talles_cal_disponibles)
    talles_con_cantidad = []
    for talle in talles_cal_disponibles:
        cantidad = accesorios.filter(talles_calzado=talle).count()
        talles_con_cantidad.append({'talle': talle, 'cantidad': cantidad})

    breadcrumbs = [
        {'name': 'Inicio', 'url': reverse('ecommerce:index')},
        {'name': 'Accesorios', 'url': reverse('ecommerce:lista_accesorios')}
    ]

    if genero:
        breadcrumbs.append({'name': genero.capitalize(), 'url': None})

    return render(request, 'ecommerce/accesorios.html', {
        'accesorios': accesorios,
        'filtros_aplicados': filtros_aplicados,
        'marcas_con_cantidad': marcas_con_cantidad,
        'colores_con_cantidad':  colores_con_cantidad,
        'genero': genero,
        'breadcrumbs': breadcrumbs,
    })


def sale_view(request, genero=None, tipo_producto = None):
    filtros = obtener_filtros(request)
    # Filtro los productos en estado sale
    sales = Producto.objects.filter(estado='sale').order_by('-created')

    sales = filtrar_productos(sales, filtros['color_ids'], filtros['talle_ids'], filtros['marca_ids'], genero, tipo_producto)

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
    calcular_cuotas(sales)

    filtros_aplicados = construir_filtros_aplicados(
        filtros['color_ids'], 
        filtros['talle_ids'], 
        filtros['marca_ids'], 
        None,  
    )

    marcas_disponibles = sales.values_list('marca', flat= True).distinct()
    marcas_disponibles = Marca.objects.filter(id__in=marcas_disponibles)
    marcas_con_cantidad = []
    for marca in marcas_disponibles:
        cantidad = sales.filter(marca=marca).count()
        marcas_con_cantidad.append({'marca': marca, 'cantidad': cantidad})

    colores_disponibles = sales.values_list('colores', flat= True).distinct()
    colores_disponibles = Color.objects.filter(id__in=colores_disponibles)
    colores_con_cantidad = []   
    for color in colores_disponibles:
        cantidad = sales.filter(colores=color).count()
        colores_con_cantidad.append({'color': color, 'cantidad': cantidad})

    talles_cal_disponibles = sales.values_list('talles_calzado', flat=True).distinct()
    talles_cal_disponibles = TalleCalzado.objects.filter(id__in=talles_cal_disponibles)
    talles_ind_disponibles = sales.values_list('talles_indumentaria', flat=True).distinct()
    talles_ind_disponibles = TalleIndumentaria.objects.filter(id__in=talles_ind_disponibles)

    # Unificamos ambos conjuntos de talles
    todos_los_talles = list(talles_ind_disponibles) + list(talles_cal_disponibles)

    breadcrumbs = [
        {'name': 'Inicio', 'url': reverse('ecommerce:index')},
        {'name': 'Sale', 'url': reverse('ecommerce:lista_sale')}
    ]
    if genero:
        breadcrumbs.append({'name': genero.capitalize(), 'url': None})

    return render(request, 'ecommerce/sale.html', {
        'sales': sales,
        'filtros_aplicados': filtros_aplicados,
        'marcas_con_cantidad': marcas_con_cantidad,
        'colores_con_cantidad': colores_con_cantidad,
        'todos_los_talles': todos_los_talles,
        'talles_ind_disponibles': talles_ind_disponibles,
        'talles_cal_disponibles': talles_cal_disponibles,
        'breadcrumbs': breadcrumbs,
        'genero' : genero,
    })


def producto_detalle(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    colores = producto.colores.all()
    
    # Obtener talles dependiendo del tipo de producto
    if producto.tipo_producto == 'indumentaria':
        talles = producto.talles_indumentaria.all()
    elif producto.tipo_producto == 'calzado':
        talles = producto.talles_calzado.all()
    elif producto.tipo_producto == 'accesorios':
        talles = producto.talles_accesorios.all()
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


"""def construir_filtros_aplicados(color_ids, talle_ids, marca_ids, categoria_id, tipo_producto):
    filtros_aplicados = {}

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

    return filtros_aplicados"""