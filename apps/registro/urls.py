from django.urls import path, include
from .views import EventListView, Event_Create, EventUpdate, asisir_events, rechazar_events, interesados_list, Event_Delete, confirm_events, rechaza_list, confirma_list, interesados_list
from django.contrib.auth.decorators import login_required


app_name= "Hola2"
urlpatterns = [

    path('crear/', login_required(Event_Create.as_view()),name='crear'),
    path('lista', EventListView.as_view(),name='lista'),
    path('editar/<int:pk>/', EventUpdate.as_view(),name='editar'),
    path('eliminar/<int:pk>/', Event_Delete.as_view(),name='eliminar'),
    path('asisir_events/<int:id_page>/', asisir_events ,name='asiste'),
    path('rechazar_events/<int:id_page>/', rechazar_events ,name='rechaza'),
    path('confima_events/<int:id_page>/', confirm_events ,name='confirma'),

    path('intereses/', interesados_list ,name='intereses'),
    path('confirmados/', confirma_list ,name='confirmados'),
    path('rechazados/', rechaza_list ,name='rechazados'),






]
