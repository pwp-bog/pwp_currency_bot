import requests
from bs4 import BeautifulSoup
i = 0  # костыль

# Массив данных что бы сайт не блокировал запрос
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'accept': '*/*'
}

# Сбор данных о валютах, нужно для конвертации
typeofhostcheck = input(
    'Введите тип конвертера валюты:\n1. uzs > byn; 2. byn > uzs. ')
valueofvalute = input('Введите количество валюты: ')

# Настройка типа конвертера
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


# Функция get_html, которая запрашивает html код страницы, и принимает
# в качестве параметров url страницы и наши заголовки
def get_html(url, HEADERS):
    # Запрашиваем html код страницы
    r = requests.get(url, headers=HEADERS).text
    return r  # Возвращаем переменную содержащую html код


def get_content(html):  # создаем функцию get_content, которая в качестве параметра принимает
    #                   уже готовый html код страницы

    global i  # Добавление переменной "костыля" в функцию

    # Переменная для работы с библиотекой
    soup = BeautifulSoup(html, 'html.parser')

    # BeautifulSoup.
    # Во всем коде ищем тег div с классом input-group input-group-xlg-specific input__currency.
    # Возвращает массив.
    items = soup.find_all(
        'div', class_='input-group input-group-xlg-specific input__currency')

    # Перебираем все элементы данного массива.
    for item in items:

        # Добавляем к i 1, чтобы в будущем пропустить первое значение, знаю что это можно
        # Было сделать без костыля, но мне лень было искать как.
        i += 1
        if i == 2:
            item = item.find('input', class_='form-control')
            print()
            print('Результат: ' + str(item.get('value')) + valutename + '.')


# Вызовов функции
get_content(get_html(HOST, HEADERS))
