# Generated by Django 3.2.19 on 2023-06-02 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DynamoDiviaky', '0013_delete_hraci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timy',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]