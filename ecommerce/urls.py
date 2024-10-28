from django.urls import path
from ecommerce.views import Home, productos_lista, indumentaria_view, calzados_view, producto_detalle

app_name = "ecommerce"
urlpatterns = [
    path('',productos_lista,name="lista"),
    path('indumentaria/',indumentaria_view,name="lista_indumentaria"),
    path('calzados/',calzados_view,name="lista_calzados"),
    path('producto/<int:producto_id>/',producto_detalle,name="producto_detalle"),
]

