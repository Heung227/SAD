import json
import sys
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder

from currency_country.models import Country


class Command(BaseCommand):
    help = "Extracting user data to JSON format"

    def handle(self, *args, **options):
        # Get User Data from User Model in monolith        
        countries_microservice_data = Country.objects.all()
        for country_data in countries_microservice_data:
            data = {
                "model": "Country",
                "country_name": country_data.country_name,
                "local_currency": country_data.local_currency,
                "added_on": country_data.added_on,
            }
            # Dumping Data into JSON Format
            json.dump(data, sys.stdout, cls=DjangoJSONEncoder)
            sys.stdout.write("\n")