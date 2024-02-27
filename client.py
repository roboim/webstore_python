from pprint import pprint

import requests
import yaml

str_route = 'api/v1/'       # API версия
filename = 'shop1.yaml'     # Название тестового файла для обновления данных поставщика
shop_id = 1                # Номер тестового магазина

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5MDQ0ODg0LCJpYXQiOjE3MDg5NTg0ODQsImp0aSI6ImE2MTYyNjM5Y2VlNDRhZmU4ZWNjNTRmNjA1NmRiNmUzIiwidXNlcl9pZCI6InNob3BAeWFuZGV4LnJ1In0.EdwuPWBtz0DSirJMF1A68eKRPOJYNQmVL45iypcGgGs"
token_refresh = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTU1MDQ4NCwiaWF0IjoxNzA4OTU4NDg0LCJqdGkiOiJjZDQyYjkyMjUxYjA0YTQ0YmI1Njg0NmYzMWUyMWE0NyIsInVzZXJfaWQiOiJzaG9wQHlhbmRleC5ydSJ9.5mGvRmJfB7nRyyHd7pjHSjRdb2tiMJVwZb3Qiyjmcvc"
token_admin = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5MDQwMzI0LCJpYXQiOjE3MDg5NTM5MjQsImp0aSI6Ijg5YzVlNzFjZDhhYjQ2Y2ViYWM4NWY5ZGI5OTdlYzI4IiwidXNlcl9pZCI6ImFkbWluQHlhbmRleC5ydSJ9.wXqfDeNXFalwOc9yv2Ump7pouHlk0duEmfF-ewVoXTY"
token_admin_refresh = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTU0NTkyNCwiaWF0IjoxNzA4OTUzOTI0LCJqdGkiOiIwNzJhYTY1NWQ1ZTQ0MzIzODIyYmRlNTVjZDhjNTdlMiIsInVzZXJfaWQiOiJhZG1pbkB5YW5kZXgucnUifQ.SjEZHJ_Xt_LF_ICQMREsItexgLmDDq0J1rG59HpNGAY"

# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}categories/'
# )
# print(response.status_code)
# print(response.text)

# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}categories/create/',
#     json={'name': 'Категория 12', 'shops': []}
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
#     json={'name': 'Продукт 1034', 'category': 1},
#     headers={'Authorization': f'Bearer {token_admin}'}
# )
# print(response.status_code)
# print(response.text)

# # Обновить данные поставщика
# with open(filename, 'rb') as f:
#     files = {'upload_file': f.read()}
# values = {'DB': 'postgres', 'OUT': 'yaml', 'user_id': '43'}
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}supplier/data/',
#     files=files,
#     data=values,
#     headers={'Authorization': f'Bearer {token_admin}'}
# )
# print(response.status_code)
# print(response.text)

# #  Получить токен
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}token/',
#     json={'email': 'shop@yandex.ru', 'password': 'admin1admin'}
# )
# print(response.status_code)
# print(response.text)

# #  Обновить токен
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}token/refresh/',
#     json={'email': 'admin@admin.ru', 'password': 'admin', 'refresh':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTUyNDE3NCwiaWF0IjoxNzA4OTMyMTc0LCJqdGkiOiJiMTIyYzNiOTVlMzg0YzhkOWY3YjdiOTAzNmI5NmUzNSIsInVzZXJfaWQiOiJhZG1pbkBhZG1pbi5ydSJ9.mvdR0DhtQpFX1e93D5_YwAIixqETcUhM1CR-mfMB8wk'}
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

# Запросить статус магазина
response = requests.get(
    f'http://127.0.0.1:8000/{str_route}supplier/status/{shop_id}/',
    headers={'Authorization': f'Bearer {token}'}
)
print(response.status_code)
print(response.text)

# Обновить статус магазина
response = requests.patch(
    f'http://127.0.0.1:8000/{str_route}supplier/status/{shop_id}/',
    json={'state': 'True'},
    headers={'Authorization': f'Bearer {token}'}
)
print(response.status_code)
print(response.text)


# #  Создать пользователя
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}user/create/',
#     json={'email': 'shop@yandex.ru',
#           'password': 'admin1admin',
#           'company': 'Test_company',
#           'position': 'Manager',
#           'username': 'Ilya',
#           'type': 'shop',
#           'first_name': 'Ilya',
#           'last_name': 'Net'}
# )
# print(response.status_code)
# print(response.text)

# #  Подтвердить пользователя
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}user/create/confirm/',
#     json={'email': 'admin@yandex.ru',
#           'token': '149988f5a6a3fa5bb1287b4b3cd2a9fdabf6079d6e3f1e'}
# )
# print(response.status_code)
# print(response.text)

# #  Проверка контактов пользователя
# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}user/contacts/',
#     headers={'Authorization': f'Bearer {token_admin}'}
# )
# print(response.status_code)
# print(response.text)

# #  Проверка контактов пользователя
# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}user/contacts/',
#     headers={'Authorization': f'Bearer {token}'}
# )
# print(response.status_code)
# print(response.text)

#
# #  Добавить контакт пользователя
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}user/contacts/',
#     json={'user': 43, 'city': 'Yakutsk', 'street': 'Mira', 'house': '1', 'structure': '', 'building': '', 'apartment': '', 'phone': '+712345667890'},
#     headers={'Authorization': f'Bearer {token_admin}'}
# )
# print(response.status_code)
# print(response.text)
