# Generated by Django 3.2.19 on 2023-06-01 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DynamoDiviaky', '0011_alter_hraci_registracne_cislo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hraci',
            name='tim',
        ),
    ]
