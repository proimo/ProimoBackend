# Generated by Django 3.1 on 2020-09-08 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200908_2153'),
        ('rents', '0008_auto_20200908_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentrent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apartmentrents', related_query_name='apartmentrent', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='apartmentrent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apartmentrents', related_query_name='apartmentrent', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='apartmentrent',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='commercialspacerent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercialspacerents', related_query_name='commercialspacerent', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='commercialspacerent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercialspacerents', related_query_name='commercialspacerent', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='commercialspacerent',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='houserents', related_query_name='houserent', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='houserents', related_query_name='houserent', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='industrialspacerent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='industrialspacerents', related_query_name='industrialspacerent', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='industrialspacerent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='industrialspacerents', related_query_name='industrialspacerent', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='industrialspacerent',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='landrent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='landrents', related_query_name='landrent', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='landrent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='landrents', related_query_name='landrent', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='landrent',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='officerent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officerents', related_query_name='officerent', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='officerent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officerents', related_query_name='officerent', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='officerent',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='specialpropertyrent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialpropertyrents', related_query_name='specialpropertyrent', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='specialpropertyrent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialpropertyrents', related_query_name='specialpropertyrent', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='specialpropertyrent',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
    ]