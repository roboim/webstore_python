import requests

str_route = 'api/v1/'
response = requests.get(
    f'http://127.0.0.1:8000/{str_route}categories/'
)
print(response.status_code)
print(response.text)

# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}categories/create/',
#     json={'name': 'Категория 9', 'shops': []}
# )
# print(response.status_code)
# print(response.text)

response = requests.get(
    f'http://127.0.0.1:8000/{str_route}products/'
)
print(response.status_code)
print(response.text)

# response = requests.post(
#     f'http://127.0.0.1:8000/{str_route}products/create/',
#     json={'name': 'Продукт 1', 'category': 1}
# )
# print(response.status_code)
# print(response.text)


