from pprint import pprint

import requests
import yaml

str_route = 'api/v1/'       # API версия
filename = 'shop1.yaml'     # Название тестового файла для обновления данных поставщика

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5NTQ0NzcwLCJpYXQiOjE3MDg2ODA3NzAsImp0aSI6IjVhNmI4Y2I2OTYxZDQzZjY4N2M0ZTEzZThiNjE4YWRmIiwidXNlcl9pZCI6MX0.MDS6B_9RN2uP7yjdKyVaeUrksAR3-OxSHuy1ZCtT8Wg"

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

response = requests.post(
    f'http://127.0.0.1:8000/{str_route}products/create/',
    json={'name': 'Продукт 1000', 'category': 1},
    headers={'Authorization': f'Bearer {token}'}
)
print(response.status_code)
print(response.text)

# # Обновить данные поставщика
# with open(filename, 'rb') as f:
#     files = {'upload_file': f.read()}
# values = {'DB': 'postgres', 'OUT': 'yaml'}
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}supplier/data/',
#     files=files,
#     data=values
# )
# print(response.status_code)
# print(response.text)

# #  Получить токен
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}token/',
#     json={'email': 'admin@admin.ru', 'password': 'admin'}
# )
# print(response.status_code)
# print(response.text)

# "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTI3Mjc3MCwiaWF0IjoxNzA4NjgwNzcwLCJqdGkiOiI2OTNhNzYyYzk4NGQ0NmRiYjM0ZDMxN2IzOTAwYjA0ZiIsInVzZXJfaWQiOjF9.PTKWlBuShD0sejTmtMzUKYabT_uPSUodqwKA5DWNj2A"
# "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5NTQ0NzcwLCJpYXQiOjE3MDg2ODA3NzAsImp0aSI6IjVhNmI4Y2I2OTYxZDQzZjY4N2M0ZTEzZThiNjE4YWRmIiwidXNlcl9pZCI6MX0.MDS6B_9RN2uP7yjdKyVaeUrksAR3-OxSHuy1ZCtT8Wg"
