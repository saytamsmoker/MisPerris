from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota

		fields = [
			'nombre',
			'raza',
			'descripcion',
			'estado',
		]
		labels = {
			'nombre': 'Nombre',
			'raza': 'Raza Estimada',
			'descripcion': 'Descripcion',
			'estado': 'Estado',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'raza': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'estado': forms.TextInput(attrs={'class':'form-control'}),
		}