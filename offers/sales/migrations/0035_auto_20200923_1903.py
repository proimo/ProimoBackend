# Generated by Django 3.1 on 2020-09-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0034_auto_20200921_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialpropertysale',
            name='building_stage',
            field=models.CharField(blank=True, choices=[('Există', 'Există'), ('În construcţie', 'În construcţie'), ('Proiect', 'Proiect')], default=None, max_length=15, verbose_name='stadiu construcţie'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='building_state',
            field=models.CharField(blank=True, choices=[('Modernizat', 'Modernizat'), ('Nemodernizat', 'Nemodernizat')], default=None, max_length=15, verbose_name='stare imobil'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='building_type',
            field=models.CharField(default=None, max_length=100, verbose_name='tip imobil'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='building_year',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='an finalizare construcţie'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='buyer_commission',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='comision cumpărător'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='contract',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_conditioning',
            field=models.BooleanField(default=False, verbose_name='climă'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_current',
            field=models.BooleanField(default=False, verbose_name='curent'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_entresol',
            field=models.BooleanField(default=False, verbose_name='mezanin'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_exclusivity',
            field=models.BooleanField(default=False, verbose_name='exclusivitate'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_gas',
            field=models.BooleanField(default=False, verbose_name='gaz'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_ground_floor',
            field=models.BooleanField(default=True, verbose_name='parter'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_heating',
            field=models.BooleanField(default=False, verbose_name='căldură'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_mansard',
            field=models.BooleanField(default=False, verbose_name='mansardă'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_parking_possibility',
            field=models.BooleanField(default=False, verbose_name='posibilitate parcare'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_semi_basement',
            field=models.BooleanField(default=False, verbose_name='demisol'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_sewerage',
            field=models.BooleanField(default=False, verbose_name='canalizare'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_terrace',
            field=models.BooleanField(default=False, verbose_name='terasă'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='has_water',
            field=models.BooleanField(default=False, verbose_name='apă'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='hide_price',
            field=models.BooleanField(default=False, verbose_name='nu doresc să fie afişat vizitatorilor site-ului'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='levels_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. niveluri'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='not_include_vat',
            field=models.BooleanField(default=False, verbose_name='nu include TVA'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='occupation_degree',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='grad ocupare clădire (%)'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='parking_spaces_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. locuri parcare'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='price',
            field=models.PositiveIntegerField(default=None, verbose_name='preţ cerut'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='price_currency',
            field=models.CharField(choices=[('eur', 'EUR'), ('ron', 'RON'), ('usd', 'USD')], default='eur', max_length=4, verbose_name=''),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='price_details',
            field=models.TextField(blank=True, default=None, verbose_name='alte detalii preţ'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='property_description',
            field=models.TextField(blank=True, default=None, max_length=100, verbose_name='descriere proprietate'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='property_name',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='nume proprietate'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='purpose_recommendation',
            field=models.CharField(blank=True, choices=[('pentru investiţie', 'pentru investiţie'), ('pentru utilizare proprie', 'pentru utilizare proprie'), ('există şi produce venituri', 'există şi produce venituri')], default=None, max_length=30, verbose_name='recomandare utilizare proprietate'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='space_height',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, verbose_name='înalţime spaţiu'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='terrain_surface',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='suprafaţă teren (mp)'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='total_surface',
            field=models.PositiveIntegerField(default=None, verbose_name='suprafaţă totală (mp)'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='underground_levels_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. niveluri subterane'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='validity_from',
            field=models.DateTimeField(blank=True, default=None, verbose_name='valabilitate de la'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='validity_up_to',
            field=models.DateTimeField(blank=True, default=None, verbose_name='până la'),
        ),
        migrations.AddField(
            model_name='specialpropertysale',
            name='zero_commission',
            field=models.BooleanField(default=False, verbose_name='comision 0%'),
        ),
    ]
