# Generated by Django 3.1.5 on 2023-05-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HraciePlochy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nazov', models.CharField(max_length=50, verbose_name='Názov')),
                ('umiestnenie', models.CharField(max_length=80, verbose_name='Miesto')),
            ],
        ),
        migrations.CreateModel(
            name='Rezervacie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Dátum')),
                ('start_time', models.TimeField(verbose_name='Čas od')),
                ('end_time', models.TimeField(verbose_name='Čas do')),
            ],
        ),
        migrations.CreateModel(
            name='Sutaze',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nazov', models.CharField(max_length=60, verbose_name='Názov')),
                ('zvaz', models.CharField(max_length=80, verbose_name='Zväz')),
            ],
        ),
        migrations.CreateModel(
            name='Timy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('skratka', models.CharField(max_length=5, verbose_name='Skratka')),
                ('nazov', models.CharField(max_length=50, verbose_name='Názov')),
            ],
        ),
    ]
