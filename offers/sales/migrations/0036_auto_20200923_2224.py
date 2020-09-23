# Generated by Django 3.1 on 2020-09-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0035_auto_20200923_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentsale',
            name='postal_code',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='cod poştal'),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='postal_code',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='cod poştal'),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='postal_code',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='cod poştal'),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='postal_code',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='cod poştal'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='postal_code',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='cod poştal'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='postal_code',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='cod poştal'),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='postal_code',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='cod poştal'),
        ),
    ]