from decimal import Decimal
from time import sleep

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from app.models import Crypto


class Command(BaseCommand):
    help = 'Update currencies'
    base_url = 'https://coinmarketcap.com/currencies/'

    def handle(self, *args, **options):
        for cur in Crypto.objects.all():
            resp = requests.get(f'{self.base_url}{cur.url}')
            soup = BeautifulSoup(resp.text, 'html.parser')
            try:
                value = soup.select_one('.priceValue___11gHJ')
                cur.current_price = Decimal(value.text[1:])
                if cur.current_price > cur.highest_price:
                    cur.highest_price = cur.current_price
                    cur.highest_date = timezone.now()
                cur.save()
            except Exception as e:
                raise CommandError(f"Can't update currency {cur.name}, error: {e}")
            sleep(3)

        self.stdout.write(self.style.SUCCESS('Successfully updated currencies'))
