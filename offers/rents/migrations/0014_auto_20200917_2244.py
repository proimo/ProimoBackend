# Generated by Django 3.1 on 2020-09-17 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0013_auto_20200914_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentrent',
            name='price',
        ),
        migrations.RemoveField(
            model_name='commercialspacerent',
            name='price',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='price',
        ),
        migrations.RemoveField(
            model_name='industrialspacerent',
            name='price',
        ),
        migrations.RemoveField(
            model_name='landrent',
            name='price',
        ),
        migrations.RemoveField(
            model_name='officerent',
            name='price',
        ),
        migrations.RemoveField(
            model_name='specialpropertyrent',
            name='price',
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='hide_address_on_imobiliare',
            field=models.BooleanField(default=False, verbose_name='ascunde adresa în imobiliare.ro'),
        ),
        migrations.AddField(
            model_name='commercialspacerent',
            name='hide_address_on_imobiliare',
            field=models.BooleanField(default=False, verbose_name='ascunde adresa în imobiliare.ro'),
        ),
        migrations.AddField(
            model_name='houserent',
            name='hide_address_on_imobiliare',
            field=models.BooleanField(default=False, verbose_name='ascunde adresa în imobiliare.ro'),
        ),
        migrations.AddField(
            model_name='industrialspacerent',
            name='hide_address_on_imobiliare',
            field=models.BooleanField(default=False, verbose_name='ascunde adresa în imobiliare.ro'),
        ),
        migrations.AddField(
            model_name='landrent',
            name='hide_address_on_imobiliare',
            field=models.BooleanField(default=False, verbose_name='ascunde adresa în imobiliare.ro'),
        ),
        migrations.AddField(
            model_name='officerent',
            name='hide_address_on_imobiliare',
            field=models.BooleanField(default=False, verbose_name='ascunde adresa în imobiliare.ro'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='hide_address_on_imobiliare',
            field=models.BooleanField(default=False, verbose_name='ascunde adresa în imobiliare.ro'),
        ),
    ]
