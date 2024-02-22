from pprint import pprint

import requests
import yaml

str_route = 'api/v1/'       # API версия
filename = 'shop1.yaml'     # Название тестового файла для обновления данных поставщика

# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}categories/'
# )
# print(response.status_code)
# print(response.text)

# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}categories/create/',
#     json={'name': 'Категория 11', 'shops': []}
# )
# print(response.status_code)
# print(response.text)

# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}products/'
# )
# print(response.status_code)
# print(response.text)

# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}products/create/',
#     json={'name': 'Продукт 1', 'category': 1}
# )
# print(response.status_code)
# print(response.text)

# Обновить данные поставщика
with open(filename, 'rb') as f:
    files = {'upload_file': f.read()}
values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
response = requests.post(
    f'http://127.0.0.1:8000/{str_route}supplier/data/',
    files=files,
    data=values
)
print(response.status_code)
print(response.text)

