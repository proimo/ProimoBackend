# Generated by Django 3.1 on 2020-09-08 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='locality',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='locality',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localities', related_query_name='locality', to='common.county', verbose_name='judeţ'),
        ),
    ]