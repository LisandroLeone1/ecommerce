# Generated by Django 5.0.4 on 2025-03-19 14:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce', '0020_alter_color_color_style'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carro', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarroItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carro.carro')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carro',
            name='productos',
            field=models.ManyToManyField(through='carro.CarroItem', to='ecommerce.producto'),
        ),
    ]
