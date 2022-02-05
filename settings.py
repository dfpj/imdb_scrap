HEADER_EXTRA = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

BASE_URL_APP = 'http://127.0.0.1:8008/api/'

URL_AUTHORIZATHION = BASE_URL_APP + 'token/'
URL_ACCESS_KEY = BASE_URL_APP + 'token/refresh/'
URL_CHAECK_PERMISSION = BASE_URL_APP + 'star/list/'

# urls_scraping

URL_GENRES_SCARPING = "https://www.imdb.com/search/title/?genres=action&explore=genres"
URL_STAR_SCARPING = "https://www.imdb.com/search/name/?match_all=true&start="

# urls_app
URL_GENRE_CREATE_APP = BASE_URL_APP + 'genre/create'
URL_GENRE_DELETE_APP = BASE_URL_APP + 'genre/delete/'
URL_GENRE_LIST_APP = BASE_URL_APP + 'genre/list/'
URL_GENRE_GET_APP = BASE_URL_APP + 'genre/get/'

URL_STAR_CREATE_APP = BASE_URL_APP + 'star/create'
URL_STAR_DELETE_APP = BASE_URL_APP + 'star/delete/'
URL_STAR_LIST_APP = BASE_URL_APP + 'star/list/'
URL_STAR_LIST_INCOMPLETE_APP = BASE_URL_APP + 'star/incomplete/'
URL_STAR_GET_APP = BASE_URL_APP + 'star/get/'
URL_STAR_UPDATE_APP = BASE_URL_APP + 'star/update/'

URL_MOVIE_CREATE_APP = BASE_URL_APP + 'movie/create'
URL_MOVIE_DELETE_APP = BASE_URL_APP + 'movie/delete/'
URL_MOVIE_LIST_APP = BASE_URL_APP + 'movie/list/'
URL_MOVIE_GET_APP = BASE_URL_APP + 'movie/get/'
URL_MOVIE_UPDATE_APP = BASE_URL_APP + 'movie/update/'

EMAIL = 'a@email.com'
PASSWORD = '1'

FILE_NAME_KEYS = 'env.json'
