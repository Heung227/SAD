import json
import sys
import logging
from django.core.management.base import BaseCommand

from currency_country.models import Country

logger = logging.getLogger(_name_)

class Command(BaseCommand):
    help = "Populating User data obtained in JSON from Monolith."

    def handle(self, *args, **options):
        for line in sys.stdin:
            data = json.loads(line)

            # Populating User Model
            if data["model"] == "Country":
                country= Country(
                    country_name=data["country_name"],
                    local_currency=data["local_currency"],
                    added_on=data["added_on"],
                )
                country.save()
                logger.debug("Country populated:{}".format(country.country_name))
                print("Country populated:{}".format(country.country_name))