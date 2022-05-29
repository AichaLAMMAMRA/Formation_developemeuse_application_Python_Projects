

import requests

from validators import url
from link.links import MAIN_PAGE
from libScrapBooks.book import scrapBook
from libScrapBooks.categories import scrapAllCategories



print("\n_______Start scraping _________ \n")

valid = url(MAIN_PAGE)

try:

	valid = url(MAIN_PAGE)
	scrapAllCategories(MAIN_PAGE)

except ValueError:

	print("Oops!  That was no valid url.  Try again...")


print("\n_______End scraping _________ \n")




