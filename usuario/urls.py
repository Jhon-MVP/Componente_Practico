from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Define el namespace de la app para evitar conflictos de nombres de URL
app_name = 'usuario'

urlpatterns = [
    # 1. Vista de Login
    # Utiliza la vista genérica de Django. Redirige a los usuarios ya autenticados.
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='usuario/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),

    # 2. Vista de Logout
    # Cierra la sesión y redirige a la página de login
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='/usuario/login/'),
        name='logout'
    ),

    # 3. Vista de Registro
    # Usa la vista personalizada que maneja el formulario y las validaciones de cédula
    path(
        'registro/',
        views.registro_usuario,
        name='registro'
    ),
]