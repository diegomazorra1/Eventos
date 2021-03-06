# Generated by Django 2.2.5 on 2019-10-17 21:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_registros_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registros',
            name='interested_in',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_interested', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registros',
            name='not_interested_in',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_not_interested', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registros',
            name='signed_up',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_assistants', to=settings.AUTH_USER_MODEL),
        ),
    ]
