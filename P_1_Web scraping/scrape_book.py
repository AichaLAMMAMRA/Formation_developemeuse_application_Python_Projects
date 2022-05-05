
import requests
import csv

from bs4 import BeautifulSoup


main_page ="http://books.toscrape.com/"

"""Scrape target URL for book."""

def scrape_page_book(url_book):
	#print("scrape_page_book")
	soup = scrape_url_book(url_book)       	                               
	book_title = soup.find('h1').text                                  #Scrape book title  
	book_category = get_categor_book(soup)                            #Scrape book category
	imag_url = soup.select('img')[0]
	book_imag_link = main_page + imag_url.get('src').strip('../../')    #Scrape image_url
	book_review_rating = get_star_rating_book(soup)                    #Scrape review rating, number of stars
	book_product_description = soup.select('article > p')[0].text       #Scrape product_description    

	product_info = soup.select('table.table')                           
	for info in product_info:
		  book_universal_product_code = info.select('tr > td')[0].text  #Scrapeuniversal_ product_code (upc)
		  book_price_no_tax = info.select('tr > td')[2].text            #Scrapeprice_excluding_tax
		  book_price_with_tax = info.select('tr > td')[3].text          #Scrapeprice_including_tax
		  book_availabity = info.select('tr > td')[5].text              #Scrape number_available
   
	book_infos = {
	             "title": book_title,
	             "category": book_category, 
	             "review_rating": book_review_rating,
	             "product_page_url": book_imag_link,
	             "number_available": book_availabity,
		         "price_including_tax": book_price_with_tax, 
		         "price_excluding_tax": book_price_no_tax,
		         "product_description": book_product_description,
		         "universal_product_code": book_universal_product_code	     
		         }  
 
	return book_infos

""" Scrape url of the book then analyse its html"""
def scrape_url_book(url_request):
	#print("scrape_url_book")
	response = requests.get(url_request)
	if (response.ok):
		soup = BeautifulSoup(response.content, 'html.parser')

	return soup

def get_categor_book (soup):
	#print("get_categor_book")
	category_book = soup.select('ul.breadcrumb')
	##print (category_book)
	for element in category_book:
		book_category= element.select('li')[2].text.strip()
	return book_category

def get_star_rating_book(soup):
	#print("get_star_rating_book")
	review_rating_book = soup.find('p', class_='star-rating').get('class')[1] + ' stars'
	return review_rating_book


	





