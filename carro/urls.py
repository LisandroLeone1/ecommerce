# carro/urls.py
from django.urls import path
from . import views

app_name = "carro"

urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_a_carro, name='agregar_a_carro'),
    path('ver/', views.ver_carro, name='carro'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carro, name='eliminar_del_carro'),
    path('actualizar/<int:producto_id>/', views.actualizar_carro, name='actualizar_carro'),
]


"""
app_name = "carro"
urlpatterns = [
    path('',views.carro,name="carro"),
    path('agregar/<int:producto_id>/',views.agregar_producto,name="agregar"),
    path('eliminar/<int:producto_id>',views.eliminar_producto,name="eliminar"),
    path('restar/<int:producto_id>',views.restar_producto,name="restar"),
]"""