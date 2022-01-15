from time import sleep
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://alert.shop-bell.com/books/magazine/3/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
sleep(1)

#comics = soup.find_all('tr', style='background-color:#eeeeee')
comics = soup.select('table[id="reflow"] > tbody > tr')
d_list = []
for comic in comics:
    title = comic.find('a').text
    author = comic.find('span', attrs={'class': 'muted'}).text
    #release_date = comic.find('td', attrs={'class': 'srpLatest'}).text.split('巻')[1]
    release_date = comic.find('td', attrs={'class': 'srpLatest'}).text
    if '巻' in release_date:
        release_date = release_date.split('巻')[1]
    d = {'title': title, 'author': author, 'release_date': release_date}
    d_list.append(d)

from pprint import pprint
pprint(d_list, width=50, sort_dicts=False)
