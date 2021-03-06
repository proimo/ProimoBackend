# Generated by Django 3.1 on 2020-09-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20200909_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='slug',
            field=models.SlugField(max_length=100, null=True, verbose_name='alias'),
        ),
        migrations.AlterField(
            model_name='county',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='slug',
            field=models.SlugField(max_length=100, null=True, verbose_name='alias'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='ultima modificare'),
        ),
    ]
