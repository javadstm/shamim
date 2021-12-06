from django.core.management.base import BaseCommand, CommandError

from healthcenter.management.startup.cities import PROVINCES
from healthcenter.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        for item in PROVINCES:
            district, _ = state.objects.get_or_create(name=PROVINCES[item]['name'])
            for city in PROVINCES[item]['cities']:
                city.objects.get_or_create(state=district, name=city['name'])
