#coding: utf8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class RegistroForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)

		self.base_fields['username'].widget.attrs['class'] = 'form-control'
		self.base_fields['numero_telefono'].widget.attrs['class'] = 'form-control'
		self.base_fields['password1'].widget.attrs['class'] = 'form-control'
		self.base_fields['password2'].widget.attrs['class'] = 'form-control'
		self.base_fields['email'].widget.attrs['class'] = 'form-control'
		self.base_fields['first_name'].widget.attrs['class'] = 'form-control'
		self.base_fields['last_name'].widget.attrs['class'] = 'form-control'
		

	class Meta: 
		model = Perfil
		fields =[
			'username',
			'first_name',
			'last_name',
			'numero_telefono',
			'email',
			]		

		labels = {
			'username': 'Numero de cuenta',
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'numero_telefono': 'Numero de telefono',
			'email': 'Correo',
			}	

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if username < 13 :
			raise forms.ValidationError("Por favor ingrese un numero de cuenta valido")	
		return username
	