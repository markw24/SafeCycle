from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand
from SafeCycle.application.models import Road


class Command(BaseCommand):
    def handle(self, *args, **options):
        for row in DictReader(open('./street_names.csv')):
            road = Road()
            road.name = row[0]
            road.save()

