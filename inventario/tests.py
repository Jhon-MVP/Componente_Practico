from django.test import TestCase
from .models import Marca, Usuario
from datetime import date


class MarcaTestCase(TestCase):
    def setUp(self):
        Marca.objects.create(nombre="Dell", descripcion="Fabricante de equipos")

    def test_marca_creada(self):
        marca = Marca.objects.get(nombre="Dell")
        self.assertEqual(marca.nombre, "Dell")

    def test_str_marca(self):
        marca = Marca.objects.get(nombre="Dell")
        self.assertEqual(str(marca), "Dell")


class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(
            nombres="Juan",
            apellidos="Perez",
            departamento="Sistemas",
            cedula_empleado="0912345678"
        )

    def test_usuario_creado(self):
        usuario = Usuario.objects.get(cedula_empleado="0912345678")
        self.assertEqual(usuario.nombres, "Juan")

    def test_str_usuario(self):
        usuario = Usuario.objects.get(cedula_empleado="0912345678")
        self.assertIn("Juan", str(usuario))
