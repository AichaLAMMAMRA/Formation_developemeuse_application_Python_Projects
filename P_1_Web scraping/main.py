
import requests
import scrape_book
import scrape_category
import scrape_all_category

url = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"

main_page ="http://books.toscrape.com/"



'''dict= []
dict= scrape_book.scrape_page_book(url)
scrape_book.create_csv_book_category (dict)
#print(dict)
'''
print("\n_______start scraping _________ \n")

#scrape_category.scrape__all_books_category (url)
scrape_all_category.scrape_categories(main_page)

print("\n_______finish scraping _________\n")


#match