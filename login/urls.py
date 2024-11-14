from django.urls import path
from login.views import CustomLoginViews, register, tucuenta
from django.contrib.auth.views import LogoutView

app_name = "login"

urlpatterns = [
    path("", CustomLoginViews.as_view(), name="login"),
    path("logout/",LogoutView.as_view(template_name = "ecommerce/index.html"), name="logout"),
    path("register/",register,name="register"),
    path('mi-cuenta/', tucuenta, name='tucuenta'),
]