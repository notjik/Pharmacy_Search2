import sys
import requests

API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"


def geocode(address):
    server = 'http://geocode-maps.yandex.ru/1.x/'
    params = {'apikey': API_KEY,
              'geocode': address,
              'format': 'json'}
    resp = requests.get(server, params=params)
    if resp:
        resp = resp.json()
    else:
        raise RuntimeError('Ошибка выполнения запроса')
    return resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']


def get_coords(address):
    toponym = geocode(address)
    if not toponym:
        return None, None
    coords = toponym['Point']['pos'].split()
    return coords[0], coords[1]


def get_ll(address):
    top = geocode(address)
    if not top:
        return None, None
    return top['Point']['pos']

