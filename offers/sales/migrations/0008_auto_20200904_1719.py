# Generated by Django 3.1 on 2020-09-04 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20200904_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartmentsaleimage',
            options={'verbose_name': 'imagine', 'verbose_name_plural': 'imagini'},
        ),
        migrations.RenameField(
            model_name='apartmentsaleimage',
            old_name='apartment',
            new_name='offer',
        ),
    ]
