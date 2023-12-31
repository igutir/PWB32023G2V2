# Generated by Django 4.2.5 on 2023-09-25 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechacompra', models.DateField()),
                ('totalcompra', models.IntegerField()),
                ('numerotarjeta', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('rut', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigaGames.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='cover')),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigaGames.categoria')),
                ('compania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigaGames.compania')),
            ],
        ),
        migrations.CreateModel(
            name='Compra_juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigaGames.juego')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigaGames.compra')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigaGames.usuario'),
        ),
    ]
