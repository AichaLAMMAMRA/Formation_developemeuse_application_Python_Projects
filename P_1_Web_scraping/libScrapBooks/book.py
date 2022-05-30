import os                               # module système pour navigation dans arborescence dossiers  
import re                            
import csv
import requests                        # module qui permet d'interagir avec une url

from bs4 import BeautifulSoup
from link.links import MAIN_PAGE





def scrap_Book(url_book):

    ''' Extraire des données d'un livre et enregistrer ses données  dans un dictionnaire 
    Args:
        url_book : url de la page des détails d'un livre
    Return:
        book_infos: dictionnaire des données du livres 
    '''
    soup = scrap_url_book(url_book)
    # Scrape le titre du livre                                         
    book_title = soup.find('h1').text
    # Scrape le titre de la catégorie
    book_category = get_category_book(soup)  
    # Scrape l'url de l'image                           
    imag_url = soup.select('img')[0]
    book_imag_link = MAIN_PAGE + imag_url.get('src').strip('../../')
    # crape la notation
    book_review_rating = scrub_review_rating(soup)
    # Scrape la description du livre                
    book_product_description = soup.select('article > p')[0].text

    product_info = soup.select('table.table')

    for info in product_info :
        book_universal_product_code = info.select('tr > td')[0].text
        book_price_no_tax = scrub_price(info.select('tr > td')[2].text)         
        book_price_with_tax = scrub_price(info.select('tr > td')[3].text)
        book_availabity = scrub_book_avail_nbr(info.select('tr > td')[5].text)
        

    book_infos ={
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

    #csv_one_book(book_infos)

    return book_infos

def scrap_url_book(url_request):

    '''Scrape l'url du livre puis analysez son html'''

    response = requests.get(url_request)
    if (response.ok):
        soup = BeautifulSoup(response.content, 'html.parser')

    return soup

def get_category_book (soup):

    category_book = soup.select('ul.breadcrumb')

    for element in category_book:
        book_category= element.select('li')[2].text.strip()
    
    return book_category

def scrub_review_rating(soup):

    ''' Conversion du rating en lettre par un chiffre '''

    review_rating_book = soup.find('p', class_='star-rating').get('class')[1] 
    switcher = {
        'One':1,
        'Two':2,
        'Three':3, 
        'Four':4,
        'Five':5,
        }

    return  switcher.get(review_rating_book, "None")  

def scrub_price(price):

    '''Retirer le symbole inutile dans  le prix) '''

    price = re.sub('£', '', price)  
    return price

def scrub_book_avail_nbr (nb_available):
    
    '''Extraire que le nombre de livre disponible '''

    res=int(re.search(r'\d+', nb_available)[0])
    return res
'''
def csv_one_book (bookInfos): 
    
    directory = "csv_one_book"
    category_folder = bookInfos["category"] 
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(os.path.join(directory, category_folder)):
        os.makedirs(os.path.join(directory, category_folder))

    with open (directory + '/'+ category_folder + '/'+ bookInfos["universal_product_code"]+'.csv','w', newline='') as bookFile:

        for info in bookInfos:
            bookFile.write("%s,%s\n"%(info,bookInfos[info]))
'''










    
