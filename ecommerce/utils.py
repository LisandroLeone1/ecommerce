def cuotas_sin_interes (precio, cuotas):
    if cuotas <= 0:
        raise ValueError("El numero de cuotas debe ser mayor a 0")
    
    cuota = int(precio / cuotas)
    return cuota


def cuotas_con_interes(precio, tasa_interes_anual, cuotas):
    if cuotas <= 0:
        raise ValueError("El número de cuotas debe ser mayor a 0")
    
    r = tasa_interes_anual / 100 / 12  # Convertir tasa anual a mensual
    n = cuotas
    pago_mensual = (r * precio) / (1 - (1 + r) ** -n)
    
    return pago_mensual



def get_breadcrumb_name(url):
    breadcrumbs = []

    # Siempre empieza con "Inicio"
    breadcrumbs.append('Inicio')

    if url == '/':
        return ' > '.join(breadcrumbs)  # Solo "Inicio"
    
    elif url == '/indumentaria/':
        breadcrumbs.append('Indumentaria')
    elif url.startswith('/indumentaria/'):
        genero = url.split('/')[-2].capitalize()  # Obtener el género de la URL
        breadcrumbs.append('Indumentaria')
        breadcrumbs.append(genero)
        
    elif url == '/calzados/':
        breadcrumbs.append('Calzados')
    elif url.startswith('/calzados/'):
        genero = url.split('/')[-2].capitalize()
        breadcrumbs.append('Calzados')
        breadcrumbs.append(genero)
        
    elif url == '/accesorios/':
        breadcrumbs.append('Accesorios')
    elif url.startswith('/accesorios/'):
        genero = url.split('/')[-2].capitalize()
        breadcrumbs.append('Accesorios')
        breadcrumbs.append(genero)
        
    elif url.startswith('/producto/'):
        breadcrumbs.append('Detalle del Producto')

    elif url == '/sale/':
        breadcrumbs.append('Sale')

    return ' > '.join(breadcrumbs)  # Devuelve la cadena de breadcrumbs


