# Generated by Django 3.1 on 2020-09-04 15:12

from django.db import migrations, models
import django.db.models.deletion
import common.utils


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_auto_20200904_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialPropertySaleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to=common.utils.get_upload_path, verbose_name='imagine')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sales.specialpropertysale')),
            ],
            options={
                'verbose_name': 'imagine',
                'verbose_name_plural': 'imagini',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OfficeSaleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to=common.utils.get_upload_path, verbose_name='imagine')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sales.officesale')),
            ],
            options={
                'verbose_name': 'imagine',
                'verbose_name_plural': 'imagini',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LandSaleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to=common.utils.get_upload_path, verbose_name='imagine')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sales.landsale')),
            ],
            options={
                'verbose_name': 'imagine',
                'verbose_name_plural': 'imagini',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndustrialSpaceSaleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to=common.utils.get_upload_path, verbose_name='imagine')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sales.industrialspacesale')),
            ],
            options={
                'verbose_name': 'imagine',
                'verbose_name_plural': 'imagini',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HouseSaleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to=common.utils.get_upload_path, verbose_name='imagine')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sales.housesale')),
            ],
            options={
                'verbose_name': 'imagine',
                'verbose_name_plural': 'imagini',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommercialSpaceSaleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to=common.utils.get_upload_path, verbose_name='imagine')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sales.commercialspacesale')),
            ],
            options={
                'verbose_name': 'imagine',
                'verbose_name_plural': 'imagini',
                'abstract': False,
            },
        ),
    ]
