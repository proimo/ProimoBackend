# Generated by Django 3.1 on 2020-08-19 20:00

from django.db import migrations, models
import common.utils


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0008_auto_20200819_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to=common.utils.get_upload_path, verbose_name='Imagine'),
        ),
    ]
