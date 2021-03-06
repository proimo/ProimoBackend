# Generated by Django 3.1 on 2020-09-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200908_2153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='county',
            options={'ordering': ['name'], 'verbose_name': 'judeţ', 'verbose_name_plural': 'judeţe'},
        ),
        migrations.AlterModelOptions(
            name='locality',
            options={'ordering': ['name'], 'verbose_name': 'localitate', 'verbose_name_plural': 'localităţi'},
        ),
        migrations.AddIndex(
            model_name='county',
            index=models.Index(fields=['id'], name='common_coun_id_533e2b_idx'),
        ),
        migrations.AddIndex(
            model_name='county',
            index=models.Index(fields=['name'], name='common_coun_name_15a987_idx'),
        ),
        migrations.AddIndex(
            model_name='locality',
            index=models.Index(fields=['id'], name='common_loca_id_b3e1cb_idx'),
        ),
        migrations.AddIndex(
            model_name='locality',
            index=models.Index(fields=['county'], name='common_loca_county__f5ea96_idx'),
        ),
        migrations.AddIndex(
            model_name='locality',
            index=models.Index(fields=['county', 'id'], name='common_loca_county__9bedd4_idx'),
        ),
        migrations.AddIndex(
            model_name='locality',
            index=models.Index(fields=['name'], name='common_loca_name_5afdcd_idx'),
        ),
    ]
