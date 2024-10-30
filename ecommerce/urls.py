from django.urls import path
from ecommerce.views import Home, index_list, indumentaria_view, calzados_view, producto_detalle

app_name = "ecommerce"
urlpatterns = [
    path('',index_list,name="index"),
    path('indumentaria/',indumentaria_view,name="lista_indumentaria"),
    path('indumentaria/<str:genero>/', indumentaria_view, name='indumentaria_por_genero'),
    path('calzados/',calzados_view,name="lista_calzados"),
    path('calzados/<str:genero>/', calzados_view, name='calzado_por_genero'),
    path('producto/<int:producto_id>/',producto_detalle,name="producto_detalle"),
]

