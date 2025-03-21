from django.contrib import admin
from .models import Carro, CarroItem

class CarroItemInline(admin.TabularInline):  # También puedes usar admin.StackedInline
    model = CarroItem
    extra = 1  # Número de líneas vacías para agregar nuevos productos en el admin

class CarroAdmin(admin.ModelAdmin):
    list_display = ('user', 'listar_productos', 'total_carro')  # Agregamos el total
    readonly_fields = ('total_carro',)  # Lo mostramos como solo lectura
    inlines = [CarroItemInline]  # Esto mostrará los productos en el mismo panel del Carro

    def listar_productos(self, obj):
        return ", ".join([f"{item.producto.nombre} (x{item.cantidad})" for item in obj.carroitem_set.all()])
    
    listar_productos.short_description = "Productos en el Carro"  # Nombre de la columna

    def total_carro(self, obj):
        # Formateamos el total del carrito como un valor monetario
        return f"${obj.total_carro:,.2f}"

    total_carro.short_description = "Total del Carrito"  # Nombre en el admi

admin.site.register(Carro, CarroAdmin)