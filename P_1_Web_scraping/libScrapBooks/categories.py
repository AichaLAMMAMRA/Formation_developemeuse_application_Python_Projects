import os                               # module système pour navigation dans arborescence dossiers
import re                               # import tout bs4 pour test type objet
import csv
import requests

from bs4 import BeautifulSoup
from  libScrapBooks import book



def scrapAllCategories (main_page) :

	#______Fonction contenant l'extraction successive des catégories des livres_____#
   
	categories = []
	soup = book.scrapUrlBook (main_page)  
	
	# Récupérer toutes les catégories de livres
	for category in soup.select('.side_categories ul > li > ul > li > a'):
		categories.append({"name": category.text.strip(), "url": "http://books.toscrape.com/" + category["href"]}) 

	for categorie in categories :
		scrapByCategory(categorie["url"])
		

def scrapByCategory (url_categorie):
	
	'''Récupération des données de tous les livres d'une catégorie'''

	all_books_infos = []
	
	soup = book.scrapUrlBook(url_categorie) 
	category_name =  soup.find('h1').text 	

	nb_pages = nombrePageCategorie(soup)

	if nb_pages > 1:

		for i in range (1, nb_pages + 1):
			url = url_categorie.replace('index.html', 'page-' + str(i) + '.html')
			soup = book.scrapUrlBook(url)
			all_books_infos += scrapBooksOfCategory(soup)
	else:

		all_books_infos += scrapBooksOfCategory(soup)

	csvBooksCategory(all_books_infos, category_name)
	downloadImagCategory(all_books_infos)	

def scrapBooksOfCategory (soup):
	book_infos = []
	all_books_infos = []
	all_h3 = soup.findAll('h3')
	
	for h3 in all_h3:
		link_to_books = h3.select('a')
		for a in link_to_books:
			url_book ='http://books.toscrape.com/' + 'catalogue/' + a['href'].strip('../../../')
			book_infos = book.scrapBook(url_book)
			all_books_infos.append(book_infos)

	return all_books_infos

def csvBooksCategory (books_infos,category_name):
	path = "csv_files"

	if not os.path.exists(path):
		os.makedirs(path)
	with open (path + '/' + category_name + '.csv','w', encoding='UTF8',newline = "") as bookFile:
		dict_writer = csv.writer(bookFile)
		# Ecrire les en-têtes
		dict_writer.writerow(books_infos[0].keys()) 

		# Ecrire les informations du livre 
		for book_info in books_infos :
			dict_writer.writerow(book_info.values())

def downloadImagCategory (all_books_infos):
	path = "pictures"

	if not os.path.exists(path):
		os.makedirs(path)

	for book in all_books_infos:

		universal_product_code = book["universal_product_code"]
		with open(path + '/' + universal_product_code + ".jpg", "wb") as file :
			url_image = book["product_page_url"]
			response = requests.get(url_image)
			file.write(response.content)


def nombrePageCategorie (soup):

	''' Cette fonction détermine le nombre de pages pour une catégorie '''
	page = (soup.find("li", {"class": "current"}))

	if page is None:
		nb_page = 1

	else:
		page = str(page)
		page = page.split()[5]
		nb_page = int (page)
		print("nb_pages ", nb_page)

	return nb_page
