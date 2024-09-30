from bs4 import BeautifulSoup
import requests as rq

burl = 'https://books.toscrape.com/'

bheader = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

bresp = rq.get(url=burl, headers=bheader)
bsoup = BeautifulSoup(bresp.content, 'html.parser')

a = []

books = bsoup.find_all('article', class_='product_pod')

for book in books:
    booktitle = book.h3.a['title']  
    bookprice = book.find('p', class_='price_color').text  
    bookrating = book.find('p', class_=['star-rating'])['class'][1]  

    a.append({
        'booktitle': booktitle,
        'bookprice': bookprice,
        'bookrating': bookrating
    })

print(a)