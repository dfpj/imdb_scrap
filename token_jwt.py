import json
import requests
import settings
from singelton import Singelton



class Token(metaclass=Singelton):
    def __init__(self):
        self._get_access()

    def _get_access(self):
        result = requests.get(settings.URL_CHAECK_PERMISSION, headers={
            'Authorization': f'Bearer {self._read_keys_in_env()[0]}'
        })
        if result.status_code == 401:
            self._get_auth_access_key()

    def _get_auth_access_refresh_key(self):
        result = requests.post(settings.URL_AUTHORIZATHION, data={
            'email': settings.EMAIL,
            'password': settings.PASSWORD
        })
        self._write_keys_in_env(json.loads(result.text)['access'], json.loads(result.text)['refresh'])

    def _get_auth_access_key(self):
        result = requests.post(settings.URL_ACCESS_KEY, data={
            'refresh': self._read_keys_in_env()[1],
        })
        if result.status_code == 401:
            self._get_auth_access_refresh_key()
        else:
            self._write_keys_in_env(json.loads(result.text)['access'], self._read_keys_in_env()[1])

    def _write_keys_in_env(self, access_key, refresh_key):
        with  open(settings.FILE_NAME_KEYS, 'w') as f:
            json.dump({"access": access_key, "refresh": refresh_key, }, f)

    def _read_keys_in_env(self):
        with  open(settings.FILE_NAME_KEYS) as f:
            data = json.load(f)
        return data['access'], data['refresh']

    @property
    def access_key(self):
        return self._read_keys_in_env()[0]
