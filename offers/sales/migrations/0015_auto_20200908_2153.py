# Generated by Django 3.1 on 2020-09-08 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200908_2153'),
        ('sales', '0014_auto_20200908_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentsale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apartmentsales', related_query_name='apartmentsale', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='apartmentsale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apartmentsales', related_query_name='apartmentsale', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='apartmentsale',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercialspacesales', related_query_name='commercialspacesale', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercialspacesales', related_query_name='commercialspacesale', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='housesales', related_query_name='housesale', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='housesales', related_query_name='housesale', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='industrialspacesales', related_query_name='industrialspacesale', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='industrialspacesales', related_query_name='industrialspacesale', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='landsales', related_query_name='landsale', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='landsales', related_query_name='landsale', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officesales', related_query_name='officesale', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officesales', related_query_name='officesale', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialpropertysales', related_query_name='specialpropertysale', to='common.county', verbose_name='judeţ'),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialpropertysales', related_query_name='specialpropertysale', to='common.locality', verbose_name='localitate'),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
    ]
