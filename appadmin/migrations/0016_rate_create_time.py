# Generated by Django 4.0.1 on 2023-04-24 03:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0015_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]