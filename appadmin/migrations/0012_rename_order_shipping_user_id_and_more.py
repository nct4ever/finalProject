# Generated by Django 4.0.1 on 2023-04-21 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0011_remove_shipping_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping',
            old_name='order',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='member_id',
        ),
    ]
