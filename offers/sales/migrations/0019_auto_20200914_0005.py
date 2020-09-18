# Generated by Django 3.1 on 2020-09-13 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0018_auto_20200914_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentsale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
    ]