# Generated by Django 5.0.4 on 2024-11-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0016_talleaccesorio_producto_talles_accesorios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='talles_accesorios',
            field=models.ManyToManyField(default='TALLE UNICO', to='ecommerce.talleaccesorio'),
        ),
    ]
