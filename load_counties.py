import json
import os
import django
from typing import Dict, List

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

django.setup()
from common.models import County, Locality


def sanitize(value: str) -> str:
    return value.lower() \
        .replace(' ', '-') \
        .replace('ă', 'a') \
        .replace('â', 'a') \
        .replace('î', 'i') \
        .replace('ş', 's') \
        .replace('ţ', 't')


def main():
    try:
        with open('judete.json', 'r') as file:
            print('Running counties loader...')
            counties: List[Dict] = json.load(file)['judete']
            for county in counties:
                county_name: str = county['nume']
                county_slug = sanitize(county_name)
                county_obj = County.objects.get_or_create(slug=county_slug, name=county_name)[0]
                localities: List[Dict] = county['localitati']
                for locality in localities:
                    locality_name: str = locality['nume']
                    locality_slug = sanitize(locality_name)
                    locality_obj = \
                        Locality.objects.get_or_create(slug=locality_slug, name=locality_name, county=county_obj)[0]
        print('Done!')
    except KeyError as err:
        print('You file is not properly configured!')
        print(err)
    except Exception as err:
        print(f'Error occurred: {err}')


if __name__ == '__main__':
    main()
