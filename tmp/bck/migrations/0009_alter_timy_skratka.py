# Generated by Django 3.2.19 on 2023-06-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DynamoDiviaky', '0008_rename_hrci_hraci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timy',
            name='skratka',
            field=models.CharField(max_length=5, unique=True, verbose_name='Skratka'),
        ),
    ]
