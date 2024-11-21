from django.urls import path
from login.views import CustomLoginViews, register, tucuenta, CuentaUpdate, cerrar_sesion
from django.contrib.auth.views import LogoutView

app_name = "login"

urlpatterns = [
    path("", CustomLoginViews.as_view(), name="login"),
    path("logout/", cerrar_sesion, name="logout"),
    path("register/",register,name="register"),
    path('cuenta/', tucuenta, name='tucuenta'),
    path('cuenta/editar/', CuentaUpdate.as_view(), name='cuenta_update'),
]