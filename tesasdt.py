import requests
from bs4 import BeautifulSoup

from converter import HEADERS


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'accept': '*/*'
}

typeofhostcheck = input(
    'Введите тип конвертера валюты:\n1. uzs > byn; 2. byn > uzs. ')
valueofvalute = input('Введите количество валюты: ')

if typeofhostcheck == '1':
    valutename = ' byn'
    HOST = 'https://pokur.su/uzs/byn/' + valueofvalute + '/'
elif typeofhostcheck == '2':
    valutename = ' uzs'
    HOST = 'https://pokur.su/byn/uzs/' + valueofvalute + '/'
else:
    valutename = ' kzt'
    print('Вы ввели неверный тип конвертера! Переключаю автоматически на: usd > byn.')
    HOST = 'https://pokur.su/usd/byn/' + valueofvalute + '/'



def get_html(url, HEADERS):
    r = requests.get(url, headers=HEADERS).text
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find_all(
        'div', class_='input-group input-group-xlg-specific input__currency'
    )

    for q in items:
        if q == 2:
            q = q.find('input', class_='form-control')
            print()
            print('Результат: ' + str(q.get('value')) + valutename + '.')


get_content(get_html(HOST, HEADERS))
