# Generated by Django 3.1 on 2020-09-13 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0019_auto_20200914_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentsale',
            name='id',
            field=models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='apartmentsale',
            name='name',
            field=models.CharField(db_index=True, default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='id',
            field=models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commercialspacesale',
            name='name',
            field=models.CharField(db_index=True, default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='id',
            field=models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='name',
            field=models.CharField(db_index=True, default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='id',
            field=models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='industrialspacesale',
            name='name',
            field=models.CharField(db_index=True, default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='id',
            field=models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='name',
            field=models.CharField(db_index=True, default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='id',
            field=models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='officesale',
            name='name',
            field=models.CharField(db_index=True, default=None, max_length=500, verbose_name='nume'),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='id',
            field=models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='specialpropertysale',
            name='name',
            field=models.CharField(db_index=True, default=None, max_length=500, verbose_name='nume'),
        ),
    ]
