# Generated by Django 4.0.1 on 2023-04-28 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0018_userrecommendation_delete_userhistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRecommendation',
        ),
    ]
