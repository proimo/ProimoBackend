# Generated by Django 3.1 on 2020-09-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20200909_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True, verbose_name='alias'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True, verbose_name='alias'),
        ),
    ]
