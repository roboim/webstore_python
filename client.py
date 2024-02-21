import requests

response = requests.get(
    'http://127.0.0.1:8000/demo/'
)
print(response.status_code)
print(response.text)

# response = requests.post(
#     'http://127.0.0.1:8000/demo/',
#     json={'name': 'Магазин 1', 'url': 'www.магазин1.ру', 'state': True}
# )
# print(response.status_code)
# print(response.text)


