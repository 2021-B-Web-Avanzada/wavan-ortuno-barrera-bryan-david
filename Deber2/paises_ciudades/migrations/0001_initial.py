# Generated by Django 4.0 on 2021-12-16 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=100)),
                ('fundacion', models.DateField()),
                ('presidente', models.CharField(max_length=100)),
                ('poblacion', models.IntegerField()),
                ('prefijo_telefonico', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_capital', models.BooleanField(default=False)),
                ('fundacion', models.DateField()),
                ('superficie', models.DecimalField(decimal_places=2, max_digits=3)),
                ('poblacion', models.IntegerField()),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paises_ciudades.pais')),
            ],
        ),
    ]