from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm, PerfilUsuarioForm
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import logout, login
from django.urls import reverse
from .models import PerfilUsuario



class CustomLoginViews(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "login/login.html"

    def get(self, request):
        # Definir las breadcrumbs directamente
        breadcrumbs = [
            {'name': 'Inicio', 'url': reverse('ecommerce:index')},
            {'name': 'Mi Cuenta', 'url': reverse('login:login')},
            {'name': 'Login', 'url': None}
        ]
        
        # Obtener el formulario de autenticación
        form = self.get_form()

        # Pasar tanto las breadcrumbs como el formulario al contexto
        context = {
            'breadcrumbs': breadcrumbs,
            'form': form,
        }

        # Renderizar la plantilla con el contexto
        return self.render_to_response(context)


def register(request: HttpRequest):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        perfil_form = PerfilUsuarioForm(request.POST)
        if form.is_valid() and perfil_form.is_valid():
            # Guardar el usuario
            user = form.save()
            
            # Crear el perfil del usuario
            perfil = perfil_form.save(commit=False)
            perfil.user = user  # Asociar el perfil al usuario recién creado
            perfil.save()
            
            # Iniciar sesión al usuario y redirigir a la página principal o a donde necesites
            login(request, user)

            return render(request, "ecommerce/index.html", {"mensaje": f"Usuario '{user.username}' creado correctamente"})
    else:
        form = CustomUserCreationForm()  # Inicializar formulario de creación de usuario
        perfil_form = PerfilUsuarioForm()  # Inicializar formulario de perfil

    breadcrumbs = [
        {'name': 'Inicio', 'url': reverse('ecommerce:index')},
        {'name': 'Mi Cuenta', 'url': reverse('login:login')},
        {'name': 'Crear Cuenta', 'url': None}
    ]
    
    return render(request, "login/register.html", {
        "form": form,
        'perfil_form': perfil_form,
        'breadcrumbs': breadcrumbs
    })


def tucuenta(request):
    # Acceder al usuario autenticado
    user = request.user

    # Obtener el perfil del usuario si existe
    try:
        perfil = PerfilUsuario.objects.get(user=user)
    except PerfilUsuario.DoesNotExist:
        perfil = None

    breadcrumbs = [
        {'name': 'Inicio', 'url': reverse('ecommerce:index')},
        {'name': 'Mi Cuenta', 'url': reverse('login:login')},
        {'name': 'Tus Datos', 'url': None}
    ]

    # Pasar los datos del usuario y perfil al template
    return render(request, "login/account.html", {
        'user': user,
        'perfil': perfil,
        'breadcrumbs': breadcrumbs
    })


def cerrar_sesion(request):
    logout(request)
    
    return redirect("ecommerce:index")
