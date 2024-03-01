from pprint import pprint

import requests
import yaml

str_route = 'api/v1/'       # API версия
filename = 'shop1.yaml'     # Название тестового файла для обновления данных поставщика
shop_id = 1                # Номер тестового магазина

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5MDQ0ODg0LCJpYXQiOjE3MDg5NTg0ODQsImp0aSI6ImE2MTYyNjM5Y2VlNDRhZmU4ZWNjNTRmNjA1NmRiNmUzIiwidXNlcl9pZCI6InNob3BAeWFuZGV4LnJ1In0.EdwuPWBtz0DSirJMF1A68eKRPOJYNQmVL45iypcGgGs"
token_refresh = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTU1MDQ4NCwiaWF0IjoxNzA4OTU4NDg0LCJqdGkiOiJjZDQyYjkyMjUxYjA0YTQ0YmI1Njg0NmYzMWUyMWE0NyIsInVzZXJfaWQiOiJzaG9wQHlhbmRleC5ydSJ9.5mGvRmJfB7nRyyHd7pjHSjRdb2tiMJVwZb3Qiyjmcvc"
token_admin = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5Mzc0Mzg4LCJpYXQiOjE3MDkwNDEwMDAsImp0aSI6ImYzMTI5ZTRlODQxNTQ1ZGRhMmY3YjVkNTgxYjEwMWRmIiwidXNlcl9pZCI6ImFkbWluQHlhbmRleC5ydSJ9.E0vJGeJKcs0wUfPg-ZiMlPfjOL3t9Y69Y3aJYFMxuGk"
token_admin_refresh = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTg3OTk4OCwiaWF0IjoxNzA5Mjg3OTg4LCJqdGkiOiIwNmUwYjRlOTc3NWI0N2U5OTBkNTQwMDdlMWNiZDRjNCIsInVzZXJfaWQiOiJhZG1pbkB5YW5kZXgucnUifQ.x0ifrMX2mnTejmvMVC59RWfWHoY8_6s9Uwi-awyb0v8"
token_buyer = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMDAwNzk2LCJpYXQiOjE3MDkwNTAwMTksImp0aSI6IjI5MmJkOTIyNmJiZTRkZjQ5YWY3ZjliYTRiNjYyZmRlIiwidXNlcl9pZCI6ImJ1eWVyQHlhbmRleC5ydSJ9.eKGHveudA2jK9vpH7H3lZX_quy8vTQqF-9E-LP7Cc7o"
token_buyer_refresh = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTcyODc5NiwiaWF0IjoxNzA5MTM2Nzk2LCJqdGkiOiJhNjhmOTNhMzgyNWE0Mjg1OGM1NGI3ZjE1MGExNWMyYyIsInVzZXJfaWQiOiJidXllckB5YW5kZXgucnUifQ.vhYRVJ2Mn6DJHb2-Ca_dK-u4c-tPzqpvBsG7pTWTjvA"


# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}categories/',
#     headers={'Authorization': f'Bearer {token_admin}'}
# )
# print(response.status_code)
# print(response.text)

# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}categories/create/',
#     json={'name': 'Категория 12', 'shops': []}
# )
# print(response.status_code)
# print(response.text)

# # Запросить доступные продукты
# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}products/'
# )
# print(response.status_code)
# print(response.text)

# # Создать продукты
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}products/create/',
#     json={'name': 'Продукт 1034', 'category': 1},
#     headers={'Authorization': f'Bearer {token_admin}'}
# )
# print(response.status_code)
# print(response.text)

# #  Просмотр продукции
# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}products/info/?shop_id=1&category_id=224',
#     headers={'Authorization': f'Bearer {token_buyer}'}
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
#     json={'email': 'buyer@yandex.ru', 'password': 'admin1admin'}
# )
# print(response.status_code)
# print(response.text)

# #  Обновить токен
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}token/refresh/',
#     json={'email': 'admin@yandex.ru', 'password': 'admin1admin', 'refresh': token_admin_refresh}
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

# # Запросить статус магазина
# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}supplier/status/{shop_id}/',
#     headers={'Authorization': f'Bearer {token}'}
# )
# print(response.status_code)
# print(response.text)
#
# # Обновить статус магазина
# response = requests.patch(
#     f'http://127.0.0.1:8000/{str_route}supplier/status/{shop_id}/',
#     json={'state': 'True'},
#     headers={'Authorization': f'Bearer {token}'}
# )
# print(response.status_code)
# print(response.text)

# #  Создать пользователя
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}user/create/',
#     json={'email': 'buyer@yandex.ru',
#           'password': 'admin1admin',
#           'company': 'Buyer',
#           'position': 'engineer',
#           'username': 'Maxim',
#           'type': 'buyer',
#           'first_name': 'Maxim',
#           'last_name': 'Guest'}
# )
# print(response.status_code)
# print(response.text)

# #  Подтвердить пользователя
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}user/create/confirm/',
#     json={'email': 'buyer@yandex.ru',
#           'token': 'e55fb6dac987a65a362daddb536222f789eec063d8438b'}
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

# #  Проверка корзины пользователя
# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}cart/',
#     headers={'Authorization': f'Bearer {token_buyer}'}
# )
# print(response.status_code)
# print(response.text)

# #  Создание корзины пользователя
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}cart/',
#     json={'orders': [
#         [
#             {'shop_id': '1', 'products': [{'product_id': '3', 'quantity': '2'}, {'product_id': '5', 'quantity': '1'}]},
#             {'shop_id': '2', 'products': [{'product_id': '6', 'quantity': '1'}]}
#         ],
#         [
#             {'shop_id': '1', 'products': [{'product_id': '3', 'quantity': '1'}]},
#             {'shop_id': '2', 'products': [{'product_id': '6', 'quantity': '1'}]}]
#         ]
#     },
#     headers={'Authorization': f'Bearer {token_buyer}'}
# )
# print(response.status_code)
# print(response.text)

# #  Удаление позиций заказа пользователя
# response = requests.delete(
#     f'http://127.0.0.1:8000/{str_route}cart/',
#     json={'orders': [
#         [
#             {'order_id': '20'},
#             {'shop_id': '1', 'products': [{'product_id': '3'}, {'product_id': '5'}]},
#         ],
#         [
#             {'order_id': '21'},
#             {'shop_id': '2', 'products': [{'product_id': '6'}]}]
#         ]
#     },
#     headers={'Authorization': f'Bearer {token_buyer}'}
# )
# print(response.status_code)
# print(response.text)

# #  Изменение позиций заказа пользователя
# response = requests.put(
#     f'http://127.0.0.1:8000/{str_route}cart/',
#     json={'orders': [
#             [
#                 {'order_id': '42'},
#                 {'shop_id': '1', 'products': [{'product_id': '4', 'quantity': '77'}, {'product_id': '5', 'quantity': '78'}]},
#                 {'shop_id': '2', 'products': [{'product_id': '6', 'quantity': '3'}]}
#             ],
#             [
#                 {'order_id': '43'},
#                 {'shop_id': '2', 'products': [{'product_id': '6', 'quantity': '4'}]}
#             ]
#         ]
#     },
#     headers={'Authorization': f'Bearer {token_buyer}'}
# )
# print(response.status_code)
# print(response.text)


# #  Создать заказ пользователя
# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}order/',
#     json={
#         'order_id': '42',
#         'state': 'new',
#         'contact_id': '2'
#     },
#     headers={'Authorization': f'Bearer {token_buyer}'}
# )
# print(response.status_code)
# print(response.text)

# #  Просмотреть заказы пользователя
# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}order/',
#     headers={'Authorization': f'Bearer {token_buyer}'}
# )
# print(response.status_code)
# print(response.text)
#
# #  Просмотреть заказы магазина
# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}order/',
#     headers={'Authorization': f'Bearer {token_admin}'}
# )
# print(response.status_code)
# print(response.text)

# #  Защита от удаления заказа пользователя
# response = requests.delete(
#     f'http://127.0.0.1:8000/{str_route}order/51/',
#     json={'state': 'canceled'},
#     headers={'Authorization': f'Bearer {token_buyer}'}
# )
# print(response.status_code)
# print(response.text)

# #  Отмена заказа пользователем
# response = requests.patch(
#     f'http://127.0.0.1:8000/{str_route}order/42/',
#     json={'state': 'canceled'},
#     headers={'Authorization': f'Bearer {token_buyer}'}
# )
# print(response.status_code)
# print(response.text)

#  Изменение заказа магазином
response = requests.patch(
    f'http://127.0.0.1:8000/{str_route}order/42/',
    json={'state': 'delivered'},
    headers={'Authorization': f'Bearer {token_admin}'}
)
print(response.status_code)
print(response.text)

# #  Просмотр заказа пользователем
# response = requests.get(
#     f'http://127.0.0.1:8000/{str_route}order/43/',
#     headers={'Authorization': f'Bearer {token_buyer}'}
# )
# print(response.status_code)
# print(response.text)
