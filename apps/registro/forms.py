from django import forms
from .models import Registros
#from .models import TipoCuenta



class EventForm(forms.ModelForm):



    class Meta:
        model = Registros

        fields = [

        'titulo',
        'image',
        'descripcion',
        'tipo',


        ]
        labels = {
                'titulo': 'Titulo' ,
                'image': 'Imagen del evento' ,
                'descripcion': 'Descripción' ,
                'tipo': 'Tipo' ,





        }
        widgets= {
                'titulo': forms.TextInput(attrs= {'class': 'form-control'}  )  ,

                'descripcion':   forms.TextInput(attrs= {'class': 'form-control'}  ) ,


        }
