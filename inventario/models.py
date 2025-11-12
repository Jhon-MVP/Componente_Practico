from django.db import models


# --- MANTENIMIENTO 1: Marca ---
class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre de la Marca")
    descripcion = models.TextField(blank=True, verbose_name="Descripción o Fabricante")

    class Meta:
        verbose_name = "Marca de Dispositivo"
        verbose_name_plural = "Marcas de Dispositivos"

    def __str__(self):
        return self.nombre


# --- MANTENIMIENTO 2: Usuario (Empleado) ---
class Usuario(models.Model):
    nombres = models.CharField(max_length=100, verbose_name="Nombres del Empleado")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos del Empleado")
    departamento = models.CharField(max_length=100, verbose_name="Departamento o Área")
    cedula_empleado = models.CharField(max_length=10, unique=True, verbose_name="Cédula de Empleado")

    class Meta:
        verbose_name = "Usuario de Equipo"
        verbose_name_plural = "Usuarios de Equipos"

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.departamento})"


# --- MANTENIMIENTO 3: Dispositivo (Núcleo) ---
class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Tipo de Dispositivo")  # Ej: Laptop, Monitor
    modelo = models.CharField(max_length=100, verbose_name="Modelo Específico")
    serial = models.CharField(max_length=100, unique=True, verbose_name="Número de Serie/Inventario")
    fecha_compra = models.DateField(verbose_name="Fecha de Compra")

    # Relación 1:N
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, verbose_name="Marca")

    class Meta:
        verbose_name = "Dispositivo Tecnológico"
        verbose_name_plural = "Dispositivos Tecnológicos"

    def __str__(self):
        return f"{self.nombre} {self.modelo} ({self.serial})"


# --- MANTENIMIENTO 4: Asignación (Relación: Dispositivo + Usuario) ---
class Asignacion(models.Model):
    fecha_asignacion = models.DateField(verbose_name="Fecha de Asignación")
    notas = models.TextField(blank=True, verbose_name="Notas de Asignación")

    # Relaciones 1:N
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.PROTECT, verbose_name="Dispositivo Asignado")
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name="Empleado Asignado")

    class Meta:
        verbose_name = "Asignación de Equipo"
        verbose_name_plural = "Asignaciones de Equipos"

    def __str__(self):
        return f"Asignación de {self.dispositivo.nombre} a {self.usuario.apellidos}"


# --- MANTENIMIENTO 5: Mantenimiento (Relación: Dispositivo) ---
class Mantenimiento(models.Model):
    fecha_mantenimiento = models.DateField(verbose_name="Fecha de Mantenimiento")
    # Choices para tipo de mantenimiento
    TIPO_CHOICES = [('P', 'Preventivo'), ('C', 'Correctivo')]
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name="Tipo de Mantenimiento")
    descripcion_trabajo = models.TextField(verbose_name="Trabajo Realizado")
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Costo del Mantenimiento")

    # Relación 1:N
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, verbose_name="Dispositivo Afectado")

    class Meta:
        verbose_name = "Registro de Mantenimiento"
        verbose_name_plural = "Registros de Mantenimientos"

    def __str__(self):
        return f"Mantenimiento {self.get_tipo_display()} - {self.dispositivo.serial} ({self.fecha_mantenimiento})"
