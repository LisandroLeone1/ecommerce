from django.urls import path, include
from ecommerce.views import Home, index_list, indumentaria_view, calzados_view, producto_detalle, sale_view, accesorios_view


app_name = "ecommerce"
urlpatterns = [
    path('',index_list,name="index"),
    path('indumentaria/',indumentaria_view,name="lista_indumentaria"),
    path('indumentaria/<str:genero>/', indumentaria_view, name='indumentaria_por_genero'),
    path('calzados/',calzados_view,name="lista_calzados"),
    path('calzados/<str:genero>/', calzados_view, name='calzado_por_genero'),
    path('accesorios/',accesorios_view,name="lista_accesorios"),
    path('accesorios/<str:genero>/', accesorios_view, name='accesorios_por_genero'),
    path('producto/<int:producto_id>/',producto_detalle,name="producto_detalle"),
    path('sale/', sale_view, name="lista_sale"),
    path('sale/<str:genero>/', sale_view, name='sale_por_genero'),
]

