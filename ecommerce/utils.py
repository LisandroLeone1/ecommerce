def cuotas_sin_interes (precio, cuotas):
    if cuotas <= 0:
        raise ValueError("El numero de cuotas debe ser mayor a 0")
    
    cuota = precio / cuotas
    return round(cuota, 2)


def cuotas_con_interes(precio, tasa_interes_anual, cuotas):
    if cuotas <= 0:
        raise ValueError("El número de cuotas debe ser mayor a 0")
    
    r = tasa_interes_anual / 100 / 12  # Convertir tasa anual a mensual
    n = cuotas
    pago_mensual = (r * precio) / (1 - (1 + r) ** -n)
    
    return round(pago_mensual, 2)  # Redondear a dos decimales
