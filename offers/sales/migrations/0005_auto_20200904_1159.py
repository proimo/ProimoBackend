# Generated by Django 3.1 on 2020-09-04 08:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20200904_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentsale',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creat'),
        ),
        migrations.AlterField(
            model_name='apartmentsale',
            name='name',
            field=models.CharField(default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='apartmentsale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creat'),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='name',
            field=models.CharField(default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creat'),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='name',
            field=models.CharField(default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creat'),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='name',
            field=models.CharField(default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creat'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='name',
            field=models.CharField(default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creat'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='name',
            field=models.CharField(default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creat'),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='name',
            field=models.CharField(default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificare'),
        ),
    ]
