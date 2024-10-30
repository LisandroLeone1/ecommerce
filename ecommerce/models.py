from django.db import models

class TalleIndumentaria(models.Model):
    nombre = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre

class TalleCalzado(models.Model):
    nombre = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

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
        ('niño', 'Niño'), 
        ('niña', 'Niña'),
    ]
    
    TIPO_PRODUCTO_CHOICES = [
        ('indumentaria', 'Indumentaria'),
        ('calzado', 'Calzado'),
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
    colores = models.ManyToManyField(Color)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, null=True)
    imagen_principal = models.ImageField(upload_to='fotos/')
    imagen_secundaria_1 = models.ImageField(upload_to='fotos/', blank=True, null=True)
    imagen_secundaria_2 = models.ImageField(upload_to='fotos/', blank=True, null=True)
    imagen_secundaria_3 = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def precio_con_descuento(self):
        if self.estado == 'sale':
            precio_descuento = int(self.precio * (1 - self.descuento / 100))
        else:
            self.precio
        return precio_descuento

    def __str__(self):
        return self.nombre
