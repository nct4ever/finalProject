# Generated by Django 4.0.1 on 2023-04-20 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0007_alter_shipping_table_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
