import os
import re
import csv
import requests
from bs4 import BeautifulSoup
from  libScrapBooks import scrapBooks



def scrape_categories (main_page) :

	#______Fonction contenant l'extraction successive des catégories des livres_____#
   
	categories = []
	soup = scrapBooks.scrape_url_book (main_page)  
	
	# Récupérer toutes les catégories de livres
	for category in soup.select('.side_categories ul > li > ul > li > a'):
		categories.append({"name": category.text.strip(), "url": "http://books.toscrape.com/" + category["href"]}) #print (categorie)
		#categories.append({"name": category.text.strip(), "url": "http://books.toscrape.com/" + category["href"]}) #print (categorie)

	for categorie in categories :
		scrape__all_books_category(categorie["url"])
		

def scrape__all_books_category (url_categorie):

	all_books_infos = []
	soup = scrapBooks.scrape_url_book(url_categorie) 
	category_name =  soup.find('h1').text  
	#print (" _________ Extraire les donnees de la categorie : ", category_name,"____________")

	page = (soup.find("li", {"class": "current"}))

	if page is None:
		all_books_infos += get_all_books_informations(soup,category_name)
		create_csv_books_category(all_books_infos, category_name)
		download_images_Category (all_books_infos)
		#diplay_books_names(all_books_infos)


	else:
		page = str(page)
		page = page.split()[5]
		nb_pages = int (page)
		print("nb_pages ", nb_pages)

		for i in range (1, nb_pages + 1):
			url = url_categorie.replace('index.html', 'page-' + str(i) + '.html')
			soup = scrapBooks.scrape_url_book(url)
			all_books_infos += get_all_books_informations(soup)

		create_csv_books_category(all_books_infos, category_name)
		download_images_Category(all_books_infos, category_name)
		diplay_books_names(all_books_infos)


def get_all_books_informations (soup):
	book_infos = []
	all_books_infos = []
	all_h3 = soup.findAll('h3')
	
	for h3 in all_h3:
		link_to_books = h3.select('a')
		for a in link_to_books:
			url_book ='http://books.toscrape.com/' + 'catalogue/' + a['href'].strip('../../../')
			book_infos = scrapBooks.scrape_page_book(url_book)
			all_books_infos.append(book_infos)

	return all_books_infos

def create_csv_books_category (books_infos,category_name):
	path = "csv_files"

	if not os.path.exists(path):
		os.makedirs(path)
	with open (path + '/' + category_name + '.csv','w', encoding='UTF8',newline = "") as bookFile:
		dict_writer = csv.writer(bookFile)
		# write headers
		dict_writer.writerow(books_infos[0].keys()) 

		# write book informations 
		for book_info in books_infos :
			dict_writer.writerow(book_info.values())

def download_images_Category (all_books_infos):
	#path = "pictures" + "_of_ " + category_name + "_category"
	path = "pictures"

	if not os.path.exists(path):
		os.makedirs(path)

	for book in all_books_infos:

		universal_product_code = book["universal_product_code"]
		with open(path + '/' + universal_product_code + ".jpg", "wb") as file :
			url_image = book["product_page_url"]
			response = requests.get(url_image)
			file.write(response.content)
	'''for book in all_books_infos:
		universal_product_code = re.sub('[^a-zA-Z0-9 \n]', '', book["universal_product_code"])
	
		if universal_product_code 
		    print(words.split().pop(0))
        else 
        '''
		


def diplay_books_names (all_books_infos):

	for book in all_books_infos :
		print ( book["universal_product_code"])
		
