# Generated by Django 5.2.1 on 2025-05-30 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='inventario',
        ),
    ]
