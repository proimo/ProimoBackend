from django.db.models import TextChoices


class ApartmentType(TextChoices):
    APARTAMENT = 'apartament'
    GARSONIERA = 'garsoniera'
    PENTHOUSE = 'penthouse'


class PartitioningType(TextChoices):
    DECOMANDAT = 'decomandat'
    SEMIDECOMANDAT = 'semidecomandat'
    NEDECOMANDAT = 'nedecomandat'
    CIRCULAR = 'circular'
    VAGON = 'vagon'


class Comfort(TextChoices):
    I = 1
    II = 2
    III = 3
    LUX = 'lux'


class BuildingType(TextChoices):
    APARTMENTS_BUILDING = 'bloc-de-apartamente', 'bloc de apartamente'
    HOUSE_OR_VILLA = 'casa-vila', 'casă/vilă'


class BuildingPeriod(TextChoices):
    _1941 = '_1941', 'Înainte de 1941'
    _1941_1977 = '1941_1977', 'Între 1941 şi 1977'
    _1977_1990 = '1977_1990', 'Între 1977 şî 1990'
    _1990_2000 = '1990_2000', 'Între 1990 şi 2000'
    _2000_2010 = '2000_2010', 'Între 2000 şi 2010'
    _2010 = '2010_', 'După 2010'


class ResistanceStructure(TextChoices):
    BETON = 'beton'
    CARAMIDA = 'caramida', 'cărămidă'
    BCA = 'bca'
    LEMN = 'lemn'
    METALE = 'metale'
    ALTELE = 'altele'


class Currencies(TextChoices):
    EUR = 'eur', 'EUR'
    RON = 'ron', 'RON'
    USD = 'usd', 'USD'


class Sector(TextChoices):
    ONE = '1', '1'
    TWO = '2', '2'
    THREE = '3', '3'
    FOUR = '4', '4'
    FIVE = '5', '5'
    SIX = '6', '6'


class Level(TextChoices):
    DEMISOL = 'demisol'
    PARTER = 'parter'
    ETAJ1 = 'etaj-1', 'Etaj 1'
    ETAJ2 = 'etaj-2', 'Etaj 2'
    ETAJ3 = 'etaj-3', 'Etaj 3'
    ETAJ4 = 'etaj-4', 'Etaj 4'
    ETAJ5 = 'etaj-5', 'Etaj 5'
    ETAJ6 = 'etaj-6', 'Etaj 6'
    ETAJ7 = 'etaj-7', 'Etaj 7'
    ETAJ8 = 'etaj-8', 'Etaj 8'
    ETAJ9 = 'etaj-9', 'Etaj 9'
    ETAJ10 = 'etaj-10', 'Etaj 10'
    ETAJ11 = 'etaj-11', 'Etaj 11'
    ETAJ12 = 'etaj-12', 'Etaj 12'
    ETAJ13 = 'etaj-13', 'Etaj 13'
    ETAJ14 = 'etaj-14', 'Etaj 14'
    ETAJ15 = 'etaj-15', 'Etaj 15'
    ETAJ16 = 'etaj-16', 'Etaj 16'
    ETAJ17 = 'etaj-17', 'Etaj 17'
    ETAJ18 = 'etaj-18', 'Etaj 18'
    ETAJ19 = 'etaj-19', 'Etaj 19'
    ETAJ20 = 'etaj-20', 'Etaj 20'
    ETAJ21 = 'etaj-21', 'Etaj 21'
    ETAJ22 = 'etaj-22', 'Etaj 22'
    ETAJ23 = 'etaj-23', 'Etaj 23'
    ETAJ24 = 'etaj-24', 'Etaj 24'
    ETAJ25 = 'etaj-25', 'Etaj 25'
    ETAJ26 = 'etaj-26', 'Etaj 26'
    ETAJ27 = 'etaj-27', 'Etaj 27'
    ETAJ28 = 'etaj-28', 'Etaj 28'
    ETAJ30 = 'etaj-30', 'Etaj 30'
    ETAJ31 = 'etaj-31', 'Etaj 31'
    ETAJ32 = 'etaj-32', 'Etaj 32'
    ETAJ33 = 'etaj-33', 'Etaj 33'
    ETAJ34 = 'etaj-34', 'Etaj 34'
    ETAJ35 = 'etaj-35', 'Etaj 35'
    ETAJ36 = 'etaj-36', 'Etaj 36'
    ETAJ37 = 'etaj-37', 'Etaj 37'
    ETAJ38 = 'etaj-38', 'Etaj 38'
    ETAJ39 = 'etaj-39', 'Etaj 39'
    ETAJ40 = 'etaj-40', 'Etaj 40'
    MANSARDA = 'mansarda'
    LAST2 = 'ultimele-2-etaje', 'Ultimele 2 etaje'
