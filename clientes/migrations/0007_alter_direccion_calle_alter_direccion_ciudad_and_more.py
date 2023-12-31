# Generated by Django 4.2.7 on 2023-12-24 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientes', '0006_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='calle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='ciudad',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='codigo_postal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='comuna',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='region',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
