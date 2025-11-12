from django.db import models
from django.contrib.auth.models import AbstractUser


# Clase que extiende el modelo de usuario por defecto de Django
class UsuarioPersonalizado(AbstractUser):
    # Campos adicionales requeridos por la consigna
    cedula = models.CharField(max_length=10, unique=True, verbose_name="Cédula Ecuatoriana")
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    # Redefinimos el email para que sea único
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    # Campos que se pedirán obligatoriamente al crear un superusuario
    REQUIRED_FIELDS = ['cedula', 'email', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.cedula})"

    class Meta:
        verbose_name = "Usuario del Sistema"
        verbose_name_plural = "Usuarios del Sistema"
        ordering = ['last_name', 'first_name']