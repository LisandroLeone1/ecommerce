# Generated by Django 5.0.4 on 2024-10-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_producto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('novedades', 'Novedades'), ('destacados', 'Destacados'), ('sale', 'Sale')], max_length=20, null=True),
        ),
    ]
