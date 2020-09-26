# Generated by Django 3.1 on 2020-09-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0026_auto_20200926_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialpropertyrent',
            name='building_stage',
            field=models.CharField(blank=True, choices=[('Există', 'Există'), ('În construcţie', 'În construcţie'), ('Proiect', 'Proiect')], default=None, max_length=15, verbose_name='stadiu construcţie'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='building_state',
            field=models.CharField(blank=True, choices=[('Modernizat', 'Modernizat'), ('Nemodernizat', 'Nemodernizat')], default=None, max_length=15, verbose_name='stare imobil'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='building_type',
            field=models.CharField(default=None, max_length=50, verbose_name='tip proprietate/imobil'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='building_year',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='an finalizare construcţie'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='contract',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_conditioning',
            field=models.BooleanField(default=False, verbose_name='climă'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_current',
            field=models.BooleanField(default=False, verbose_name='curent'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_entresol',
            field=models.BooleanField(default=False, verbose_name='mezanin'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_exclusivity',
            field=models.BooleanField(default=False, verbose_name='exclusivitate'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_gas',
            field=models.BooleanField(default=False, verbose_name='gaz'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_ground_floor',
            field=models.BooleanField(default=True, verbose_name='parter'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_heating',
            field=models.BooleanField(default=False, verbose_name='căldură'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_mansard',
            field=models.BooleanField(default=False, verbose_name='mansardă'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_parking_possibility',
            field=models.BooleanField(default=False, verbose_name='posibilitate parcare'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_semi_basement',
            field=models.BooleanField(default=False, verbose_name='demisol'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_sewerage',
            field=models.BooleanField(default=False, verbose_name='canalizare'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_terrace',
            field=models.BooleanField(default=False, verbose_name='terasă'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='has_water',
            field=models.BooleanField(default=False, verbose_name='apă'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='levels_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. niveluri'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='parking_spaces_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. locuri parcare'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='property_description',
            field=models.TextField(blank=True, default=None, max_length=100, verbose_name='descriere proprietate'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='property_name',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='nume proprietate'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='terrain_surface',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=6, verbose_name='suprafaţă teren (mp)'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='total_surface',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=6, verbose_name='suprafaţă totală (mp)'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='underground_levels_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. niveluri subterane'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='validity_from',
            field=models.DateTimeField(blank=True, default=None, verbose_name='valabilitate de la'),
        ),
        migrations.AddField(
            model_name='specialpropertyrent',
            name='validity_up_to',
            field=models.DateTimeField(blank=True, default=None, verbose_name='până la'),
        ),
    ]