# Сбор данных
input_data = input("write information in this window: ")


# Преобразование данных в нужный вид
input_data = input_data.replace(" ", "")
input_data = input_data.lower()


# Поиск валюты в преобразованной строке
if "byninuzs" in input_data:
    value = "byn"
elif "uzsinbyn" in input_data:
    value = "uzs"
else:
    value = "unknown value"
    print(value)


# Преобразование данных в число денег
for i in range(len(input_data)):
    if input_data[i].isdigit() == False:
        money = input_data[:i]
        break


print(money, value)
