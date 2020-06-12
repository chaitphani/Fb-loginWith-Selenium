import requests
from bs4 import BeautifulSoup
import random
import urllib.request
import lxml

url = 'https://www.creativeshrimp.com/top-30-artworks-of-beeple.html'

form = requests.get(url).text

soup = BeautifulSoup(form, 'lxml')

for image in soup.find_all('a',{'class':'lightbox'}):
    href = image.get('href')
    print(href)

    image_name = random.randrange(1,200)
    full_name = str(image_name) + '.jpg'
    urllib.request.urlretrieve(href, full_name)

    print()
