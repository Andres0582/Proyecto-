# Generated by Django 5.2.1 on 2025-06-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0005_inventario_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='comentario',
            field=models.CharField(default='Sin categoría', max_length=80),
        ),
    ]
