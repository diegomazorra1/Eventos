from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django import forms


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.forms_user import RegistroForm
# Create your views here.



class PagPrincipal(TemplateView):

	template_name="base/base.html"






class RegistroUsuario(CreateView):
	model = User
	template_name = "login/register.html"
	form_class = RegistroForm

	def get_success_url(self):
		return reverse_lazy('login') + '?register'

	def get_form(self,form_class=None):
		form = super(RegistroUsuario, self).get_form()
		# Modifico en tiempo real para no perder las caracteristicas por defecto de user de django
		form.fields['first_name'].widget= forms.TextInput(attrs={'class': ' form-control form-control-user ', 'placeholder':' Nombre'  })
		form.fields['last_name'].widget= forms.TextInput(attrs={'class': ' form-control form-control-user ','placeholder':'Apellido' })
		form.fields['username'].widget= forms.TextInput(attrs={'class': ' form-control form-control-user   ','placeholder':'Nombre de Usuario' })
		form.fields['email'].widget= forms.EmailInput(attrs={'class': ' form-control form-control-user   ','placeholder':'Email' })
		form.fields['password1'].widget= forms.PasswordInput(attrs={'class': ' form-control form-control-user   ','placeholder':'Contraseña' })
		form.fields['password2'].widget= forms.PasswordInput(attrs={'class': ' form-control form-control-user   ','placeholder':'Repite la Contraseña' })
		return form
