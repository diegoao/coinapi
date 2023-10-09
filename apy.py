import requests

apikey = '54CC9DB5-A9E5-4DEF-AFCA-BFAEE77C7995'
server = 'https://rest.coinapi.io'
endpoint = '/v1/assets'
# FUCTION1 endpoint = 'v1/assets?filter_asset_id-EUR; BTC;USD; ETH' SE PUEDE HACER ASI PARA REDUCIR TRAFICO
url = server + endpoint

headers = {'X-CoinApi-key': apikey}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    json_response = response.json()
    for coin in json_response:
        id = coin.get('asset_id')
        # SI UTILIZAMOS LA FUNCION 1 PODEMOS ELIMINAR ESTA LINEA
        if (id in ['BTC', 'USD', 'EUR', 'ETH']):
            print(id, '-', coin.get('name'), coin.get('type_is_crypto'))
else:
    print('Algo no ha ido bien. Error ', response.status_code, response.reason)
