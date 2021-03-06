# Generated by Django 3.1 on 2020-08-19 20:00

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=500, verbose_name='Nume')),
                ('slug', models.CharField(default=None, max_length=500)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creat')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ultima modificare')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, region=None, verbose_name='Număr de contact')),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
    ]
