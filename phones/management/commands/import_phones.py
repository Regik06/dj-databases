import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = list(csv.DictReader(csvfile, delimiter=';'))

            for phone in phone_reader:
                Phone.objects.create(
                    id=phone['id'],
                    name=phone['name'],
                    image=phone['image'],
                    price=phone['price'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                    slug=slugify(phone['name']))

