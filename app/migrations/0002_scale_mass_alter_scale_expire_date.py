# Generated by Django 5.0.1 on 2024-01-17 12:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scale',
            name='mass',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scale',
            name='expire_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
