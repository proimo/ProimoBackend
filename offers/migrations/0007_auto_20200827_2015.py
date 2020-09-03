# Generated by Django 3.1 on 2020-08-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0006_auto_20200827_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='is_for_sale',
            field=models.CharField(choices=[('selling', 'Voi vinde'), ('rent', 'Voi închiria')], default='rent', max_length=10),
        ),
        migrations.AlterField(
            model_name='commercialspace',
            name='is_for_sale',
            field=models.CharField(choices=[('selling', 'Voi vinde'), ('rent', 'Voi închiria')], default='rent', max_length=10),
        ),
        migrations.AlterField(
            model_name='house',
            name='is_for_sale',
            field=models.CharField(choices=[('selling', 'Voi vinde'), ('rent', 'Voi închiria')], default='rent', max_length=10),
        ),
        migrations.AlterField(
            model_name='industrialspace',
            name='is_for_sale',
            field=models.CharField(choices=[('selling', 'Voi vinde'), ('rent', 'Voi închiria')], default='rent', max_length=10),
        ),
        migrations.AlterField(
            model_name='land',
            name='is_for_sale',
            field=models.CharField(choices=[('selling', 'Voi vinde'), ('rent', 'Voi închiria')], default='rent', max_length=10),
        ),
        migrations.AlterField(
            model_name='office',
            name='is_for_sale',
            field=models.CharField(choices=[('selling', 'Voi vinde'), ('rent', 'Voi închiria')], default='rent', max_length=10),
        ),
        migrations.AlterField(
            model_name='specialproperty',
            name='is_for_sale',
            field=models.CharField(choices=[('selling', 'Voi vinde'), ('rent', 'Voi închiria')], default='rent', max_length=10),
        ),
    ]