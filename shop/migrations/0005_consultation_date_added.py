# Generated by Django 5.0.1 on 2024-04-22 17:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_consultation'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
