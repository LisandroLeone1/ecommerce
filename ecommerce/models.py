from django.db import models
from django.utils import timezone

class TalleIndumentaria(models.Model):
    nombre = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre

class TalleCalzado(models.Model):
    nombre = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre
    
class TalleAccesorio(models.Model):
    nombre = models.CharField(max_length=11)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos/', null=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=20)
    color_style = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    GENERO_CHOICES = [
        ('hombre', 'Hombre'), 
        ('mujer', 'Mujer'), 
        ('niños', 'Niños'), 
        ('unisex', 'Unisex'),
    ]
    
    TIPO_PRODUCTO_CHOICES = [
        ('indumentaria', 'Indumentaria'),
        ('calzado', 'Calzado'),
        ('accesorios', 'Accesorios')
    ]

    ESTADO_CHOICES = [
        ('novedades', 'Novedades'),
        ('destacados', 'Destacados'),
        ('sale', 'Sale'),
    ]

    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    descuento = models.IntegerField(default=0)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES)
    tipo_producto = models.CharField(max_length=20, choices=TIPO_PRODUCTO_CHOICES, default='indumentaria')
    talles_indumentaria = models.ManyToManyField(TalleIndumentaria, blank=True, null=True)
    talles_calzado = models.ManyToManyField(TalleCalzado, blank=True, null=True)
    talles_accesorios = models.ManyToManyField(TalleAccesorio, default='TALLE UNICO')
    colores = models.ManyToManyField(Color)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES,blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    imagen_principal = models.ImageField(upload_to='fotos/')
    imagen_secundaria_1 = models.ImageField(upload_to='fotos/', blank=True, null=True)
    imagen_secundaria_2 = models.ImageField(upload_to='fotos/', blank=True, null=True)
    imagen_secundaria_3 = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def precio_con_descuento(self):
        if self.estado == 'sale':
            return int(self.precio * (1 - self.descuento / 100))
        return self.precio  # Retorna el precio original si no hay descuento

    def __str__(self):
        return self.nombre
