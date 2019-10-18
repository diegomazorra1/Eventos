from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [

				'first_name',
				'last_name',
				'username',
				'email',
				'password1',
				'password2',
			]
		labels = {

				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'username': 'Nombre de usuario',
				'email': 'Correo',
				'password1': 'Contraseña',
				'password2': 'Repita la contraseña',

		}
