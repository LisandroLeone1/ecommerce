from django.db import models
from django.contrib.auth.models import User
from ecommerce.models import Producto

class Carro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carro')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Carro de {self.user.username} - Producto {self.producto.nombre}"
