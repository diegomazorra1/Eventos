from django import forms
from apps.usuario.models import Profile



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = [
        'avatar',
        'bio' ,




        ]
        labels = {
        'avatar': 'Avatar',
        'bio' :    'Bio',
        


        }
