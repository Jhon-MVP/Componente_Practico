from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    # MENÚ PRINCIPAL
    path('', views.menu_principal, name='menu_principal'),

    # 1. CRUD Marca
    path('marcas/', views.marca_listar, name='marca_listar'),
    path('marcas/crear/', views.marca_crear, name='marca_crear'),
    path('marcas/editar/<int:pk>/', views.marca_editar, name='marca_editar'),
    path('marcas/eliminar/<int:pk>/', views.marca_eliminar, name='marca_eliminar'),

    # 2. CRUD Usuario (Empleado)
    path('usuarios/', views.usuario_listar, name='usuario_listar'),
    path('usuarios/crear/', views.usuario_crear, name='usuario_crear'),
    path('usuarios/editar/<int:pk>/', views.usuario_editar, name='usuario_editar'),
    path('usuarios/eliminar/<int:pk>/', views.usuario_eliminar, name='usuario_eliminar'),

    # 3. CRUD Dispositivo (Núcleo)
    path('dispositivos/', views.dispositivo_listar, name='dispositivo_listar'),
    path('dispositivos/crear/', views.dispositivo_crear, name='dispositivo_crear'),
    path('dispositivos/editar/<int:pk>/', views.dispositivo_editar, name='dispositivo_editar'),
    path('dispositivos/eliminar/<int:pk>/', views.dispositivo_eliminar, name='dispositivo_eliminar'),

    # 4. CRUD Asignación
    path('asignaciones/', views.asignacion_listar, name='asignacion_listar'),
    path('asignaciones/crear/', views.asignacion_crear, name='asignacion_crear'),
    path('asignaciones/editar/<int:pk>/', views.asignacion_editar, name='asignacion_editar'),
    path('asignaciones/eliminar/<int:pk>/', views.asignacion_eliminar, name='asignacion_eliminar'),

    # 5. CRUD Mantenimiento
    path('mantenimientos/', views.mantenimiento_listar, name='mantenimiento_listar'),
    path('mantenimientos/crear/', views.mantenimiento_crear, name='mantenimiento_crear'),
    path('mantenimientos/editar/<int:pk>/', views.mantenimiento_editar, name='mantenimiento_editar'),
    path('mantenimientos/eliminar/<int:pk>/', views.mantenimiento_eliminar, name='mantenimiento_eliminar'),
]