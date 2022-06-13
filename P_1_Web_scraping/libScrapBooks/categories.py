import os
import csv
import requests


from bs4 import BeautifulSoup                               

from link.links import MAIN_PAGE
from  libScrapBooks import book



def scrap_all_categories (main_page) :

    ''' Fonction contenant l'extraction successive des catégories des livres '''
   
    categories = []
    soup = book.scrap_url_book (main_page)  
    
    # Récupérer toutes les catégories de livres
    for category in soup.select('.side_categories ul > li > ul > li > a'):
        categories.append({"name": category.text.strip(), "url": MAIN_PAGE + category["href"]}) 

    for categorie in categories :
        scrap_by_category(categorie["url"])
        

def scrap_by_category (url_categorie):
    
    '''Récupération des données de tous les livres d'une catégorie'''

    all_books_infos = []
    
    soup = book.scrap_url_book(url_categorie) 
    category_name =  soup.find('h1').text   

    nb_pages = nombre_page_categorie(soup)

    if nb_pages > 1:

        for i in range (1, nb_pages + 1):
            url = url_categorie.replace('index.html', 'page-' + str(i) + '.html')
            soup = book.scrap_url_book(url)
            all_books_infos += scrap_books_of_category(soup)
    else:

        all_books_infos += scrap_books_of_category(soup)

    csv_books_category(all_books_infos, category_name)
    download_imag_category(all_books_infos)   

def scrap_books_of_category (soup):
    book_infos = []
    all_books_infos = []
    all_h3 = soup.findAll('h3')
    
    for h3 in all_h3:
        link_to_books = h3.select('a')
        for a in link_to_books:
            url_book = MAIN_PAGE + 'catalogue/' + a['href'].strip('../../../')
            book_infos = book.scrap_Book(url_book)
            all_books_infos.append(book_infos)

    return all_books_infos

def csv_books_category (books_infos,category_name):
    '''
    Creation le fichier csv qui contient les données des livres de categorie.
    Tous ces fichiers csv sont rangés dans un dossier (nomé par csv files: 
    '''
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

def download_imag_category (all_books_infos):
    

    path = "pictures"

    if not os.path.exists(path):
        os.makedirs(path)

    for book in all_books_infos:

        universal_product_code = book["universal_product_code"]
        with open(path + '/' + universal_product_code + ".jpg", "wb") as file :
            url_image = book["product_page_url"]
            response = requests.get(url_image)
            file.write(response.content)


def nombre_page_categorie (soup):

    ''' Cette fonction détermine le nombre de pages pour une catégorie '''
    
    page = (soup.find("li", {"class": "current"}))

    if page is None:
        nb_page = 1

    else:
        page = str(page)
        page = page.split()[5]
        nb_page = int (page)

    return nb_page
