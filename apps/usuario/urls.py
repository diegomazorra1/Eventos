from django.urls import path, include
from .views import RegistroUsuario, PagPrincipal, ProfileUpdate
app_name= "Hola"
urlpatterns = [

path('registro/usuario', RegistroUsuario.as_view(),name='usuario_registro'),

path('inicio', PagPrincipal.as_view(),name='inicio'),

path('profile/', ProfileUpdate.as_view(), name="profile" )





]
