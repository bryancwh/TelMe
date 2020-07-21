import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()

from products.models import Product
from scrapers.starhubscraper import add_starhub_products
from scrapers.singtelscraper import add_singtel_products
from scrapers.myrepublicscraper import add_myrepublic_products
from scrapers.m1scraper import add_m1_products
from scrapers.gigascraper import add_giga_products
from scrapers.add_products import add_all_products

if __name__ == '__main__':
    add_starhub_products()
    add_singtel_products()
    add_myrepublic_products()
    add_m1_products()
    add_giga_products()
    add_all_products()
    print('Done.')
