from main import get_content_from_imdb,ConnectApp
import settings


def genre_scarping():
    geners = []
    content = get_content_from_imdb(settings.URL_GENRES_SCARPING)
    for item in content.findAll('td'):
        title = item.find('a').text
        geners.append(title)
    return geners


def create_genre(genre):
    ConnectApp().post(settings.URL_GENRE_CREATE_APP, data={"title": genre})


def create_geners():
    geners = genre_scarping()
    for genre in geners:
        create_genre(genre)

def list_genre():
    result =ConnectApp().get(settings.URL_GENRE_LIST_APP)
    return result[1]

def get_genre(genre):
    result =ConnectApp().get(settings.URL_GENRE_GET_APP + genre)
    return result[1]

def delete_genre(genre):
    ConnectApp().delete(settings.URL_GENRE_DELETE_APP + genre)

