
import requests

from libScrapBooks.book import scrapBook
from libScrapBooks.categories import scrapAllCategories

main_page ="http://books.toscrape.com/"



dict= []


print("\n_______start scraping _________ \n")

#dict = book.scrapBook(url)
scrapAllCategories('http://books.toscrape.com/')


print("\n_______finish scraping _________\n")

