# Generated by Django 4.0.1 on 2023-04-21 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0010_remove_orders_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='order_id',
        ),
    ]
