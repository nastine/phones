import csv
from datetime import date
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)


            for line in phone_reader:
                phones = Phone.objects.get_or_create(
                id = line[0],
                name=line[1],
                image=line[2],
                price=int(line[3]),
                release_date=line[4],
                lte_exists=line[5]
                )[0]
                phones.save()
