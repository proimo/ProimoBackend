# Generated by Django 3.1 on 2020-08-18 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Setting',
        ),
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='title',
        ),
        migrations.AddField(
            model_name='announcement',
            name='name',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='announcement',
            name='slug',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
