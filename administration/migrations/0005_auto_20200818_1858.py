# Generated by Django 3.1 on 2020-08-18 15:58

from django.db import migrations, models
import django.utils.timezone
import main.utils
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creat'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.utils.get_file_name, verbose_name='Imagine'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='name',
            field=models.CharField(default=None, max_length=500, verbose_name='Nume'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ultima modificare'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Valoare'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=None, upload_to='profile_pics', verbose_name='Imagine profil'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Număr de telefon'),
        ),
    ]