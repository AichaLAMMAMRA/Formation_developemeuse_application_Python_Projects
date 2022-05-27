
import requests

from validators import url
from link.links import MAIN_PAGE
from libScrapBooks.book import scrapBook
from libScrapBooks.categories import scrapAllCategories




dict= []


print("\n_______start scraping _________ \n")

valid = url(MAIN_PAGE)
'''
if valid==True:
    print("Url is valid")
    scrapAllCategories(MAIN_PAGE)

else:
    print("Invalid url")

'''
try:
	valid = url(MAIN_PAGE)
	scrapAllCategories(MAIN_PAGE)

except ValueError:
	print("Oops!  That was no valid url.  Try again...")



