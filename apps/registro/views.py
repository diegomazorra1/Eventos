from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import Registros
from apps.registro.forms import EventForm
from apps.registro.models import Registros
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect




@method_decorator(login_required, name='dispatch')
class Event_Create(LoginRequiredMixin,CreateView):
    model= Registros
    form_class = EventForm
    success_url= reverse_lazy('registro:lista')
    template_name='registro/create_event.html'
    def get_initial(self):
        initial = super().get_initial()
        initial['created_by'] = self.request.user.id
        return initial





class EventListView(ListView):
    model= Registros
    paginate_by =2

class Event_Update(UpdateView):
    model= Registros
    template_name='usuarios/usuarios_form.html'
    success_url= reverse_lazy('usuarios:usuario_listas')




class Event_Delete(DeleteView):
    model= Registros
    template_name='registro/borrar_registro.html'
    success_url= reverse_lazy('registro:lista')





@method_decorator(login_required, name='dispatch')
class EventUpdate(LoginRequiredMixin,UpdateView):
    model= Registros
    template_name= 'registro/edit_event.html'
    form_class= EventForm
    success_url= reverse_lazy('registro:lista')


def asisir_events(request,id_page):



    solicitud="Intereses"
    Evento = Registros.objects.get(id=id_page)
    user1 = User.objects.get(id=request.user.id)

    print("EVENTO",Evento)
    print("USUARIO",user1)
    queryset1 = Registros.objects.filter(
    Q(interested_in__username=request.user.username))
    print("  ESTA INTERESADO EN ESTOS ",queryset1)


    #Q(interested_in__username=request.user.username)&
    #Q(id=id_page))
    #print("  ESTA INTERESADO EN ESTOS ",queryset1)
    #print(Evento)
    #print(user1)
    Evento.interested_in.add(user1)
    Evento.not_interested_in.remove(user1)
    Evento.signed_up.remove(user1)





#    queryset2 = Registros.objects.filter(
#    Q(interested_in__username=id_page) ==
#    request.user.username
#    )


#    print("  si el mismo esta interesado en este evento  ",queryset2)

    return render(request, 'eventos/intereses_list.html', {'queryset1':queryset1, 'solicitud':solicitud } )



def rechazar_events(request,id_page):



    solicitud="Rechazados"
    Evento = Registros.objects.get(id=id_page)
    user1 = User.objects.get(id=request.user.id)

    print("EVENTO",Evento)
    print("USUARIO",user1)
    queryset1 = Registros.objects.filter(
    Q(not_interested_in__username=request.user.username))
    print("  ESTA INTERESADO EN ESTOS ",queryset1)


    #Q(interested_in__username=request.user.username)&
    #Q(id=id_page))
    #print("  ESTA INTERESADO EN ESTOS ",queryset1)
    #print(Evento)
    #print(user1)
    Evento.not_interested_in.add(user1)
    Evento.interested_in.remove(user1)
    Evento.signed_up.remove(user1)






#    queryset2 = Registros.objects.filter(
#    Q(interested_in__username=id_page) ==
#    request.user.username
#    )


#    print("  si el mismo esta interesado en este evento  ",queryset2)

    return render(request, 'eventos/intereses_list.html', {'queryset1':queryset1,'solicitud':solicitud } )



def confirm_events(request,id_page):



    solicitud="Confirmados"
    Evento = Registros.objects.get(id=id_page)
    user1 = User.objects.get(id=request.user.id)

    print("EVENTO",Evento)
    print("USUARIO",user1)
    queryset1 = Registros.objects.filter(
    Q(signed_up__username=request.user.username))
    print("  ESTA INTERESADO EN ESTOS ",queryset1)


    #Q(interested_in__username=request.user.username)&
    #Q(id=id_page))
    #print("  ESTA INTERESADO EN ESTOS ",queryset1)
    #print(Evento)
    #print(user1)
    Evento.signed_up.add(user1)
    Evento.not_interested_in.remove(user1)
    Evento.interested_in.remove(user1)


    return render(request, 'eventos/intereses_list.html', {'queryset1':queryset1,'solicitud':solicitud } )














def interesados_list(request):
    solicitud="Intereses"
    queryset1 = Registros.objects.filter(
    Q(interested_in__username=request.user.username))
    print("  ESTA INTERESADO EN ESTOS ",queryset1)

    #Evento.interested_in.add(user1)


#    queryset2 = Registros.objects.filter(
#    Q(interested_in__username=id_page) ==
#    request.user.username
#    )


#    print("  si el mismo esta interesado en este evento  ",queryset2)

    return render(request, 'eventos/intereses_list.html', {'queryset1':queryset1,'solicitud':solicitud  })


def confirma_list(request):
    solicitud="Confirmados"
    queryset1 = Registros.objects.filter(
    Q(signed_up__username=request.user.username))
    print("  ESTA INTERESADO EN ESTOS ",queryset1)

    #Evento.interested_in.add(user1)


#    queryset2 = Registros.objects.filter(
#    Q(interested_in__username=id_page) ==
#    request.user.username
#    )


#    print("  si el mismo esta interesado en este evento  ",queryset2)

    return render(request, 'eventos/intereses_list.html', {'queryset1':queryset1,'solicitud':solicitud })


def rechaza_list(request):
    solicitud="Rechazados"
    queryset1 = Registros.objects.filter(
    Q(not_interested_in__username=request.user.username))
    print("  ESTA INTERESADO EN ESTOS ",queryset1)

    #Evento.interested_in.add(user1)


#    queryset2 = Registros.objects.filter(
#    Q(interested_in__username=id_page) ==
#    request.user.username
#    )


#    print("  si el mismo esta interesado en este evento  ",queryset2)

    return render(request, 'eventos/intereses_list.html', {'queryset1':queryset1,'solicitud':solicitud })
