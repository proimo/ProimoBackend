# Generated by Django 3.1 on 2020-08-14 14:14

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='image',
            field=models.ImageField(null=True, upload_to=main.utils.get_file_name),
        ),
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.CharField(max_length=200, null=True),
        ),
    ]