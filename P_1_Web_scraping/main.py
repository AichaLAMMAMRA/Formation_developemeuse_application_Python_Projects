

import requests
import time

from validators import url
from link.links import MAIN_PAGE
from libScrapBooks.categories import scrap_all_categories



print("\n_______Start scraping _________ \n")

valid = url(MAIN_PAGE)

try:

    valid = url(MAIN_PAGE)
    start = time.time()
    scrap_all_categories(MAIN_PAGE)
    end = time.time()

    elapsed = end - start
    print(f'Temps d\'exécution : {elapsed:.2}ms')


except ValueError:

    print("Oops!  That was no valid url.  Try again...")


print("\n_______End scraping _________ \n")




