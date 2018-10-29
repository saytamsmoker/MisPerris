from django import forms
from apps.contacto.models import Contacto

class ContactoForm(forms.ModelForm):

	class Meta:
		model = Contacto

		fields = [
			'rut',
			'com_name',
			'email',
			'phone',
			'reg',
			'city',

		]

		labels = {
			'rut': 'Rut',
			'com_name': 'Nombre de mascota',
			'email': 'Email', 
			'phone': 'Telefono',
			'reg': 'Region',
			'city': 'Ciudad',
		}

		widgets = {
			'rut': forms.TextInput(attrs={'class':'form-control'}),
			'com_name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'phone': forms.TextInput(attrs={'class':'form-control'}),
			'reg': forms.TextInput(attrs={'class':'form-control'}),
			'city': forms.TextInput(attrs={'class':'form-control'}),
		}