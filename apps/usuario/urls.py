from django.urls import path, include
from .views import RegistroUsuario, PagPrincipal
app_name= "Hola"
urlpatterns = [

path('registro/usuario', RegistroUsuario.as_view(),name='usuario_registro'),

path('inicio', PagPrincipal.as_view(),name='inicio'),






]
