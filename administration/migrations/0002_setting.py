# Generated by Django 3.1 on 2020-08-18 15:10

from django.db import migrations, models
import django.utils.timezone
import common.utils


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=500)),
                ('slug', models.CharField(default=None, max_length=500)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('value', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=common.utils.get_upload_path)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
    ]
