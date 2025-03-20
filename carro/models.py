from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from ecommerce.models import Producto

class Carro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carro')
    productos = models.ManyToManyField(Producto, through='CarroItem')

    def __str__(self):
        return f"Carro de {self.user.username}"

    @property
    def total_carro(self):
        """Calcula el total del carrito sumando los totales de cada CarroItem"""
        total = sum(Decimal(item.producto.precio) * Decimal(item.cantidad) for item in self.carroitem_set.all())
        return total
    

class CarroItem(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en el carrito de {self.carro.user.username}"
    
    def total_producto(self):
        return self.producto.precio * self.cantidad 
