# Generated by Django 3.1 on 2020-09-08 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('administration', '0013_auto_20200908_2140'),
        ('sales', '0013_auto_20200904_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentsale',
            name='region',
        ),
        migrations.RemoveField(
            model_name='commercialspacesale',
            name='region',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='region',
        ),
        migrations.RemoveField(
            model_name='industrialspacesale',
            name='region',
        ),
        migrations.RemoveField(
            model_name='landsale',
            name='region',
        ),
        migrations.RemoveField(
            model_name='officesale',
            name='region',
        ),
        migrations.RemoveField(
            model_name='specialpropertysale',
            name='region',
        ),
        migrations.AddField(
            model_name='apartmentsale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apartmentsales', related_query_name='apartmentsale', to='common.county'),
        ),
        migrations.AddField(
            model_name='apartmentsale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apartmentsales', related_query_name='apartmentsale', to='common.locality'),
        ),
        migrations.AddField(
            model_name='commercialspacesale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercialspacesales', related_query_name='commercialspacesale', to='common.county'),
        ),
        migrations.AddField(
            model_name='commercialspacesale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercialspacesales', related_query_name='commercialspacesale', to='common.locality'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='housesales', related_query_name='housesale', to='common.county'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='housesales', related_query_name='housesale', to='common.locality'),
        ),
        migrations.AddField(
            model_name='industrialspacesale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='industrialspacesales', related_query_name='industrialspacesale', to='common.county'),
        ),
        migrations.AddField(
            model_name='industrialspacesale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='industrialspacesales', related_query_name='industrialspacesale', to='common.locality'),
        ),
        migrations.AddField(
            model_name='landsale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='landsales', related_query_name='landsale', to='common.county'),
        ),
        migrations.AddField(
            model_name='landsale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='landsales', related_query_name='landsale', to='common.locality'),
        ),
        migrations.AddField(
            model_name='officesale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officesales', related_query_name='officesale', to='common.county'),
        ),
        migrations.AddField(
            model_name='officesale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officesales', related_query_name='officesale', to='common.locality'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialpropertysales', related_query_name='specialpropertysale', to='common.county'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialpropertysales', related_query_name='specialpropertysale', to='common.locality'),
        ),
        migrations.AlterField(
            model_name='apartmentsale',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.userprofile'),
        ),
    ]