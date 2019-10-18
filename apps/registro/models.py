from django.db import models
from django.contrib.auth.models import User
import datetime
import time
from django.utils import timezone





# Create your models here.



class Registros(models.Model):

    titulo= models.CharField(max_length=50)
    image = models.ImageField(upload_to='profiles', null=True, blank=True)
    descripcion= models.CharField(max_length=82)
    Tipos=(('Publico','Publico'),('Privado','Privado'))
    tipo=models.CharField(choices=Tipos,default="Publico",max_length=7)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    interested_in = models.ManyToManyField(User,related_name="users_interested", blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    not_interested_in = models.ManyToManyField(User,related_name="users_not_interested", blank=True)
    signed_up = models.ManyToManyField(User,related_name="users_assistants", blank=True)
    def __str__(self):
        return '{} '.format(self.id)



class Comment(models.Model):
    post = models.ForeignKey(Registros, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="eventsc")
    approved_comment = models.BooleanField(default=True)
