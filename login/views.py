from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm, PerfilUsuarioForm
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import logout, login
from django.urls import reverse, reverse_lazy
from .models import PerfilUsuario
from django.views.generic import UpdateView



class CustomLoginViews(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "login/login.html"

    def get(self, request):
        breadcrumbs = [
            {'name': 'Inicio', 'url': reverse('ecommerce:index')},
            {'name': 'Mi Cuenta', 'url': reverse('login:login')},
            {'name': 'Login', 'url': None}
        ]
        
        # obtener el formulario de autenticación
        form = self.get_form()

        # paso tanto las breadcrumbs como el formulario al contexto
        context = {
            'breadcrumbs': breadcrumbs,
            'form': form,
        }

        # renderizar la plantilla con el contexto
        return self.render_to_response(context)


def register(request: HttpRequest):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        perfil_form = PerfilUsuarioForm(request.POST)
        if form.is_valid() and perfil_form.is_valid():
            # guardar el usuario
            user = form.save()
            
            # crear el perfil del usuario
            perfil = perfil_form.save(commit=False)
            perfil.user = user  # asociar el perfil al usuario recién creado
            perfil.save()
            
            # iniciar sesión al usuario 
            login(request, user)

            return render(request, "ecommerce/index.html", {"mensaje": f"Usuario '{user.username}' creado correctamente"})
    else:
        form = CustomUserCreationForm()  # inicializar formulario de creación de usuario
        perfil_form = PerfilUsuarioForm()  # inicializar formulario de perfil

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
    # acceder al usuario autenticado
    user = request.user

    # obtener el perfil del usuario si existe
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


class CuentaUpdate(UpdateView):
    model = PerfilUsuario
    template_name = "login/account_update.html"
    form_class = PerfilUsuarioForm

    def get_object(self, queryset=None):
        # Obtener el perfil del usuario actual
        return PerfilUsuario.objects.get(user=self.request.user)

    def get_success_url(self):
        # redirige a la página de la cuenta tras la actualización
        return reverse_lazy('login:tucuenta')

    def get_context_data(self, **kwargs):
        # obtiene el contexto de la vista, incluyendo los breadcrumbs
        context = super().get_context_data(**kwargs)
        
        context['breadcrumbs'] = [
            {'name': 'Inicio', 'url': reverse('ecommerce:index')},
            {'name': 'Tus Datos', 'url': reverse('login:tucuenta')},
            {'name': 'Editar Datos', 'url': None}
        ]
        
        return context



def cerrar_sesion(request):
    logout(request)
    return redirect("ecommerce:index")
