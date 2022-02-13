import requests
from pprint import pprint


def find_bis(ll, spn, request, locale="ru_RU"):
    server = 'http://search-maps.yandex.ru/v1/'
    API_KEY = 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3'
    params = {'apikey': API_KEY,
              'text': request,
              'lang': locale,
              'll': ll,
              'spn': ','.join((spn, spn)),
              'type': 'biz'}
    response = requests.get(server, params=params).json()
    return [tuple(map(str, response['features'][0]['geometry']['coordinates'])),
            response['features'][0]['properties']['description'],
            response['features'][0]['properties']['CompanyMetaData']['name'],
            response['features'][0]['properties']['CompanyMetaData']['Hours']['text']]
