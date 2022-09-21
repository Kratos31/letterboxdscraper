
import requests
from bs4 import BeautifulSoup as bs
import json

url = 'https://letterboxd.com/film/jojo-rabbit/'

r = requests.get(url)
soup = bs(r.text, 'lxml')

script_w_data = soup.select_one('script[type="application/ld+json"]')
json_obj = json.loads(script_w_data.text.split(' */')[1].split('/* ]]>')[0])
print(json_obj['image'])