# Generated by Django 3.1 on 2020-09-04 08:19

import ckeditor_uploader.fields
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=500, verbose_name='Nume')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creat')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ultima modificare')),
                ('slug', models.CharField(default=None, max_length=500, null=True)),
                ('address', django.contrib.gis.db.models.fields.PointField(max_length=200, null=True, srid=4326, verbose_name='Adresă')),
                ('region', models.CharField(blank=True, default=None, max_length=200, verbose_name='Regiune')),
                ('price', models.CharField(blank=True, default=None, max_length=15, verbose_name='Preţ')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publicat?')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, verbose_name='Conţinut')),
            ],
            options={
                'verbose_name': 'Apartament',
                'verbose_name_plural': 'Apartamente',
            },
        ),
        migrations.CreateModel(
            name='CommercialSpaceRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=500, verbose_name='Nume')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creat')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ultima modificare')),
                ('slug', models.CharField(default=None, max_length=500, null=True)),
                ('address', django.contrib.gis.db.models.fields.PointField(max_length=200, null=True, srid=4326, verbose_name='Adresă')),
                ('region', models.CharField(blank=True, default=None, max_length=200, verbose_name='Regiune')),
                ('price', models.CharField(blank=True, default=None, max_length=15, verbose_name='Preţ')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publicat?')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, verbose_name='Conţinut')),
            ],
            options={
                'verbose_name': 'Spaţiu comercial',
                'verbose_name_plural': 'Spaţii comerciale',
            },
        ),
        migrations.CreateModel(
            name='HouseRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=500, verbose_name='Nume')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creat')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ultima modificare')),
                ('slug', models.CharField(default=None, max_length=500, null=True)),
                ('address', django.contrib.gis.db.models.fields.PointField(max_length=200, null=True, srid=4326, verbose_name='Adresă')),
                ('region', models.CharField(blank=True, default=None, max_length=200, verbose_name='Regiune')),
                ('price', models.CharField(blank=True, default=None, max_length=15, verbose_name='Preţ')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publicat?')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, verbose_name='Conţinut')),
            ],
            options={
                'verbose_name': 'Casă',
                'verbose_name_plural': 'Case',
            },
        ),
        migrations.CreateModel(
            name='IndustrialSpaceRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=500, verbose_name='Nume')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creat')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ultima modificare')),
                ('slug', models.CharField(default=None, max_length=500, null=True)),
                ('address', django.contrib.gis.db.models.fields.PointField(max_length=200, null=True, srid=4326, verbose_name='Adresă')),
                ('region', models.CharField(blank=True, default=None, max_length=200, verbose_name='Regiune')),
                ('price', models.CharField(blank=True, default=None, max_length=15, verbose_name='Preţ')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publicat?')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, verbose_name='Conţinut')),
            ],
            options={
                'verbose_name': 'Spaţiu industrial',
                'verbose_name_plural': 'Spaţii industriale',
            },
        ),
        migrations.CreateModel(
            name='LandRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=500, verbose_name='Nume')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creat')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ultima modificare')),
                ('slug', models.CharField(default=None, max_length=500, null=True)),
                ('address', django.contrib.gis.db.models.fields.PointField(max_length=200, null=True, srid=4326, verbose_name='Adresă')),
                ('region', models.CharField(blank=True, default=None, max_length=200, verbose_name='Regiune')),
                ('price', models.CharField(blank=True, default=None, max_length=15, verbose_name='Preţ')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publicat?')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, verbose_name='Conţinut')),
            ],
            options={
                'verbose_name': 'Teren',
                'verbose_name_plural': 'Terenuri',
            },
        ),
        migrations.CreateModel(
            name='OfficeRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=500, verbose_name='Nume')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creat')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ultima modificare')),
                ('slug', models.CharField(default=None, max_length=500, null=True)),
                ('address', django.contrib.gis.db.models.fields.PointField(max_length=200, null=True, srid=4326, verbose_name='Adresă')),
                ('region', models.CharField(blank=True, default=None, max_length=200, verbose_name='Regiune')),
                ('price', models.CharField(blank=True, default=None, max_length=15, verbose_name='Preţ')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publicat?')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, verbose_name='Conţinut')),
            ],
            options={
                'verbose_name': 'Birou',
                'verbose_name_plural': 'Birouri',
            },
        ),
        migrations.CreateModel(
            name='SpecialPropertyRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=500, verbose_name='Nume')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creat')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ultima modificare')),
                ('slug', models.CharField(default=None, max_length=500, null=True)),
                ('address', django.contrib.gis.db.models.fields.PointField(max_length=200, null=True, srid=4326, verbose_name='Adresă')),
                ('region', models.CharField(blank=True, default=None, max_length=200, verbose_name='Regiune')),
                ('price', models.CharField(blank=True, default=None, max_length=15, verbose_name='Preţ')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publicat?')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, verbose_name='Conţinut')),
            ],
            options={
                'verbose_name': 'Proprietate specială',
                'verbose_name_plural': 'Proprietăţi speciale',
            },
        ),
    ]
