# Generated by Django 5.1.6 on 2025-03-25 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_fecha_reseña_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelicula_id', models.CharField(max_length=100)),
                ('accion', models.CharField(choices=[('reseñar', 'Reseñar'), ('calificar', 'Calificar'), ('guardar', 'Guardar')], max_length=20)),
                ('reseña', models.TextField(blank=True, null=True)),
                ('calificacion', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
