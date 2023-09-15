from database import Product, create_engine
from sqlalchemy.orm import sessionmaker
import requests
from bs4 import BeautifulSoup

# Database Function
def opendb():
    engine = create_engine('sqlite:///example.db')
    Session = sessionmaker(bind=engine)
    return Session()
def save(product):
    db = opendb()
    db.add(product)
    db.commit()
    db.close()
    print("Product saved")

def get_soup():
    url = 'https://www.flipkart.com/search?q=tv'
    try:
        page = requests.get(url)
        if page.status_code == 200:
           print('success!')
           return BeautifulSoup(page.text, 'html.parser')
        elif page.status_code == 404:
            print('page not found!')
        elif page.status_code == 503:
           print('service unavailabe')
    except Exception as e:
        print('Error',e)

def extract(soup):
    target = soup.find('div', class_ = '_1YokD2 _3Mn1Gg')
    if not target:
       print('target found')
       return
    products = target.find_all('div', class_ = '_1AtVbE col-12-12')
    if not products:
       print('products not found')
       return
    total = len(products)
    print('products found')
    print('total products: ', total)
    for item in products:
        try:title = item.find('div', class_ = '_4rR01T').text
        except: title = None
        review_n_rating = item.find('span', class_='_2_R_DZ').text
        price = item.find('div', class_='_30jeq3 _1_WHN1').text
        products = Product(
            title = title,
            rrcount = review_n_rating,
            price = price
        )
        save(products)

if __name__ == '__main__':
    soup = get_soup()
    try:
        extract(soup)
        print("Done")
    except Exception as e:
        print("Could not get data",e)

   
    