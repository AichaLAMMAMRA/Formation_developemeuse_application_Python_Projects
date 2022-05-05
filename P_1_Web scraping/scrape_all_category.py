import requests
import os
import re
import csv
from slugify import slugify
import scrape_book
import scrape_category



def scrape_categories (main_page) :
	categories = []

	soup = scrape_book.scrape_url_book (main_page)  
	# Récupérer toutes les catégories de livres

	for category in soup.select('.side_categories ul > li > ul > li > a'):
		categories.append({"name": category.text.strip(), "url": "http://books.toscrape.com/" + category["href"]}) #print (categorie)
		#categories.append({"name": category.text.strip(), "url": "http://books.toscrape.com/" + category["href"]}) #print (categorie)



	for categorie in categories :
		scrape_category.scrape__all_books_category(categorie["url"])
		





