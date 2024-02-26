from pprint import pprint

import requests
import yaml

str_route = 'api/v1/'       # API версия
filename = 'shop1.yaml'     # Название тестового файла для обновления данных поставщика

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5MDMzNjUzLCJpYXQiOjE3MDg5NDcyNTMsImp0aSI6IjU3ZTc0MDlmMzgwMzQwYjVhMmUzMDBlZmU0M2QxN2RhIiwidXNlcl9pZCI6InJvYm90ZWR1QHlhbmRleC5ydSJ9.hNiqRuYPXX3I_buNyXacvI1sqlU_yUc0CKS7aSFtv7Y"

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
#     json={'name': 'Продукт 1032', 'category': 1},
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
#     json={'email': 'shop1@yandex.ru', 'password': 'Shop222Shop'}
# )
# print(response.status_code)
# print(response.text)

# "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTUzOTI1MywiaWF0IjoxNzA4OTQ3MjUzLCJqdGkiOiI0ZTU5YjBlMjhjOTk0MWVhOTE2NzE0NTNkNDViNGI2YyIsInVzZXJfaWQiOiJyb2JvdGVkdUB5YW5kZXgucnUifQ.vJpWQp5pT9IaINQpDROCfiNmZ7wmaXhrJBdRzKlCcY4"
# "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5MDMzNjUzLCJpYXQiOjE3MDg5NDcyNTMsImp0aSI6IjU3ZTc0MDlmMzgwMzQwYjVhMmUzMDBlZmU0M2QxN2RhIiwidXNlcl9pZCI6InJvYm90ZWR1QHlhbmRleC5ydSJ9.hNiqRuYPXX3I_buNyXacvI1sqlU_yUc0CKS7aSFtv7Y"

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

# #  Создать пользователя
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}user/create/',
#     json={'email': 'shop1@yandex.ru',
#           'password': 'Shop222Shop',
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
#     json={'email': 'shop1@yandex.ru',
#           'token': '807286e4234faab5c582884c02847'}
# )
# print(response.status_code)
# print(response.text)

#  Проверка контактов пользователя
response = requests.get(
    f'http://127.0.0.1:8000/{str_route}user/contacts/',
)
print(response.status_code)
print(response.text)
