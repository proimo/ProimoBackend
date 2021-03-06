# Generated by Django 3.1 on 2020-09-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0014_auto_20200917_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentrent',
            name='bathrooms_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. băi'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='building_type',
            field=models.CharField(choices=[('bloc-de-apartamente', 'bloc de apartamente'), ('casa-vila', 'casă/vilă')], default='bloc-de-apartamente', max_length=20, verbose_name='tip imobil'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='buyer_commission',
            field=models.TextField(blank=True, default=None, verbose_name='Comision cumpărător'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='comfort',
            field=models.CharField(blank=True, choices=[('1', 'I'), ('2', 'Ii'), ('3', 'Iii'), ('lux', 'Lux')], default=None, max_length=3, verbose_name='confort'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='constructed_surface',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='suprafaţa construită'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='level',
            field=models.CharField(blank=True, choices=[('demisol', 'Demisol'), ('parter', 'Parter'), ('etaj-1', 'Etaj 1'), ('etaj-2', 'Etaj 2'), ('etaj-3', 'Etaj 3'), ('etaj-4', 'Etaj 4'), ('etaj-5', 'Etaj 5'), ('etaj-6', 'Etaj 6'), ('etaj-7', 'Etaj 7'), ('etaj-8', 'Etaj 8'), ('etaj-9', 'Etaj 9'), ('etaj-10', 'Etaj 10'), ('etaj-11', 'Etaj 11'), ('etaj-12', 'Etaj 12'), ('etaj-13', 'Etaj 13'), ('etaj-14', 'Etaj 14'), ('etaj-15', 'Etaj 15'), ('etaj-16', 'Etaj 16'), ('etaj-17', 'Etaj 17'), ('etaj-18', 'Etaj 18'), ('etaj-19', 'Etaj 19'), ('etaj-20', 'Etaj 20'), ('etaj-21', 'Etaj 21'), ('etaj-22', 'Etaj 22'), ('etaj-23', 'Etaj 23'), ('etaj-24', 'Etaj 24'), ('etaj-25', 'Etaj 25'), ('etaj-26', 'Etaj 26'), ('etaj-27', 'Etaj 27'), ('etaj-28', 'Etaj 28'), ('etaj-30', 'Etaj 30'), ('etaj-31', 'Etaj 31'), ('etaj-32', 'Etaj 32'), ('etaj-33', 'Etaj 33'), ('etaj-34', 'Etaj 34'), ('etaj-35', 'Etaj 35'), ('etaj-36', 'Etaj 36'), ('etaj-37', 'Etaj 37'), ('etaj-38', 'Etaj 38'), ('etaj-39', 'Etaj 39'), ('etaj-40', 'Etaj 40'), ('mansarda', 'Mansarda'), ('ultimele-2-etaje', 'Ultimele 2 etaje')], default=None, max_length=17, verbose_name='etaj'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='levels_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. niveluri'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='other_details',
            field=models.TextField(blank=True, default=None, max_length=500, verbose_name='alte detalii'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='partitioning_type',
            field=models.CharField(blank=True, choices=[('decomandat', 'Decomandat'), ('semidecomandat', 'Semidecomandat'), ('nedecomandat', 'Nedecomandat'), ('circular', 'Circular'), ('vagon', 'Vagon')], default=None, max_length=15, verbose_name='tip compartimentare'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='rent_cost',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='chirie/lună'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='rent_currency',
            field=models.CharField(choices=[('eur', 'EUR'), ('ron', 'RON'), ('usd', 'USD')], default='eur', max_length=4, verbose_name=''),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='rooms_nr',
            field=models.PositiveIntegerField(default=0, verbose_name='nr. camere'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='util_surface',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='suprafaţa utilă'),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='zero_commission',
            field=models.BooleanField(default=False, verbose_name='Comision 0%'),
        ),
    ]
