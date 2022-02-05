from time import sleep
from random import randint
import settings
from main import get_content_from_imdb,ConnectApp
import json


def _scrap_stars(start=1):
    content = get_content_from_imdb(settings.URL_STAR_SCARPING + str(start))
    stars = []
    for item in content.findAll('div', class_='lister-item'):
        id = item.find('h3').find('a').get('href').split('/')[-1]
        name = item.find('h3').find('a').text
        bio = str(item.findAll('p')[-1].text).strip()
        image = item.find('div', class_='lister-item-image').find('img').get('src')
        data = {'id': id, 'name': name, 'bio': bio, 'image': image}
        stars.append(data)
    return stars


def _scrap_star(id):
    url = f'https://www.imdb.com/name/{id}/bio'
    content = get_content_from_imdb(url)
    image = content.find('img', class_='poster').get('src')
    bio = content.find('div', {'id': 'bio_content'}).find('div', class_='soda').find('p').contents[0].strip()
    name = content.find('div', {'id': 'main'}).find('div', class_='parent').find('h3').text.strip()
    return {'name': name, 'bio': bio, 'image': image}


def get_star_incomplete():
    return ConnectApp().get(settings.URL_STAR_LIST_INCOMPLETE_APP)[1]


def stars_scraping(count_page=1):
    stars = []
    for page in range(1, count_page + 1):
        start = ((page - 1) * 50) + 1
        sleep(randint(10, 30))
        stars.extend(_scrap_stars(start))
    return stars


def create_stars(list_star):
    for star in list_star:
        create_star(star)


def create_star(star):
    ConnectApp().post(settings.URL_STAR_CREATE_APP, data=star)


def list_star():
    result = ConnectApp().get(settings.URL_STAR_LIST_APP)
    return result[1]


def get_star(id):
    result = ConnectApp().get(settings.URL_STAR_GET_APP + id)
    return result[1]


def delete_star(id):
    ConnectApp().delete(settings.URL_STAR_DELETE_APP + id)


def update_star(id, data):
    ConnectApp().put(settings.URL_STAR_UPDATE_APP + id, data)


def star_complete():
    stars = json.loads(get_star_incomplete())
    for star in stars[:3]:
        sleep(5)
        update_star(star['id'], _scrap_star(star['id']))


