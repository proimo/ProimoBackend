# Generated by Django 3.1 on 2020-09-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0031_auto_20200921_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officesale',
            name='has_entresol',
            field=models.BooleanField(default=False, verbose_name='mezanin'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='has_mansard',
            field=models.BooleanField(default=False, verbose_name='mansardă'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='has_terrace',
            field=models.BooleanField(default=False, verbose_name='terasă'),
        ),
    ]
