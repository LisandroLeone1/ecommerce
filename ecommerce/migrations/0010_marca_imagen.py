# Generated by Django 5.0.4 on 2024-11-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_alter_producto_descuento_alter_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos/'),
        ),
    ]
