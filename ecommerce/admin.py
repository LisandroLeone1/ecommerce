from django.contrib import admin
from .models import Categoria, Marca, Producto, Color, TalleIndumentaria, TalleCalzado

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Color)
admin.site.register(TalleCalzado)
admin.site.register(TalleIndumentaria)

