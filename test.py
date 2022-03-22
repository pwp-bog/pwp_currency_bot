import requests # инициализируем библиотеки.
from bs4 import BeautifulSoup
i = 0 # переменная i, выступает у меня в качестве костыля, так как потом нам вернет два кода.

# Создаём массив заголовков (Тут вся информация о браузере и операционной системе, сделано для того,
# чтобы сайт не заблокировал запрос.)
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'accept': '*/*'
}
# Спрашиваем у человека тип конвертера и количество валюты.
typeofhostcheck = input('Введите тип конвертера валюты:\n1. uzs > byn; 2. byn > uzs. ')
valueofvalute = input('Введите количество валюты: ')

# Настраиваем тип конвертера.
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



# Функция get_html, которая запрашивает html код страницы, и принимает в качестве параметров
# url страницы и наши заголовки.
def get_html(url, HEADERS):
    r = requests.get(url, headers=HEADERS).text # Запрашиваем html код страницы.
    return r # Возвращаем переменную r.

def get_content(html): # создаем функцию get_content, которая в качестве параметра принимает
    # уже готовый html код страницы.
    global i # добавляем в нашу функцию переменную i.
    soup = BeautifulSoup(html, 'html.parser') # создаем переменную для работы с библиотекой
    # BeautifulSoup.
    # Во всем коде ищем тег div с классом input-group input-group-xlg-specific input__currency.
    # Нам вернет массив.
    items = soup.find_all('div', class_='input-group input-group-xlg-specific input__currency')
    # Перебираем все элементы данного массива.
    for item in items:
        # Добавляем к i 1, чтобы в будущем пропустить первое значение, знаю что это можно
        # Было сделать без костыля, но мне лень было искать как.
        i += 1
        if i == 2: # Если i равняется двум:
            iteme = item.find('input', class_='form-control') # Ищем элемент input с классом
            # form-control.
            print() # Пропускаем одну строку.
            # Оформляем с помощью модуля colorama и выводим результат.
            print('Результат: '+ str(iteme.get('value')) + valutename + '.')

get_content(get_html(HOST, HEADERS)) # Вызываем функцию get_content, которой передаем возвращаемое значение
# функции get_html, помните, мы в функции get_html возвращали значение переменной r, так вот это оно и есть.