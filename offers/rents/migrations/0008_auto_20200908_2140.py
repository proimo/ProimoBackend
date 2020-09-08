# Generated by Django 3.1 on 2020-09-08 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('administration', '0013_auto_20200908_2140'),
        ('rents', '0007_auto_20200904_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentrent',
            name='region',
        ),
        migrations.RemoveField(
            model_name='commercialspacerent',
            name='region',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='region',
        ),
        migrations.RemoveField(
            model_name='industrialspacerent',
            name='region',
        ),
        migrations.RemoveField(
            model_name='landrent',
            name='region',
        ),
        migrations.RemoveField(
            model_name='officerent',
            name='region',
        ),
        migrations.RemoveField(
            model_name='specialpropertyrent',
            name='region',
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apartmentrents', related_query_name='apartmentrent', to='common.county'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apartmentrents', related_query_name='apartmentrent', to='common.locality'),
        ),
        migrations.AddField(
            model_name='commercialspacerent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercialspacerents', related_query_name='commercialspacerent', to='common.county'),
        ),
        migrations.AddField(
            model_name='commercialspacerent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercialspacerents', related_query_name='commercialspacerent', to='common.locality'),
        ),
        migrations.AddField(
            model_name='houserent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='houserents', related_query_name='houserent', to='common.county'),
        ),
        migrations.AddField(
            model_name='houserent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='houserents', related_query_name='houserent', to='common.locality'),
        ),
        migrations.AddField(
            model_name='industrialspacerent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='industrialspacerents', related_query_name='industrialspacerent', to='common.county'),
        ),
        migrations.AddField(
            model_name='industrialspacerent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='industrialspacerents', related_query_name='industrialspacerent', to='common.locality'),
        ),
        migrations.AddField(
            model_name='landrent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='landrents', related_query_name='landrent', to='common.county'),
        ),
        migrations.AddField(
            model_name='landrent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='landrents', related_query_name='landrent', to='common.locality'),
        ),
        migrations.AddField(
            model_name='officerent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officerents', related_query_name='officerent', to='common.county'),
        ),
        migrations.AddField(
            model_name='officerent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officerents', related_query_name='officerent', to='common.locality'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialpropertyrents', related_query_name='specialpropertyrent', to='common.county'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialpropertyrents', related_query_name='specialpropertyrent', to='common.locality'),
        ),
        migrations.AlterField(
            model_name='apartmentrent',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='commercialspacerent',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='industrialspacerent',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='landrent',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='officerent',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='specialpropertyrent',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
    ]
