# Generated by Django 3.2.20 on 2023-07-12 12:33

from django.db import migrations, models
import django.db.models.deletion


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
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('skratka', models.CharField(max_length=5, unique=True, verbose_name='Skratka')),
                ('nazov', models.CharField(max_length=50, verbose_name='Názov')),
                ('start_jesen', models.DateField(null=True, verbose_name='Dátum')),
                ('koniec_jesen', models.DateField(null=True, verbose_name='Dátum')),
                ('start_jar', models.DateField(null=True, verbose_name='Dátum')),
                ('koniec_jar', models.DateField(null=True, verbose_name='Dátum')),
            ],
        ),
        migrations.CreateModel(
            name='TypZapasu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nazov', models.CharField(max_length=50, verbose_name='Názov')),
            ],
        ),
        migrations.CreateModel(
            name='Zaujem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=50, verbose_name='Záujem')),
            ],
        ),
        migrations.CreateModel(
            name='Rezervacie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(verbose_name='Dátum')),
                ('start_time', models.TimeField(verbose_name='Čas od')),
                ('end_time', models.TimeField(verbose_name='Čas do')),
                ('hracieplochy', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DynamoDiviaky.hracieplochy')),
                ('tim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DynamoDiviaky.timy')),
                ('typzapasu', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DynamoDiviaky.typzapasu')),
            ],
        ),
        migrations.CreateModel(
            name='Hraci',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('hrac', models.CharField(max_length=80, verbose_name='Celé meno')),
                ('meno', models.CharField(max_length=80, verbose_name='Meno')),
                ('priezvisko', models.CharField(max_length=80, verbose_name='Priezvisko')),
                ('matersky_klub', models.CharField(max_length=50, verbose_name='Materský klub')),
                ('hostujuci_klub', models.CharField(max_length=50, verbose_name='Hosťujúci klub')),
                ('klubova_prislusnost', models.CharField(max_length=50, verbose_name='Klubová príslušnosť')),
                ('hostovanie', models.CharField(max_length=50, verbose_name='Hosťovanie')),
                ('clenske_od', models.DateField(verbose_name='Členské od')),
                ('clenske_do', models.DateField(verbose_name='Členské do')),
                ('registracne_cislo', models.CharField(max_length=12, unique=True, verbose_name='Registračné číslo')),
                ('datum_narodenia', models.DateField(verbose_name='Dátum narodenia')),
                ('platnost_rp', models.DateField(verbose_name='Platnosť reg.preukazu')),
                ('aktivita', models.CharField(max_length=1, verbose_name='Aktivita')),
                ('stav', models.CharField(max_length=12, verbose_name='Stav')),
                ('tim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DynamoDiviaky.timy')),
            ],
        ),
    ]
