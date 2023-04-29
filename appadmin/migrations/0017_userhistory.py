# Generated by Django 4.0.1 on 2023-04-27 22:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0016_rate_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=1)),
                ('product', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'user_history',
            },
        ),
    ]