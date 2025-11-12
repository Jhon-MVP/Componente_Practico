from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Marca, Usuario, Dispositivo, Asignacion, Mantenimiento
from .forms import MarcaForm, UsuarioForm, DispositivoForm, AsignacionForm, MantenimientoForm


# ====================================================================
# --- FUNCIONES GENÉRICAS REUTILIZABLES (CRUD) ---
# ====================================================================

@login_required
def _crud_crear_editar(request, Model, FormClass, success_url_name, pk=None):
    """Maneja la lógica de crear (pk=None) o editar (pk existe) para cualquier modelo."""

    objeto = None
    titulo = f"Crear {Model._meta.verbose_name}"

    if pk:
        # Modo Edición
        objeto = get_object_or_404(Model, pk=pk)
        titulo = f"Editar {Model._meta.verbose_name}: {objeto}"

    form = FormClass(request.POST or None, instance=objeto)

    if request.method == 'POST' and form.is_valid():
        form.save()
        if pk:
            messages.success(request, f'{Model._meta.verbose_name} actualizado exitosamente.')
        else:
            messages.success(request, f'{Model._meta.verbose_name} creado exitosamente.')
        return redirect(success_url_name)

    context = {
        'form': form,
        'titulo': titulo,
        'objeto': objeto,
        'nombre_modelo': Model._meta.verbose_name_plural,
        'url_listado': reverse(success_url_name),
    }
    return render(request, "inventario/form.html", context)


@login_required
def _crud_eliminar(request, Model, success_url_name, pk):
    """Maneja la lógica de eliminación para cualquier modelo."""

    objeto = get_object_or_404(Model, pk=pk)

    if request.method == 'POST':
        # Intenta eliminar. Si falla por restricción de FK (PROTECT), notifica.
        try:
            objeto.delete()
            messages.warning(request, f'{Model._meta.verbose_name} "{objeto}" ha sido eliminado.')
        except Exception as e:
            # Mensaje de error para el usuario
            messages.error(request,
                           f'No se puede eliminar "{objeto}". Existen registros relacionados (Asignaciones o Mantenimientos) que dependen de este elemento.')
            # Redirige para mostrar el mensaje de error
            return redirect(success_url_name)

        return redirect(success_url_name)

    context = {
        'objeto': objeto,
        'titulo': f"Eliminar {Model._meta.verbose_name}",
        'url_listado': reverse(success_url_name),
    }
    return render(request, "inventario/confirm_delete.html", context)


# ====================================================================
# --- VISTAS ESPECÍFICAS (Llaman a las Genéricas) ---
# ====================================================================

@login_required
def menu_principal(request):
    """Vista del menú principal después del login."""
    return render(request, "inventario/menu_principal.html")


# 1. CRUD Marca
@login_required
def marca_listar(request):
    marcas = Marca.objects.all().order_by('nombre')
    return render(request, "inventario/marca_listar.html", {"objetos": marcas, "titulo": "Listado de Marcas"})


@login_required
def marca_crear(request):
    return _crud_crear_editar(request, Marca, MarcaForm, "inventario:marca_listar")


@login_required
def marca_editar(request, pk):
    return _crud_crear_editar(request, Marca, MarcaForm, "inventario:marca_listar", pk=pk)


@login_required
def marca_eliminar(request, pk):
    return _crud_eliminar(request, Marca, "inventario:marca_listar", pk=pk)


# 2. CRUD Usuario (Empleado)
@login_required
def usuario_listar(request):
    usuarios = Usuario.objects.all().order_by('apellidos')
    return render(request, "inventario/usuario_listar.html",
                  {"objetos": usuarios, "titulo": "Listado de Usuarios (Empleados)"})


@login_required
def usuario_crear(request):
    return _crud_crear_editar(request, Usuario, UsuarioForm, "inventario:usuario_listar")


@login_required
def usuario_editar(request, pk):
    return _crud_crear_editar(request, Usuario, UsuarioForm, "inventario:usuario_listar", pk=pk)


@login_required
def usuario_eliminar(request, pk):
    return _crud_eliminar(request, Usuario, "inventario:usuario_listar", pk=pk)


# 3. CRUD Dispositivo (Núcleo)
@login_required
def dispositivo_listar(request):
    # Usamos select_related para optimizar la consulta de la FK (Marca)
    dispositivos = Dispositivo.objects.select_related('marca').all().order_by('nombre')
    return render(request, "inventario/dispositivo_listar.html",
                  {"objetos": dispositivos, "titulo": "Inventario de Dispositivos"})


@login_required
def dispositivo_crear(request):
    return _crud_crear_editar(request, Dispositivo, DispositivoForm, "inventario:dispositivo_listar")


@login_required
def dispositivo_editar(request, pk):
    return _crud_crear_editar(request, Dispositivo, DispositivoForm, "inventario:dispositivo_listar", pk=pk)


@login_required
def dispositivo_eliminar(request, pk):
    return _crud_eliminar(request, Dispositivo, "inventario:dispositivo_listar", pk=pk)


# 4. CRUD Asignación
@login_required
def asignacion_listar(request):
    # Usamos select_related para optimizar las consultas de las FKs (Dispositivo y Usuario)
    asignaciones = Asignacion.objects.select_related('dispositivo', 'usuario').all().order_by('-fecha_asignacion')
    return render(request, "inventario/asignacion_listar.html",
                  {"objetos": asignaciones, "titulo": "Listado de Asignaciones"})


@login_required
def asignacion_crear(request):
    return _crud_crear_editar(request, Asignacion, AsignacionForm, "inventario:asignacion_listar")


@login_required
def asignacion_editar(request, pk):
    return _crud_crear_editar(request, Asignacion, AsignacionForm, "inventario:asignacion_listar", pk=pk)


@login_required
def asignacion_eliminar(request, pk):
    return _crud_eliminar(request, Asignacion, "inventario:asignacion_listar", pk=pk)


# 5. CRUD Mantenimiento
@login_required
def mantenimiento_listar(request):
    mantenimientos = Mantenimiento.objects.select_related('dispositivo').all().order_by('-fecha_mantenimiento')
    return render(request, "inventario/mantenimiento_listar.html",
                  {"objetos": mantenimientos, "titulo": "Registros de Mantenimiento"})


@login_required
def mantenimiento_crear(request):
    return _crud_crear_editar(request, Mantenimiento, MantenimientoForm, "inventario:mantenimiento_listar")


@login_required
def mantenimiento_editar(request, pk):
    return _crud_crear_editar(request, Mantenimiento, MantenimientoForm, "inventario:mantenimiento_listar", pk=pk)


@login_required
def mantenimiento_eliminar(request, pk):
    return _crud_eliminar(request, Mantenimiento, "inventario:mantenimiento_listar", pk=pk)