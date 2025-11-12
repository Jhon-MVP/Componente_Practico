from django import forms
from .models import Marca, Usuario, Dispositivo, Asignacion, Mantenimiento


# --- 1. CRUD Marca ---
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }


# --- 2. CRUD Usuario (Empleado) ---
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'cedula_empleado': forms.TextInput(attrs={'maxlength': 10}),
        }

    # Aquí podrías añadir una validación de cédula si es necesario


# --- 3. CRUD Dispositivo (Núcleo) ---
class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'
        widgets = {
            'fecha_compra': forms.DateInput(attrs={'type': 'date'}),
        }


# --- 4. CRUD Asignación ---
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = '__all__'
        widgets = {
            'fecha_asignacion': forms.DateInput(attrs={'type': 'date'}),
            'notas': forms.Textarea(attrs={'rows': 3}),
        }


# --- 5. CRUD Mantenimiento ---
class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
            'descripcion_trabajo': forms.Textarea(attrs={'rows': 4}),
        }

    # Validación: El costo debe ser un valor positivo
    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo is not None and costo < 0:
            raise forms.ValidationError("El costo del mantenimiento no puede ser negativo.")
        return costo