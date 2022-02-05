from random import randint
from decimal import Decimal
from main import get_content_from_imdb,ConnectApp
from time import sleep
import settings


def _get_directors_star(item):
    element = item.find('div', class_='lister-item-content').findAll('p')[-2]
    directors = []
    stars = []
    content = ",".join([str(tag) for tag in element.contents])
    count_directos = content.split('Star')[0].count('<a')
    a_tags = element.findAll('a')
    for director in a_tags[0:count_directos]:
        person_slug = director.get('href').split('/')[2]
        person_name = director.text
        directors.append(dict(slug=person_slug, name=person_name))

    for star in a_tags[count_directos:len(a_tags)]:
        person_slug = star.get('href').split('/')[2]
        person_name = star.text
        stars.append(dict(slug=person_slug, name=person_name))
    return directors, stars


def _get_duration(item):
    duration = 0
    if item.find('span', class_='runtime') is not None:
        pre_duration = item.find('span', class_='runtime').text
        duration = int(str(pre_duration).split(' ')[0])
    return duration


def _get_votes_gross(item):
    gross = 0.0
    votes = item.find('p', class_='sort-num_votes-visible').findAll('span', {'name': 'nv'})[0].get('data-value')
    if 'Gross' in item.find('p', class_='sort-num_votes-visible').text:
        gross = item.find('p', class_='sort-num_votes-visible').findAll('span', {'name': 'nv'})[1].text.split('$')[1].split('M')[0]
    return votes, gross


def _get_score(item):
    score = 0
    if 'Metascore' in item.find('div', class_='ratings-bar').text:
        score = item.find('div', class_='ratings-metascore').find('span', class_='metascore').text
    return score


def _scrap_movie(genre, start=1):
    url = f"https://www.imdb.com/search/title/?genres={genre}&languages=en&start={start}"
    content = get_content_from_imdb(url)
    movies = []
    for item in content.findAll('div', class_='lister-item'):
        is_rating = item.find('div', class_='ratings-bar')
        is_director = 'Director' in item.find('div', class_='lister-item-content').text
        if is_rating is not None and is_director:
            slug = item.find("h3", class_='lister-item-header').find('a').get('href').split('/')[2]
            image = item.find("div", class_='lister-item-image').find('img').get('src')
            title = item.find("h3", class_='lister-item-header').find('a').text
            published = item.find("span", class_='lister-item-year').text.split('(')[1].split(')')[0].strip()
            duration = _get_duration(item)
            genres = item.find('span', class_='genre').text.strip().split(', ')
            rate = Decimal(item.find('div', class_='ratings-bar').find('strong').text)
            summary = item.findAll('p', class_='text-muted')[1].text
            directors, stars = _get_directors_star(item)
            votes, gross = _get_votes_gross(item)
            score = _get_score(item)

            data_movie = {'slug': slug, 'image': image, 'title': title, 'published': published,
                          'duration': duration, 'genres': genres, 'rate': float(rate), 'summary': summary,
                          'votes': int(votes), 'gross': gross, 'score': score,
                          'directors': [director.get('slug') for director in directors],
                          'stars': [star.get('slug') for star in stars]}

            movies.append(data_movie)
    return movies


def movies_scraping(genre, count_page=1):
    movies = []
    for page in range(1, count_page + 1):
        start = ((page - 1) * 50) + 1
        sleep(randint(10, 30))
        result = _scrap_movie(genre, start)
        movies.extend(result)
    return movies


def create_movie(movie):
    ConnectApp().post(settings.URL_MOVIE_CREATE_APP, data=movie)


def create_movies(list_movie):
    for movie in list_movie:
        create_movie(movie)


def list_movie():
    result = ConnectApp().get(settings.URL_MOVIE_LIST_APP)
    return result[1]


def get_movie(id):
    result = ConnectApp().get(settings.URL_MOVIE_GET_APP + id)
    return result[1]


def delete_movie(id):
    ConnectApp().delete(settings.URL_MOVIE_DELETE_APP + id)


