# Generated by Django 3.1 on 2020-09-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0019_auto_20200923_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentrent',
            name='neighborhood',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='vecinătăţi'),
        ),
        migrations.AlterField(
            model_name='commercialspacerent',
            name='neighborhood',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='vecinătăţi'),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='neighborhood',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='vecinătăţi'),
        ),
        migrations.AlterField(
            model_name='industrialspacerent',
            name='neighborhood',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='vecinătăţi'),
        ),
        migrations.AlterField(
            model_name='landrent',
            name='neighborhood',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='vecinătăţi'),
        ),
        migrations.AlterField(
            model_name='officerent',
            name='neighborhood',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='vecinătăţi'),
        ),
        migrations.AlterField(
            model_name='specialpropertyrent',
            name='neighborhood',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='vecinătăţi'),
        ),
    ]
