# Generated by Django 3.1 on 2020-09-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20200904_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='slug',
            field=models.CharField(db_index=True, default=None, max_length=500, null=True),
        ),
    ]
