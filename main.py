import settings
from token_jwt import Token
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from singelton import Singelton


def get_content_from_imdb(url):
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    result = session.get(url, headers=settings.HEADER_EXTRA)
    content = BeautifulSoup(result.text, 'html.parser')
    return content

class ConnectApp(metaclass=Singelton):
    def __init__(self):
        _access_key=Token().access_key
        self.headers={'Authorization': f'Bearer {_access_key}'}

    def get(self,url):
        result = requests.get(url, headers=self.headers)
        return result.status_code, result.text

    def post(self,url, data):
        result = requests.post(url + "/", data=data, headers=self.headers)
        return result.status_code, result.text


    def put(self,url, data):
        result = requests.put(url + "/", data=data, headers=self.headers)
        return result.status_code, result.text


    def delete(self,url):
        result = requests.delete(url + "/", headers=self.headers)
        return result.status_code, result.text
