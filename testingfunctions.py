import requests
from bs4 import BeautifulSoup as bs
import json


movie=input("Enter movie name:") 

movie_url= "https://letterboxd.com/film/" + movie.replace(" ",'-')
print(movie_url)

page=requests.get(movie_url)
response=page.text
soup=bs(response, 'html.parser')
script = soup.find_all("script", {"type": "application/ld+json"}, string="image")

