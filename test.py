# Сбор данных
a = input()

# Проверка на конвертируемые валюты
if "byn in uzs" in a:

    # Поиск индекса для нахождения числа
    index = a.index("/")
    # Создание строки с одним числом
    prenum = (a[:index])
    # Удаление пробелов из строки содержащее число, с последующей конвертацией в int
    num = int(prenum.replace(" ", ""))


# TODO Добавить удаление пробелов до получения индексов
# TODO Добавить преобразование в маленькие буквы для полученной строки

    print(f"convert {num} byn in uzs")

elif "uzs in byn" in a:
    index = a.index("/")
    prenum = (a[:index])
    num = int(prenum.replace(" ", ""))

    print("convert {num} uzs in byn")
else:
    print("error")
