# Generated by Django 5.0.4 on 2024-11-04 17:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_alter_producto_tipo_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
