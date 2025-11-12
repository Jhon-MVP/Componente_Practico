from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado
from .utils import validar_cedula_ecuatoriana


class RegistroUsuarioForm(UserCreationForm):
    """
    Formulario de creación de usuario que hereda de UserCreationForm
    y añade la validación algorítmica y de unicidad de la cédula.
    """
    # Campos adicionales requeridos y con etiquetas en español
    cedula = forms.CharField(max_length=10, required=True, label="Cédula Ecuatoriana")
    first_name = forms.CharField(max_length=150, required=True, label="Nombres")
    last_name = forms.CharField(max_length=150, required=True, label="Apellidos")
    email = forms.EmailField(required=True, label="Correo Electrónico")

    # Campos con requerimiento en el formulario
    telefono = forms.CharField(max_length=15, required=True, label="Teléfono")
    fecha_nacimiento = forms.DateField(
        required=True,
        label="Fecha de Nacimiento",
        # Widget para mostrar un selector de fecha HTML5
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    direccion = forms.CharField(
        required=True,
        label="Dirección de Residencia",
        # Widget de área de texto con 3 filas
        widget=forms.Textarea(attrs={'rows': 3})
    )

    class Meta:
        model = UsuarioPersonalizado
        # Incluye los campos de UserCreationForm (username, password, password2)
        fields = ('username', 'cedula', 'first_name', 'last_name', 'email', 'telefono', 'fecha_nacimiento', 'direccion')

    # Método de limpieza específico para el campo 'cedula'
    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula', '').strip()

        # 1. Validación de unicidad
        queryset = UsuarioPersonalizado.objects.filter(cedula=cedula)
        # Excluir al propio usuario si se estuviera editando (contexto de creación, pero buena práctica)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            queryset = queryset.exclude(pk=instance.pk)

        if queryset.exists():
            raise forms.ValidationError("Ya existe un usuario registrado con esta Cédula.")

        # 2. Validación algorítmica usando la función de utils.py
        if not validar_cedula_ecuatoriana(cedula):
            raise forms.ValidationError("La Cédula Ecuatoriana ingresada no es válida según el algoritmo.")

        return cedula

    # Método de limpieza específico para el campo 'email'
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Validación de unicidad
        queryset = UsuarioPersonalizado.objects.filter(email=email)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            queryset = queryset.exclude(pk=instance.pk)

        if queryset.exists():
            raise forms.ValidationError("Ya existe un usuario registrado con este Correo Electrónico.")
        return email