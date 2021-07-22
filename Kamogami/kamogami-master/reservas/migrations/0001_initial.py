# Generated by Django 3.2.3 on 2021-06-26 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slots', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('reference_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.TimeField()),
                ('end_hour', models.TimeField()),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('SCHEDULED', 'Agendado'), ('CANCELLED', 'Cancelado'), ('COMPLETED', 'Realizado')], max_length=15)),
                ('servicio', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='reservas.servicio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]