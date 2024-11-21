from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilUsuario

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['direccion_de_entrega', 'phone_number', 'birth_date']
        
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),  # para que 'birth_date' sea un campo de tipo fecha
        }

class CustomUserCreationForm(UserCreationForm):
    # Añadir los campos de PerfilUsuario
    direccion_de_entrega = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Dirección de entrega'}))
    phone_number = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Número de teléfono'}))
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))  # se muestra como un selector de fecha

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'direccion_de_entrega', 'phone_number', 'birth_date']