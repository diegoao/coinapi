import requests

url = 'https://randomuser.me/api/'

response = requests.get(url)

if response.status_code == 200:
    print(response. json())
else:
    print('Algo ha ido mal')
    print('Código del error', response.status_code)
    print('Error', response.reason)
