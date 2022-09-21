import requests
import json
from bs4 import BeautifulSoup

def letterboxd(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'referer': 'https://google.com',
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    item = {}

    title = soup.find('meta', {'property': 'og:title'}).get('content')
    cast = [cast.text for cast in soup.find_all('a', {'class': 'text-slug tooltip'})]
    directors = [directors.text for directors in soup.find_all('span', {'class': 'prettify'})]
    rating = soup.find('meta', {'name': 'twitter:data2'}).get('content')
    genres = soup.find('div', {'class': 'text-sluglist capitalize'})
    genres = [genres.text for genres in genres.find_all('a', {'class': 'text-slug'})]
    producers = soup.find_all('div', {'class': 'text-sluglist'})[2]
    producers = [producers.text for producers in producers.find_all('a')]
    writers = soup.find_all('div', {'class': 'text-sluglist'})[3]
    writers = [writers.text for writers in writers.find_all('a')]
    year = soup.find('small', {'class': 'number'}).text
    description = soup.find('meta', {'property': 'og:description'}).get('content')
    r = requests.get(url)
    
    
    

    item['title'] = title
    item['release year'] = year
    item['director(s)'] = directors
    item['cast'] = cast
    item['rating'] = rating
    item['genres'] = genres
    item['producer(s)'] = producers
    item['writer(s)'] = writers
    item['description'] = description

    #poster function

    script_w_data = soup.select_one('script[type="application/ld+json"]')
    json_obj = json.loads(script_w_data.text.split(' */')[1].split('/* ]]>')[0])
    item['poster'] = json_obj
    

    

    movie = url.split('/')[-2]

    r = requests.get(f'https://letterboxd.com/esi/film/{movie}/stats/', headers=headers)

    soup = BeautifulSoup(r.content, 'lxml')


    watched_by = soup.find('a', {'class': 'has-icon icon-watched icon-16 tooltip'}).text
    listed_by = soup.find('a', {'class': 'has-icon icon-list icon-16 tooltip'}).text
    liked_by = soup.find('a', {'class': 'has-icon icon-like icon-liked icon-16 tooltip'}).text

    item['watched by'] = watched_by
    item['listed by'] = listed_by
    item['liked by'] = liked_by
    with open(f'{movie}.json', 'w') as f:
        json.dump(item, f,  indent=2)
    print(item)
movie=input("Enter movie name:")
movie_url= "https://letterboxd.com/film/" + movie.replace(" ",'-')
letterboxd(movie_url)