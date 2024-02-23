from pprint import pprint

import requests
import yaml

str_route = 'api/v1/'       # API версия
filename = 'shop1.yaml'     # Название тестового файла для обновления данных поставщика

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5NTQ3Mjc3LCJpYXQiOjE3MDg2ODMyNzcsImp0aSI6ImFlZTYyOTAzMGY4MTRhYjdiZjQwNzJmZDcwMTE5OGVkIiwidXNlcl9pZCI6ImFkbWluQGFkbWluLnJ1In0.rDqFfdvWtrSebX0Gt5dE73qkgoIap3DFw7txUmvX5OI"

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
#     json={'name': 'Продукт 1012', 'category': 1},
#     headers={'Authorization': f'Bearer {token}'}
# )
# print(response.status_code)
# print(response.text)

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

# "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTI3NTQ1MywiaWF0IjoxNzA4NjgzNDUzLCJqdGkiOiIxYzczMDk2ZDBiMTQ0NTI1Yjg3ZGRkYzk4MWIzNTM3NCIsInVzZXJfaWQiOiJhZG1pbkBhZG1pbi5ydSJ9.FxCGiK4LPrdKXPkXqCwJx7KQCXXDR499Rxsd5V0L9Uc"
# "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5NTQ3NDUzLCJpYXQiOjE3MDg2ODMyNzcsImp0aSI6IjFkNzMyMGI2ZGJmZDRkNGQ4NjliNjcyNTMwMDY3NGJlIiwidXNlcl9pZCI6ImFkbWluQGFkbWluLnJ1In0.ixITH2PpQZIVm1rHr69ws07985IzEbRAr3tkW1Adzqg"

# #  Обновить токен
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}token/refresh/',
#     json={'email': 'admin@admin.ru', 'password': 'admin', 'refresh':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTI3NTI3NywiaWF0IjoxNzA4NjgzMjc3LCJqdGkiOiI3Yjk1ODY5MWZmZjI0ZjdlOTNkZGNiYzg5NDc1NjZhNiIsInVzZXJfaWQiOiJhZG1pbkBhZG1pbi5ydSJ9.2y6tkpLe6GIvQKNRySWDN2bHmS-EBervxrKc8ulZok4'}
# )
# print(response.status_code)
# print(response.text)

# #  Занести токен в чёрный список
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}token/blacklist/',
#     json={'email': 'admin@admin.ru', 'password': 'admin', 'refresh':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTI3NDU2NiwiaWF0IjoxNzA4NjgyNTY2LCJqdGkiOiIyMzYxMDA1NGIyYzc0MWNjYjIwZjQ5YjZlNGZhZTEzOCIsInVzZXJfaWQiOjF9.sPJLwmB01lj-7XkBqQr_vGQsfp4nAHl99uhJ4kaHMwI'}
# )
# print(response.status_code)
# print(response.text)

#  Создать пользователя
response = requests.post(
    f'http://127.0.0.1:8000/{str_route}user/create/',
    json={'email': 'shop@shop.ru',
          'password': 'Shop222Shop',
          'company': 'Test_company',
          'position': 'Manager',
          'username': 'Ilya',
          'type': 'shop',
          'first_name': 'Ilya',
          'last_name': 'Net'}
)
print(response.status_code)
print(response.text)
