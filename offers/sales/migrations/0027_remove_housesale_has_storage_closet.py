# Generated by Django 3.1 on 2020-09-21 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0026_auto_20200921_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housesale',
            name='has_storage_closet',
        ),
    ]
