# Generated by Django 3.1.5 on 2023-05-26 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DynamoDiviaky', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezervacie',
            name='tim',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DynamoDiviaky.timy'),
        ),
        migrations.AddField(
            model_name='timy',
            name='koniec_jar',
            field=models.DateField(null=True, verbose_name='Dátum'),
        ),
        migrations.AddField(
            model_name='timy',
            name='koniec_jesen',
            field=models.DateField(null=True, verbose_name='Dátum'),
        ),
        migrations.AddField(
            model_name='timy',
            name='start_jar',
            field=models.DateField(null=True, verbose_name='Dátum'),
        ),
        migrations.AddField(
            model_name='timy',
            name='start_jesen',
            field=models.DateField(null=True, verbose_name='Dátum'),
        ),
    ]