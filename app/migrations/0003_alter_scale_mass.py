# Generated by Django 5.0.1 on 2024-01-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_scale_mass_alter_scale_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scale',
            name='mass',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
