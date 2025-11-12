from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistroUsuarioForm


# Vista para manejar el proceso de registro de nuevos usuarios
def registro_usuario(request):
    if request.method == 'POST':
        # Instanciar el formulario con los datos enviados por POST
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo usuario en la base de datos
            user = form.save()
            # Iniciar sesión automáticamente con el usuario recién creado
            login(request, user)
            messages.success(request, f"Registro exitoso para {user.first_name}. ¡Bienvenido al sistema!")
            # Redirigir a la página principal después del registro
            # Asegúrate de que 'inventario:menu_principal' esté definida en tu urls.py
            return redirect('inventario:menu_principal')
        else:
            # Si el formulario no es válido, mostrar un mensaje de error general
            messages.error(request, "Error en el formulario. Por favor, revise y corrija los errores marcados.")
    else:
        # Petición GET: mostrar el formulario de registro vacío
        form = RegistroUsuarioForm()

    # Renderizar la plantilla de registro
    return render(request, 'usuario/registro.html', {'form': form, 'titulo': 'Registro de Nuevo Usuario'})