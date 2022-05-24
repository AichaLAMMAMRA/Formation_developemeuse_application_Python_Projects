
import requests
from libScrapBooks.category import scrape_categories

main_page ="http://books.toscrape.com/"




print("\n_______start scraping _________ \n")

#scrape_category.scrape__all_books_category (url)
scrape_categories(main_page)

print("\n_______finish scraping _________\n")

