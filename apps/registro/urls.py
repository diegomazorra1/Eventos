from django.urls import path, include
from .views import EventListView, EventUpdate, asisir_events, interesados_list, Event_Delete

app_name= "Hola2"
urlpatterns = [


    path('lista', EventListView.as_view(),name='lista'),
    path('editar/<int:pk>/', EventUpdate.as_view(),name='editar'),
    path('eliminar/<int:pk>/', Event_Delete.as_view(),name='eliminar'),
    path('asisir_events/<int:id_page>/', asisir_events ,name='asiste'),
    path('intereses/', interesados_list ,name='intereses'),





]
