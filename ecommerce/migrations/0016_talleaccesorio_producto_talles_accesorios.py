# Generated by Django 5.0.4 on 2024-11-08 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_alter_producto_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalleAccesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='talles_accesorios',
            field=models.ManyToManyField(blank=True, null=True, to='ecommerce.talleaccesorio'),
        ),
    ]
